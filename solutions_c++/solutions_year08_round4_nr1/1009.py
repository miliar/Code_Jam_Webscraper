#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

struct Point
{
   Point(int lastchanged, const vector<int>& gatetype, int cost = 0)
      : m_lastchanged(lastchanged), m_cost(cost), m_gatetype(gatetype) { }
   bool operator<(const Point& rhs) const
   {
      return m_cost > rhs.m_cost;
   }
   int m_lastchanged;
   int m_cost;
   vector<int> m_gatetype;
};

int main(void)
{
   int n;
   cin >> n;
   for(int i = 1; i <= n; ++i)
   {
      int m; // number of nodes;
      int v; // desired value
      int g;
      int c;
      int nodev;
      cin >> m >> v;
      vector<int> value(m + 1, -1);
      vector<int> gatetype(m + 1, 0);
      vector<int> changable(m + 1, 0);
      for(int j = 1; j <= (m - 1)/2; ++j)
      {
         cin >> g >> c;
         gatetype[j] = g;
         changable[j] = c;
         /*
#ifndef NDEBUG
         cerr << "Gate " << j << ": ";
         cerr << (c?"changable":"fixed") << " ";
         cerr << (g?"AND":"OR") << " gate\n";
#endif
         */
      }
      for(int j = (m-1)/2 + 1; j <= m; ++j)
      {
         cin >> nodev;
         value[j] = nodev;
      }

      bool ansfound = false;
      priority_queue<Point> candidate;
      candidate.push(Point(0, gatetype, 0)); 
      while(!candidate.empty())
      {
         Point curr = candidate.top();
         candidate.pop();
         //unchanged
         for(int j = (m-1)/2; j >= 1; --j)
         {
            if(curr.m_gatetype[j]) // AND
               value[j] = (value[j * 2] && value[j * 2 + 1]);
            else // OR
               value[j] = (value[j * 2] || value[j * 2 + 1]);
         }
#ifndef NDEBUG
         for(int j = 1; j <= (m - 1) / 2; ++j)
            cerr << curr.m_gatetype[j] << " ";
         cerr << endl;
         for(int j = 1; j <= m; ++j)
            cerr << value[j] << " ";
         cerr << endl;
#endif

         if(value[1] == v)
         {
            ansfound = true;
            cout << "Case #" << i << ": " << curr.m_cost << endl;
            break;
         }

         int chgpos;
         for(chgpos = curr.m_lastchanged + 1;
               chgpos <= (m-1)/2 && !changable[chgpos]; ++chgpos)
            ;

         // a changable position or end
         if(chgpos > (m-1)/2)
            continue;
         // a changable position
         curr.m_lastchanged = chgpos;
         candidate.push(curr);
         (curr.m_gatetype[chgpos]) ^= 1;
         ++(curr.m_cost);
         candidate.push(curr);
      }

      if(!ansfound)
         cout << "Case #" << i << ": IMPOSSIBLE\n";
   }
   return 0;
}

