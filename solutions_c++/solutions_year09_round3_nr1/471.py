
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
typedef V( int )        VI;
typedef V( VI )         VVI;
typedef V( bool )       VB;
typedef V( VB )         VVB;
typedef V( PI  )        VPI;
typedef V( string )     VS;
typedef V( VS )         VVS;
typedef int             I ;

int main()
{
	int nt;S(nt);
	I ii=0;
	while(nt--)
	{
		ii++;
		cout<<"Case #"<<ii<<": ";
		string a;
		cin>>a;
		I l=a.size();
		VI arr(200,0);
		I diff=0;
		REP(i,l)
		{
			if(arr[a[i]]==0)
			{
				diff++;
				arr[a[i]]++;
			}
		}
		I base;
		I n=l;
		if(diff==1) base=2;
		else base=diff;
		
		VI mark(200,-1);
		vector<long long> b(n);
		b[0]=1;
		int i=1;
		mark[a[0]]=1;
		for(;i<n;i++)
		{
			if(a[i]!=a[i-1]) break;
			b[i]=1;
		}
		if(i<n)
		{
			b[i]=0;
			mark[a[i]]=0;
			i++;
		}
		I val=2;
		for(;i<n;i++)
		{
			if(mark[a[i]]!=-1)
			{
				b[i]=mark[a[i]];
			}
			else 
			{
				b[i]=mark[a[i]]=val++;
			}
		}
		LL mod=1;
		LL ans=0;
		for(I i=n-1;i>=0;i--)
		{
			ans=ans+mod*b[i];
			mod=mod*base;
		}
		cout<<ans<<endl;
	}
}
