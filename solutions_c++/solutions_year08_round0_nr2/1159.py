#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <utility>


using namespace std;

typedef pair<int,int> pii;

struct comp : binary_function<pii, pii, bool>
{
  bool operator () (pii a, pii b)
  {
       return (a.first > b.first || (a.first == b.first && a.second > b.second));
  }
};

struct compi : binary_function<int, int, bool>
{
  bool operator () (int a, int b)
  {
       return (a > b);
  }
};

int main()
{
    int n, i, j, t, na, nb, p1, q1, no_ina, no_inb;
    string str;
    priority_queue<pair<int, int>, vector<pii>, comp> QA, QB;
    
    
    cin>>n;
    for (i = 0; i < n; i++)
    {
        priority_queue<int, vector<int>, compi> a, b;
        no_ina = 0;
        no_inb = 0;
        cin>>t>>na>>nb;
        getline(cin, str);
        
        for (j = 0; j < na; j++)
        {
            getline(cin, str);
            p1 = ((str[0] - '0') * 10 + str[1] - '0') * 60 + (str[3] - '0') * 10 + str[4] - '0';
            q1 = ((str[6] - '0') * 10 + str[7] - '0') * 60 + (str[9] - '0') * 10 + str[10] - '0';
            QA.push(make_pair(p1, q1 + t));
        }
        for (j = 0; j < nb; j++)
        {
            getline(cin, str);
            p1 = ((str[0] - '0') * 10 + str[1] - '0') * 60 + (str[3] - '0') * 10 + str[4] - '0';
            q1 = ((str[6] - '0') * 10 + str[7] - '0') * 60 + (str[9] - '0') * 10 + str[10] - '0';
            QB.push(make_pair(p1, q1 + t));
            
        }
        
        while (!QA.empty() || !QB.empty())
        {
          if (QA.empty())
          {
             pii p = QB.top();
             if (b.empty() || b.top() > p.first)
                no_inb++;
             else
                b.pop();
             QB.pop();
          }
          else
          {
            if (QB.empty())
            {
               pii p = QA.top();
               if (a.empty() || a.top() > p.first)
                 no_ina++;
               else
                 a.pop();
               QA.pop();
            }
            else
            {
               pii p = QA.top();
               pii q = QB.top();
               if (p.first < q.first)
               {
                 if (a.empty() || a.top() > p.first)
                   no_ina++;
                 else
                   a.pop();
                 b.push(p.second);
                 QA.pop();
               }
               else
               {
                 if (b.empty() || b.top() > q.first)
                   no_inb++;
                 else
                   b.pop();
                 a.push(q.second);
                 QB.pop();
               }
            }
          }
        }// while
          
                
        cout<<"Case #"<<i+1<<": "<<no_ina<<" "<<no_inb<<endl;           
    }
    
    return 0;
}
            
