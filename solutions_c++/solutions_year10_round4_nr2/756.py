#include<iostream>
#include<cmath>

using namespace std;

int p;
int m[2222];
int cnt ;

bool Check(int s, int t)
{
     for(int i = s; i < t; i++)
     {
             if(m[i] < p) return false;
     }
     return true;
}

void dfs(int s, int t)
{
     if(Check(s, t))
        return ;
     else
     {
         for(int i = s; i < t; i++)
         {
                 m[i]++;
         }
         cnt++;
         dfs(s, (s+t)/2);
         dfs((s+t)/2, t);
     }
     return ;
}

int main()
{
   freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    
    int cas, icas;
    cin >> cas;
    int i, j;
    for(icas = 1; icas <= cas; icas++)
    {
             cout << "Case #" << icas << ": ";
             cin >> p;
             int n = pow(2.0, p);
             for(i = 0; i < n; i++)
             {
                   cin >> m[i];
             }
             for(i = p-1; i >= 0; i--)
             {
                   int pp = pow(2.0, i);
                   int t;
                   for(j = 0; j < pp; j++)
                      cin >> t;
             }
             cnt = 0;
             dfs(0, n);
             cout << cnt << endl;
    }
    return 0;
}
