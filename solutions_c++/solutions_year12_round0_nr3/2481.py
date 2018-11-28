
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

const int inf = (1<<28);
const double pi = (2.0*acos(0.0));
const double eps = 1e-9;

#define _rep( i, a, b, x ) for( __typeof(b) i = ( a ); i <= ( b ); i += x )
#define rep( i, n ) _rep( i, 0, n - 1, 1 )

#define pb push_back

int len[2000000+2];
int p[20];
typedef pair < int , int > pii;
set < pii > S;
vector < pii > vi;
void precalc()
{
    int i , j ,k;
    S.clear();
    vi.clear();
    for(i=0;i<=2000000;i++)
        len[i] = log10(i) + 1;
    for(i=0;i<=8;i++) p[i] = (int) pow(10.,double(i));
    //for(i=0;i<=9;i++) printf("%d\n",p[i]);
    for(i=1;i<=2000000;i++)
    {
        //int p= 1;
        //printf("%d\n",i);
        for(j=0;j<=len[i]-1;j++)
        {
            int ii = i;
            int tmp= ii%p[j];ii/=p[j];
            tmp*=p[len[ii]]; tmp+=ii;ii=tmp;
            //if(i<1000)
            //if(i<1000)printf("%d %d\n",i,ii);
            if(ii>2000000) continue;
            if(len[i]==len[ii] && i<ii)
            {
                if(S.find(pii(i,ii))==S.end())
                {
                    vi.pb(pii(i,ii));
                    S.insert(pii(i,ii));
                }
            }

        }
    }

}
int main(void)
{
    //freopen("C-large.in","r",stdin);
    //freopen("outCCC.txt","w",stdout);
    int i,j,k,kase=0;
    precalc();
    int t; scanf("%d",&t);
    while(t--)
    {
        int a , b;
        scanf("%d %d",&a,&b);
        int sz = vi.size();
        int ans = 0;
        rep(i,sz)
        {
            if(vi[i].first > b) break;
            if(vi[i].first >=a && vi[i].second<=b)
                ans++;
        }
        printf("Case #%d: %d\n",++kase,ans);
    }
    return 0;
}
