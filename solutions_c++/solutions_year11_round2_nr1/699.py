//GCC 4.6.0, define IGEL_ACM to make the code work properly

#pragma comment (linker, "/STACK:16777216")
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

using namespace std;

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


string a[200];

double wp[200];
double owp[200],oowp[200];

int wins[200],sum[200];

void solution()
{

    int itnum;
    scanf("%d",&itnum);
    FI(it,itnum)
    {
        int n;
        scanf("%d",&n);
        FI(i,n) a[i]=gs();
        FI(i,n)
        {
            wins[i]=sum[i]=0;
            FI(j,n) if (a[i][j]!='.') {sum[i]++; wins[i]+=a[i][j]-'0';}
            wp[i]=wins[i]/double(sum[i]);
        }
        FI(i,n)
        {
            double res=0;
            FI(j,n) if (a[i][j]!='.') res+=(wins[j]-(a[j][i]-'0'))/double(sum[j]-1);
            owp[i]=res/sum[i];
        }
        FI(i,n)
        {
            oowp[i]=0;
            FI(j,n) if (a[i][j]!='.') oowp[i]+=owp[j];
            oowp[i]/=sum[i];
        }
        printf("Case #%d:\n",it+1);
        FI(i,n)
        printf("%.20lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
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

