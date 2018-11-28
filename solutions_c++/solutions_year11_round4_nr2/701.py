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


int r,c,d;
string a[600];

inline double dist(double x, double y, double xx, double yy)
{ return sqrt(sqr(x-xx)+(y-yy)); }

void solution()
{
    int tn;
    scanf("%d",&tn);
    FI(it,tn)
    {
        int best=0;
        scanf("%d%d%d",&r,&c,&d);
        FI(i,r) a[i]=gs();
        FI(i,r) FI(j,c) a[i][j]-='0';
        FI(i,r) FI(j,c) FOR(k,3,max(r,c)+1)
        if (i+k<=r && j+k<=c)
        {
            double x=0,y=0,cx=(i+(k-1)/2.0),cy=(j+(k-1)/2.0);
            LL sum=0;
            FI(ii,k)
            {
                for (int jj=((ii==0 || ii==k-1)?1:0); jj<((ii==0 || ii==k-1)?k-1:k); ++jj)
                {
                    x+=(a[i+ii][j+jj]+d)*(i+ii-cx);
                    y+=(a[i+ii][j+jj]+d)*(j+jj-cy);
                    sum+=(a[i+ii][j+jj]+d);
                }
            }
            x/=sum; y/=sum;
            if (abs(x)<eps && (abs(y)<eps)) best=max(best,k);
        }
        if (best==0) printf("Case #%d: IMPOSSIBLE\n",it+1);
        else printf("Case #%d: %d\n",it+1,best);
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



