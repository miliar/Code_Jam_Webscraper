
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

class my
{
	public:

};
string a,b="welcome to code jam";
I l,m;

VVI mp(10000 , VI(20));
I mod=10000;

int fn(I p , I q)
{
	if(q==m) return 1;
	if(mp[p][q]!=-1) return mp[p][q];
	I count=0;
	I pp=p;
	for(;p<l;p++)
	{
		if(a[p]==b[q])
			count = (count+fn(p+1,q+1))%mod;
	}
	mp[pp][q]=count;
	return count;
}
I dig(I n)
{
	I ret=0;
	while(n)
	{
		n=n/10;
		ret++;
	}
	return ret;
}
int main()
{
	I nt;S(nt);
	char ss[100];
	gets(ss);

	REP(ii,nt)
	{
		cout<<"Case #"<<ii+1<<": ";
		char temp[10000];
		gets(temp);
		
		a=temp ;
		l=a.size();
		m=b.size();
		
		REP(i,l)REP(j,m)mp[i][j]=-1;

		I ans=(fn(0,0))%mod;	
		if(ans==0)
		{
			printf("0000\n");
			continue;
		}
		I dd=dig(ans);
		REP(i,4-dd)printf("0");
		printf("%d\n",ans);
	}
}
