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


LL n,d;
LL px[1000];
LL pc[1000];

double f(double left)
{
    double res=abs(px[0]-left); left+=d;
    FI(i,n) for (int j=((i==0)?1:0); j<pc[i]; ++j)
    {
        //dout(left << ' ' << px[i]);
        if (px[i]-left>0) left=max(left,px[i]-res);
        else {res=max(res,abs(left-px[i]));}
        left+=d;
        //dout(res);
    }
    return res;
}

void solution()
{

    int itnum;
    scanf("%d",&itnum);
    FI(it,itnum)
    {
        scanf("%lld%lld",&n,&d);
        FI(i,n) scanf("%lld%lld",&px[i],&pc[i]);
        LL sum=0; FI(i,n) sum+=pc[i];
        double l=px[0]-sum*d-100.0;
        double r=px[0];
        //dout(f(-4));
       //*
        FI(iter,300)
        {
            double lm=l+(r-l)/3.0, rm=r-(r-l)/3.0;
            if (f(lm)<f(rm)) r=rm;
            else l=lm;
        }//*/
        printf("Case #%d: %.20lf\n",it+1,f((l+r)/2.0));
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

