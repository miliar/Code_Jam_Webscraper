#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
using namespace std;

int n,s,p,ans,tcase;
int normal[50],ss[50],ar[110];

int main()
{
    freopen ("inputb.in","r",stdin);
    freopen ("outputb.out","w",stdout);
    FORS(i,0,10){
        FORS(j,0,10){
            FORS(k,0,10){
                if (abs(i-j) <= 1 && abs(i-k) <= 1 && abs(j-k) <= 1) {
                    normal[i+j+k] = max(normal[i+j+k],max(i,max(j,k)));
                }
                else if (abs(i-j) <= 2 && abs(i-k) <= 2 && abs(j-k) <= 2) {
                    ss[i+j+k] = max(ss[i+j+k],max(i,max(j,k)));
                }
            }
        }
    }
    cin >> tcase;
    FORN(t,tcase){
        ans = 0;
        cin >> n >> s >> p;
        FORN(i,n){
            cin >> ar[i];
        }
        sort(ar,ar+n);
        FORN(i,n){
            if (normal[ar[i]] >= p) ans++;
            else if (ss[ar[i]] >= p && s > 0) {
                ans++;
                s--;
            }
        }
        cout << "Case #" << t+1 <<": " << ans << endl;
    }
    //system("pause");
    return 0;
}
//ASK Template Modified
