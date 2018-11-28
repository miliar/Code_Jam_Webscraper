#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <math.h>
#include <queue>
#include <string.h>
#include <sstream>
#define mst(a,v) memset(a, v, sizeof(a))
#define msk(s,p) for(p=(s-1)&s;p=(p-1)&s)
#define _USE_MATH_DEFINES
#define fo(i,n) for(i=0;i<n;i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define MP make_pair
#define sz(x) ((int)x.size())
using namespace std;

typedef long long ll;

string s;
map < char, char > mp;
set < string > st;
int ans;
int outdeg[50], indeg[50];
int g[50][50];
bool vis[100];

int val(char c)
{
    if (c >= 'a' && c <= 'z')
        {
            //cout << c << " " << c-'a';
            return c - 'a';
        }
    return 26 + c - '0';
}

bool visit(int x)
{
    int i;
    vis[x] = true;
    bool dif = false;
    ans += max(outdeg[x], indeg[x]);
    if (outdeg[x] != indeg[x]) dif = true;
    fo(i,50) if (g[x][i])
        {
            if (!vis[i] && visit(i)) dif = true;
        }
    return dif;
}

int main(void)
{
    mp['o'] = '0';
    mp['i'] = '1';
    mp['e'] = '3';
    mp['a'] = '4';
    mp['s'] = '5';
    mp['t'] = '7';
    mp['b'] = '8';
    mp['g'] = '9';

    int t, tt, i, j;
    cin >> t;
    fo(tt, t)
        {
            int k;
            cin >> k >> s;
            st.clear();
            int n = sz(s);
            memset(g, 0, sizeof(g));
            fo(i,(n-1))
                {
                    //st.insert(s[i] + s[i+1]);
                    g[val(s[i])][val(s[i+1])] = 1;
                    bool f = false;
                    if (mp.find(s[i]) != mp.end())
                        {
                            g[val(mp[s[i]])][val(s[i+1])] = 1;
                            //st.insert(mp[s[i]] + s[i+1]);
                            f = true;
                        }
                    if (mp.find(s[i+1]) != mp.end())
                        {
                            g[val(s[i])][val(mp[s[i+1]])] = 1;
                            //st.insert(s[i] + mp[s[i+1]]);
                            if (f)
                                {
                                    //st.insert(mp[s[i]] + mp[s[i+1]]);
                                    g[val(mp[s[i]])][val(mp[s[i+1]])] = 1;
                                }
                        }
                }

            memset(outdeg, 0, sizeof(outdeg));
            memset(indeg, 0, sizeof(indeg));
            fo(i,50)fo(j,50)
                if(g[i][j])
                    {
                        //cout << i << " " << j << endl;
                        outdeg[i]++;
                        indeg[j]++;
                    }
            ans = 0;

            memset(vis, false, sizeof(vis));
            fo(i,50)
                if (!vis[i] && outdeg[i])
                    {
                        if (!visit(i)) ans++;
                    }
                        
            cout << "Case #" << tt + 1 << ": " << ans << endl;
        }
}
