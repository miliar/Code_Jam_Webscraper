
#include<iostream>
#include <vector>
#include <stack>
#include <map>
#include <queue>
#include <list>
#include <algorithm>
#include <set>
#include <cstring>
#include<string.h>
#include <cmath>
#include<math.h>
#include <cassert>
#include <sstream>
#include <climits>
#include <deque>
#include <fstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
using namespace std;

#define FOR(i,a,b)         for(int i= (int )a ; i < (int )b ; ++i) 
#define REP(i,n)           FOR(i,0,n)
#define PB                 push_back
#define PP                 pop()
#define EM                 empty()
#define INF                2000000000
#define PF                 push_front
#define ALL(x)             x.begin(),x.end()
#define SORT(x)            sort(ALL(x))
#define V(x)               vector< x >
#define PRINT(x)           cout << #x << " " << x << endl
#define LET(x,a)           __typeof(a) x(a)
#define IFOR(i,a,b) 	   for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	   IFOR(it,v.begin(),v.end())
#define PRESENT(c,x) 	   ((c).find(x) != (c).end())
#define SZ(x) 		   x.size();
#define CPRESENT(c,x) 	   (find(c.begin(),c.end(),x) != (c).end())
#define S(N)		   scanf("%d",&N)
#define PR(v)              REP(iii,v.size())cout<<v[iii]<<" ";cout<<endl;

bool isUpperCase(char c){return c>='A' && c<='Z';}//NOTES:isUpperCase
bool isLowerCase(char c){return c>='a' && c<='z';}//NOTES:isLowerCase
bool isLetter(char c){return c>='A' && c<='Z' || c>='a' && c<='z';}//NOTES:isLetter
bool isDigit(char c){return c>='0' && c<='9';}//NOTES:isDigit(


//translator 
char toLowerCase(char c){return (isUpperCase(c))?(c+32):c;}//NOTES:toLowerCase
char toUpperCase(char c){return (isLowerCase(c))?(c-32):c;}//NOTES:toUpperCase
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toInt
long long  toLL(string s){long long  r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toLL
//double toFloat(string s){float r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toFloat
//double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toDouble


typedef map<int,int>    MI;
typedef pair<int,int>   PI;
typedef long long int   LL;
typedef V( double )     VD;
typedef V( VD )         VVD;
typedef V( bool )       VB;
typedef V( VB )         VVB;
typedef V( PI  )        VPI;
typedef V( string )     VS;
typedef V( VS )         VVS;
typedef int             I ;

double sqr(double n)
{
	return n*n;
}
int main()
{
	I nt;S(nt);
	I ii=0;
	while(nt--)
	{
		ii++;
		cout<<"Case #"<<ii<<": ";
		I n;S(n);
		VVD a(n,VD(3));
		REP(i,n)
			REP(j,3) cin>>a[i][j];
		if(n==1)
		{
			cout<<a[0][2]<<endl;
			continue;
		}
		if(n==2)
		{
			cout<<max(a[0][2],a[1][2])<<endl;
			continue;
		}
		double min=INF;
		REP(i,n)
		{
			double r1=a[i][2];
			I p=(i+1)%n , q=(i+2)%n;
		//	cout<<a[p][0]<<" "<<a[p][1]<<" "<<a[q][0]<<" "<<a[q][1]<<endl;
			double r2=sqrt(sqr(a[p][0]-a[q][0])+(sqr(a[p][1]-a[q][1])));
		//	cout<<r2<<endl<<endl;
			r2 +=a[p][2]+a[q][2];
			r2=r2/2;
			if(r2 < max(a[p][2],a[q][2])) r2=max(a[p][2],a[q][2]);

			if(max(r1,r2)<min) min=max(r1,r2);
		}
		printf("%.8lf\n",min);
	//	cout<<min<<endl;
	}
}
