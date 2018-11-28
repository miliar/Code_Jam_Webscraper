#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <queue>

using namespace std;

struct Point
{
   Point(int e, int q, int c)
      : m_eng(e), m_que(q), m_cost(c) { }

   bool operator<(const Point& rhs) const
   {
      return m_cost > rhs.m_cost;
   }

   int m_eng;
   int m_que;
   int m_cost;
};

int main(void)
{
   int n;
   cin >> n;
   for(int i = 1; i <= n; ++i)
   {
      cout << "Case #" << i << ": ";

      vector<string> engines;
      int s;
      cin >> s;
      cin.ignore();
      if(s == 0)
      {
         cout << "0\n";
         continue;
      }
      engines.reserve(s);
      string enginename;
      for(int j = 0; j < s; ++j)
      {
         getline(cin, enginename);
         engines.push_back(enginename);
      }

      vector<string> queries;
      int q;
      cin >> q;
      cin.ignore();
      if(q == 0)
      {
         cout << "0\n";
         continue;
      }
      queries.reserve(q);
      string queryname;
      for(int j = 0; j < q; ++j)
      {
         getline(cin, queryname);
         queries.push_back(queryname);
      }

      bool reached[s][q];
      for(int j = 0; j < s; ++j)
         for(int k = 0; k < q; ++k)
            reached[j][k] = false;
      
      // Dijkstra
      priority_queue<Point> candidate;
      for(int j = 0; j < s; ++j)
         if(queries[0] != engines[j])
            candidate.push(Point(j, 0, 0));
      for(;;)
      {
         Point bestpoint = candidate.top();
         candidate.pop();
         int engid = bestpoint.m_eng;
         int queid = bestpoint.m_que;
         int cost = bestpoint.m_cost;
         if(queid == (q - 1))
         {
            cout << cost << endl;
            break;
         }
         reached[bestpoint.m_eng][bestpoint.m_que] = true;
         for(int j = 0; j < s; ++j)
         {
            if(!reached[j][queid + 1] && queries[queid + 1] != engines[j])
            {
               candidate.push(Point(j, queid + 1, 
                  (j == engid)?(cost):(cost + 1)));
            }
         }
      }
   }
}
