
#include <iostream>
#include <fstream>
#include <map>
#include <queue>
#include <vector>

using namespace std;

map < int, vector<int> > m;
int mark[2000];

bool bfs(int start)
{
     memset(mark, 0, sizeof(mark));
     
     queue <int> q;
     q.push(start);
     
     while(!q.empty())
     
     {
        int current = q.front();
        mark[current]++;
        if(mark[current] >=2 ) return true;

        for(int i = 0; i < m[current].size(); i++)
        {
                q.push(m[current][i]);
        }
     }
     
     return false;
}
 

int main()
{
    int N;

    
    ifstream cin("pc1.in");
    ofstream fout("pc1.out");
    cin >> N;    
    int n;
    for(int t = 1; t <= N; t++)
    {
            fout << "Case #" << t << ":";
            cin >> n;
            
            for(int i = 1; i <= n; i++)
            {
                    int m_i;
                    cin >> m_i;
                    for(int j = 1; j <= m_i; j++)
                    {
                            int p;
                            cin >> p;
                            m[p].push_back(i);
                    }
            }
            
            for(int i = 1; i <= n; i++)
            {
                    if(bfs(i)) 
                    {
                               fout << "Yes" << endl;
                               goto la;
                    };
            }
            fout << "No" << endl;
la:
            ;            
    } 
}
