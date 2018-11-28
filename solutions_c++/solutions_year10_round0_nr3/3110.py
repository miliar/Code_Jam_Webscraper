#include<iostream>
#include<stdio.h>

using namespace std;

// for small data set

int main()
{
    int T, Case;
    unsigned long long R,k;
    int N;
    unsigned long g[1000];
    int visited[1000],onetime_flag[1000];
    int i;
    unsigned long long j,tr,s;
    
    freopen("C:\\Users\\vads\\Downloads\\C-small-attempt0.in","r",stdin);
    freopen("1.out","w",stdout);
    
    cin >> T;
    while(Case < T)
    {
              cin >> R >> k >> N;
              for(i = 0; i < N;i++)          
                    cin >> g[i],visited[i] = 0;
              tr = j = 0;
              while(tr < R)
              {
                       s = 0;
                       memset(onetime_flag,0,sizeof(onetime_flag));
                       while(s <= k)
                       {
                               if(s+g[j] > k)  break;          
                               s += g[j], onetime_flag[j]++;
                               if(onetime_flag[j] != 1) break;
                               visited[j++]++;
                               if(j == N)  j = 0;
                       }
                       tr++;
              }
              for(i = s = 0;i < N;i++)
                    s += g[i] * visited[i];
              cout << "Case #" << ++Case << ": " << s << endl;
    }    
    return 0;    
}
