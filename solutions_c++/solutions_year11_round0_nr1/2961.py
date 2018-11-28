#include <vector>
#include <iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<string.h>
#include<queue>
#include <set>
#include<map>
#include<string>
#include<stdexcept>
#include<errno.h>

using namespace std;
template <class T> void show(T a, int n) { for (int i = 0; i < n; ++i) cout << a[i] << ' '; cout << endl; }
template <class T> void show(T a, int r, int l) { for (int i = 0; i < r; ++i) show(a[i], l); cout << endl; }
#define max(a, b) (a > b?a:b)
#define min(a, b) (a < b?a:b)

#define ms(a, v)    memset(a, v, sizeof(a))
#define pb push_back
#define mp make_pair
#define pii pair<int, int>

typedef long long LL;

const int N = 128 * 2;
const int M = 5000;
const int oo = 10000 * 10000 * 10;

int n;
char tag[N];
int pos[N];

inline int dis(int i, int j)
{
    return abs(i - j) + 1;
}

int solve()
{
    int i, j, k;
    int opos = 1, bpos = 1;
    int ot = 0, bt = 0;
    
    for(i = 0; i < n;++i)
    {
        if( tag[i] == 'O' )
        {
            if( bt > ot )
            {
                ot = ot + dis(opos, pos[i]);
                ot = max(ot, bt + 1);
            }
            else
            {
                ot += dis(opos, pos[i]);
            }
            opos = pos[i];
        }
        else
        {
            bt += dis(bpos, pos[i]);
            bt = max(bt, ot + 1);
            bpos = pos[i];
        }
    }
    return max(bt, ot);
}

int main()
{
        freopen("in", "r", stdin);
        freopen("out","w",stdout); 
    int i, j, cas = 0;
    
    scanf("%d", &cas);
    for(int cc = 0; cc < cas;++cc)
    {
        scanf("%d", &n);
        for(i = 0;i < n;++i)
        {
            scanf(" %c %d", &tag[i], &pos[i]);
        }
        int ans = solve();
        printf("Case #%d: %d\n", cc + 1, ans);
    }
    
 
    

    
   
    return 0;
}

