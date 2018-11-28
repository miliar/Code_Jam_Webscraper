#include <iostream>
#define maxn 10
#define maxg 10000001
using namespace std;
int main()
{
    freopen("C-small.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int T;
    long R,k,N;
    long g[maxn+1]; 
    cin >> T;
    for(int i=1;i<=T;i++)
    {
            memset(g,0,sizeof(g));
            cin >> R >> k >> N;
            for (int j=0;j<N;j++) cin >> g[j];
            long long sum = 0;
            long count = 0;
            long long sub = 0;
            int begin = 0;
            int j = 0;
            while (count < R)
            {
                  int sonhom = 0;
                  j = begin;
                  while (sub + g[j] <= k && sonhom < N) 
                  {
                     sub += g[j];
                     sonhom++;
                     j = (j+1) % N;
                  }
                  if (sonhom == N)
                  {
                     sum = sub * R;
                     break;
                  }
                  if (sub + g[j] > k)
                      {
                         count++;
                         sum += sub;
                         sub = 0;
                         begin = j;
                      }
            }
            cout << "Case #" << i << ": " << sum;
            if (i <= T-1) cout << endl;
    }
    return 0;
}
