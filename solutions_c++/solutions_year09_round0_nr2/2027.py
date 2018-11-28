
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
typedef V(PI)           VPI;
typedef V(VPI)          VVPI;
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
I n,m;
VVI a(101,VI(101));

bool isSink(I &i , I &j)
{
	if(i>0 and a[i-1][j]< a[i][j]) return false;
	if(i<n-1 and a[i+1][j]< a[i][j]) return false;
	if(j>0 and a[i][j-1]< a[i][j]) return false;
	if(j<m-1 and a[i][j+1]< a[i][j]) return false;
	return true;
}

PI direction(I &i, I &j)
{
	I min=INF;
	if(i>0 and a[i-1][j]< min) min=a[i-1][j];
	if(i<n-1 and a[i+1][j]< min) min=a[i+1][j];
	if(j>0 and a[i][j-1]< min) min=a[i][j-1];
	if(j<m-1 and a[i][j+1]< min) min=a[i][j+1];
	
	PI ret;
	if(i>0 and a[i-1][j]==min)
	{
		ret.first=i-1;
		ret.second=j;
		return ret;
	}
	if(j>0 and a[i][j-1]==min)
	{
		ret.first=i;
		ret.second=j-1;
		return ret;
	}
	if(j<m-1 and a[i][j+1]==min)
	{
		ret.first=i;
		ret.second=j+1;
		return ret;
	}
	if(i<n-1 and a[i+1][j]==min)
	{
		ret.first=i+1;
		ret.second=j;
		return ret;
	}
}
void fn(I i , I j, const VVPI &dir , VVI &ans)
{
	PI temp(i,j);
	if(i>0 and dir[i-1][j]==temp)
	{
		ans[i-1][j]=ans[i][j];
		fn(i-1,j,dir,ans);
	}
	if(i<n-1 and dir[i+1][j]==temp)
	{
		ans[i+1][j]=ans[i][j];
		fn(i+1,j,dir,ans);
	}
	if(j>0 and dir[i][j-1]==temp)
	{
		ans[i][j-1]=ans[i][j];
		fn(i,j-1,dir,ans);
	}
	if(j<m-1 and dir[i][j+1]==temp)
	{
		ans[i][j+1]=ans[i][j];
		fn(i,j+1,dir,ans);
	}
}

int main()
{
	I nt;S(nt);
	REP(ii,nt)
	{
		cout<<"Case #"<<ii+1<<":\n";
		S(n);S(m);
		REP(i,n)REP(j,m)S(a[i][j]);	

		VVI ans(n,VI(m,-1));
		
		I ind=0;
		REP(i,n)REP(j,m)
			if(isSink(i,j)) ans[i][j]=ind++;
		
		/*
		REP(i,n)
		{
			REP(j,m)
				cout<<ans[i][j]<<" ";
			cout<<endl;
		}
		*/
		
		PI inf(INF,INF);

		VVPI dir(n,VPI(m , inf));

		REP(i,n)REP(j,m)
		{	
			if(!isSink(i,j))
			{
				dir[i][j]=direction(i,j);
			}
		}
		
		REP(i,n)REP(j,m)
		{
			if(isSink(i,j))
			{
				fn(i,j,dir , ans);
			}
		}
		map<int, char> mp;
		I index=0;
		REP(i,n)
		{
			REP(j,m)
			{
				if(mp[ans[i][j]])
					cout<<mp[ans[i][j]];
				else 
				{
					mp[ans[i][j]]=char('a'+index++);
					cout<<mp[ans[i][j]];
				}
				if(j!=m-1)cout<<" ";
			//	cout<<" ";
			}
			cout<<endl;
		}
	}
}


