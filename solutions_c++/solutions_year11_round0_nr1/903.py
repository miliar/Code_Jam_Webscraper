#include <iostream>
using namespace std;

int seq[100];
int pos[2];
int N;

bool move(int r, int cnt)
{   
    int t = seq[cnt]%2;
    int p = seq[cnt]/2;
    
    //cout << t << " " << p << endl;
    if (t == r && p == pos[r])
    {
       return true;
    }
    else
    {
        for (int i = cnt; i < N; i++)
        {
            int t2 = seq[i]%2;
            int p2 = seq[i]/2;
            if (t2 == r)
            {
                 if (pos[r] < p2) pos[r]++;
                 else if (pos[r] > p2) pos[r]--;
                 break;
            }
        }
    }
    return false;
}

void solve()
{
     cin >> N;
    
     for (int i = 0; i < N; i++)
     {
         char let;
         int a;
         cin >> let >> a;
         if (let == 'O') seq[i] = a*2;
         else seq[i] = a*2 + 1;
     }
     
     pos[0] = pos[1] = 1;
     
     int cnt = 0, ans = 0;
     while (1)
     {
          if (cnt == N) break;
          bool f1 = move(0, cnt);
          bool f2 = move(1, cnt);
          if (f1 || f2) cnt++;
          ans++;
     }
     cout << ans << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
