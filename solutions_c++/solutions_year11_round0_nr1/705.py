//GNU C++ gcc version 4.6.0
//define IGEL_ACM to make program work properly

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <numeric>
#include <complex>
#include <string>
#ifdef IGEL_ACM
#include <ctime>
#endif

#include <sys/resource.h>
void setstacksize(rlim_t sz)
{
    struct rlimit rl;
    int result;
    result = getrlimit(RLIMIT_STACK, &rl);
    if (result == 0)
    {
        if (rl.rlim_cur < sz)
        {
            rl.rlim_cur = sz;
            result = setrlimit(RLIMIT_STACK, &rl);
            if (result != 0)
            {
                fprintf(stderr, "setrlimit returned result = %d\n", result);
            }
        }
    }
}

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> pnt;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector <vector < pair <int, int> > > VVP;

#define FI(i,a) for (int i=0; i<(a); ++i)
#define RFI(i,a) for (int i=(a); i>=0; --i)
#define FOR(i,s,e) for (int i=(s); i<(e); ++i)
#define RFOR(i,e,s) for (int i=(e); i>=s; --i)
#define MEMS(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define mp make_pair
#define ALL(a) a.begin(),a.end()
#define ISIN(s,a) (s.find(a)!=s.end())
#define sqr(a) ((a)*(a))
#define abs(a) (((a)>0)?(a):(-(a)))
#define CPY(a, b) memcpy(a, b, sizeof(a))

#define dout(a) cerr << a << endl;
#define sout(a) cerr << a << "  ";

const double pi = 3.14159265358979323846264338327950288419716939937511;
const double eps = 1e-9;

char ch_ch_ch[1<<20];
string gs() {scanf("%s",ch_ch_ch); return string(ch_ch_ch);}
string gl() {gets(ch_ch_ch); return string(ch_ch_ch);}


int n;
int a[200];
char who[200];
int nxt[200];

//int dp[110][110][110];

int R(int posb, int poso, int need)
{
    if (need==n) return 0;
 /*   int &r=dp[posb][poso][need];
    if (r!=-1) return r;*/

    bool pushed=false;

    if (who[need]=='O')
    {
        if (poso==a[need]) pushed=true;
        else poso+=(a[need]-poso>0)?1:-1;
        if (nxt[need]!=n && posb!=a[nxt[need]]) posb+=(a[nxt[need]]>posb)?1:-1;
    } else
    {
        if (posb==a[need]) pushed=true;
        else posb+=(a[need]>posb)?1:-1;
        if (nxt[need]!=n && poso!=a[nxt[need]]) poso+=(a[nxt[need]]>poso)?1:-1;
    }
    return R(posb,poso,need+pushed)+1;

}


void solution()
{
    int cnum;
    scanf("%d",&cnum);
    FI(it,cnum)
    {

        scanf("%d",&n);
        FI(i,n) cin >> who[i] >> a[i];
        FI(i,n)
        {
            nxt[i]=n;
            FOR(j,i+1,n) if (who[j]!=who[i]) {nxt[i]=j; break;}
        }

       // MEMS(dp,-1);

        int res=R(1,1,0);
        printf("Case #%d: %d\n",it+1,res);
    }



}




int main()
{

        setstacksize(1024*1024*1024);   

#ifdef IGEL_ACM
	freopen("sample.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	clock_t beg_time = clock();
#else
	//freopen("drawing.dat", "r", stdin);
	//freopen("drawing.sol", "w", stdout);
#endif

        
	solution();


#ifdef IGEL_ACM
	fprintf(stderr,"Time: %.3lf\n",1.0*(clock()-beg_time)/CLOCKS_PER_SEC);
#endif

    return 0;
}

