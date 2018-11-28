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

typedef long long LL;
typedef unsigned long long ULL;
typedef pair <int, int> pnt;
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
#define CPY(a, b) memcpy(a, b, sizeof(a))

#define dout(a) cerr << a << endl
#define sout(a) cerr << a << "  "


const double pi = 3.14159265358979323846264338327950288419716939937511;
const double eps = 1e-12;
//*
char ch_ch_ch[1<<20];
string gs() {scanf("%s",ch_ch_ch); return string(ch_ch_ch);}
string gl() {gets(ch_ch_ch); return string(ch_ch_ch);}
inline int gi() {int x; scanf("%d",&x); return x;}
//*/

string s[]={"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

string r[]={"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"};

char mapping[333];

void solution()
{     
    FI(i,3) FI(j,r[i].size()) mapping[s[i][j]]=r[i][j];
    mapping['z']='q';
    mapping['q']='z';
    int tn;
    cin >> tn;
    gl();
    FI(it,tn)
    {
        string ss=gl();
        string res="";
        FI(i,ss.size()) res+=mapping[ss[i]];
        printf("Case #%d: ",it+1);
        cout << res << endl;
    }
   
   
}




int main(int argc, char** argv)
{
    
       
#ifdef IGEL_ACM
        //freopen("sample.in","r",stdin);
        //*
        freopen("jam.txt","r",stdin);
	freopen("out.txt", "w", stdout); //*/
	clock_t beg_time = clock();
#else
        //freopen(argv[1],"r",stdin);
	freopen("c3.in", "r", stdin);
	freopen("c3.out", "w", stdout);
#endif
        
        solution(); 


#ifdef IGEL_ACM
	fprintf(stderr,"Time: %.3lf\n",1.0*(clock()-beg_time)/CLOCKS_PER_SEC);
#endif

    return 0;
}