#include <iostream>
using namespace std;

long long R, K, N;
long long g[1000];

long long people[1000], rides[1000];

void addleft(long long, long long, long long);

void dfs(long long pos, long long p, long long r)
{
     if (rides[pos] != -1)
     {
          long long cyclep = p - people[pos];
          long long cycler = r -  rides[pos];
          
          addleft(pos, p + cyclep*((R - r)/cycler), r + cycler*((R - r)/cycler));
          return;
     }
     
     if (r == R) { addleft(pos, p, r); return; }
     
     people[pos] = p;
     rides[pos] = r;
     
     long long i = pos;
     long long added = 0;
     for (;;)
     {
         if (added + g[i] > K) break;
         added += g[i];
         i++;
         if (i == N) i = 0;
         if (i == pos) break;
     }
     
     dfs(i, p + added, r + 1);
     return ;
}

void addleft(long long pos, long long p, long long r)
{
     for (; r < R; r++)
     {
         long long i = pos;
         long long added = 0;
         for (;;)
         {
             if (added + g[i] > K) break;
             added += g[i];
             i++;
             if (i == N) i = 0;
             if (i == pos) break;
         }
         p += added;
         pos = i;
     }
     cout << p << endl;
}

void solve()
{
     cin >> R >> K >> N;
     for (int i = 0; i < N; i++) cin >> g[i];
     memset(people, -1, sizeof(people));
     memset(rides, -1, sizeof(rides));

     dfs(0, 0, 0);
}

int main()
{
    int T;
    cin >> T;
    for (int q = 1; q <= T; q++)
    {
        cout << "Case #" << q << ": ";
        solve();
    }
}
