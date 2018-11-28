#include <iostream>
#include <set>
#include <vector>
#define BASE 91
#define MOD 6661313
#define BASE2 93
using namespace std;

set<pair<int, unsigned int> > S;

void solve()
{
     S.clear();
     int N, M;
     cin >> N >> M;
     
     S.insert(make_pair(0, 0));
     for (int i = 0; i < N; i++)
     {
         string s;
         cin >> s;
         s += '/';
         
         int hash1 = 0;
         unsigned int hash2 = 0;
         for (int i = 0; i < s.size(); i++)
         {
             if (s[i] == '/') S.insert(make_pair(hash1, hash2));
             
             hash1 = (hash1*BASE + s[i])%MOD;
             hash2 = hash2*BASE2 + s[i];
         }
     }
     
     int ans = 0;
     for (int i = 0; i < M; i++)
     {
         string s;
         cin >> s;
         s += '/';
         
         int hash1 = 0, hash2 = 0;
         for (int i = 0; i < s.size(); i++)
         {
             if (s[i] == '/' && S.find(make_pair(hash1, hash2)) == S.end())
             {
                  S.insert(make_pair(hash1, hash2));
                  ans++;
             }
             
             hash1 = (hash1*BASE + s[i])%MOD;
             hash2 = hash2*BASE2 + s[i];
         }
     }
     cout << ans << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) 
    {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
    return 0;    
}
