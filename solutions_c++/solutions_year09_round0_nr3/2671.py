#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define MP(X,Y) make_pair(X,Y)

#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

#define REP(i,n) FOR(i,0,(n)-1)
#define FOR(i,a,b) for(int i = (a);i<=(b);++i)
#define ALL(x) ((x).begin(),(x).end())
#define CLR(x,a) memset(x,a,sizeof(x))

#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}

template<class T> inline T gcd(T a,T b)
  {if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b)
  {if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline T euclide(T a,T b,T &x,T &y)
  {if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}
   if(b<0){T d=euclide(a,-b,x,y);y=-y;return d;}
   if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}

template<class T> inline vector<pair<T,int> > factorize(T n)
  {vector<pair<T,int> > R;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);R.push_back(make_pair(i,C));}
   i++;if (i>n/i) i=n;}if (n>1) R.push_back(make_pair(n,1));return R;}

template<class T> inline bool isPrimeNumber(T n)
  {if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}

template<class T> inline T eularFunction(T n)
  {vector<pair<T,int> > R=factorize(n);T r=n;for (int i=0;i<R.size();i++)r=r/R[i].first*(R[i].first-1);return r;}


double dist(double x1,double y1,double x2,double y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}
double distR(double x1,double y1,double x2,double y2){return sqr(x1-x2)+sqr(y1-y2);}
template<class T> T cross(T x0,T y0,T x1,T y1,T x2,T y2){return (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);}
int crossOper(double x0,double y0,double x1,double y1,double x2,double y2)
  {double t=(x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);if (fabs(t)<=eps) return 0;return (t<0)?-1:1;}
bool isIntersect(double x1,double y1,double x2,double y2,double x3,double y3,double x4,double y4)
  {return crossOper(x1,y1,x2,y2,x3,y3)*crossOper(x1,y1,x2,y2,x4,y4)<0 && crossOper(x3,y3,x4,y4,x1,y1)*crossOper(x3,y3,x4,y4,x2,y2)<0;}
bool isMiddle(double s,double m,double t){return fabs(s-m)<=eps || fabs(t-m)<=eps || (s<m)!=(t<m);}

bool isUpperCase(char c){return c>='A' && c<='Z';}
bool isLowerCase(char c){return c>='a' && c<='z';}
bool isLetter(char c){return c>='A' && c<='Z' || c>='a' && c<='z';}
bool isDigit(char c){return c>='0' && c<='9';}
char toLowerCase(char c){return (isUpperCase(c))?(c+32):c;}
char toUpperCase(char c){return (isLowerCase(c))?(c-32):c;}

template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}
int64 toInt64(string s){int64 r=0;istringstream sin(s);sin>>r;return r;}
double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}

template<class T> void stoa(string s,int &n,T A[]){n=0;istringstream sin(s);for(T v;sin>>v;A[n++]=v);}
template<class T> void atos(int n,T A[],string &s){ostringstream sout;for(int i=0;i<n;i++){if(i>0)sout<<' ';sout<<A[i];}s=sout.str();}
template<class T> void atov(int n,T A[],vector<T> &vi){vi.clear();for (int i=0;i<n;i++) vi.push_back(A[i]);}
template<class T> void vtoa(vector<T> vi,int &n,T A[]){n=vi.size();for (int i=0;i<n;i++)A[i]=vi[i];}
template<class T> void stov(string s,vector<T> &vi){vi.clear();istringstream sin(s);for(T v;sin>>v;vi.push_bakc(v));}
template<class T> void vtos(vector<T> vi,string &s){ostringstream sout;for (int i=0;i<vi.size();i++){if(i>0)sout<<' ';sout<<vi[i];}s=sout.str();}

string wcj = "welcome to code jam";
//string wcj = "we";


int countWordsEx(string phrase)
{
	int count = 0;
	int wcjIdx = 0;
	int offset = 0;	
	int* offsets = new int[wcj.size()];
	memset(offsets, 0, wcj.size());
	do	
	{
		char currChar = wcj[wcjIdx];
		size_t posChar = phrase.find(currChar, offset);
		if(posChar != string::npos)
		{
			offset = posChar+1;
			offsets[wcjIdx] = posChar+1;

			wcjIdx++;
			if(wcjIdx == wcj.size())
			{
				wcjIdx--;
				offset = offsets[wcjIdx];
				count++; // one more found
				if(count >= 9999)
					break;
			}
		}	
		else
		{
			wcjIdx--;
			offset = offsets[wcjIdx];
		}
	}	
	while(wcjIdx >= 0);

	delete [] offsets;

	return(count);
}

int main()
{
	int n;

	FILE* inputFile		= fopen("C-small-attempt1.in", "r");
	FILE* outputFile	= fopen("output.out", "w");

	fscanf(inputFile,"%d\n", &n);
	
	for (int i=1; i<=n; i++)
	{	
		int count;

		char phrase[1024];
		memset(phrase, 0, sizeof(phrase));

		fgets(phrase, 1024, inputFile);
		if(phrase[strlen(phrase)-1] == '\n')
			phrase[strlen(phrase)-1] = '\0';	
		
		count = countWordsEx(phrase);

		fprintf(outputFile, "Case #%d: %04d\n", i, count);						
	}

	fflush(outputFile);

	fclose(inputFile);
	fclose(outputFile);
	 
	return(0);
}

