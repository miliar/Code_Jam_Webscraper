#pragma comment (linker, "/STACK:16777216")
#include <algorithm> 
#include <cctype> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <deque> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <vector> 

using namespace std; 

template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

#define bublic public
#define TynKogep TOPCODER 
#define clr(a); memset(a,0,sizeof(a));
#define pb push_back
#define sz size()  
#define ld long double
#define ll long long
#define istr istringstream

int a[510][510],n,k,u[510][510],z,U[510][510],x,y,t[510][510],st;
long long ans;

void dfs(int x,int y,int l)
{
//	cout<<x<<" "<<l<<" "<<u[x]<<endl;
	if (l==0) return;
	if (t[x][y]<st)
	if (u[x][y]) {t[x][y]=st; z++;}
	U[x][y]=1;
	U[y][x]=1;
	for(int i=0;i<n;i++)
	if (a[x][i] && !U[x][i] && !U[i][x]) dfs(x,i,l-1);
	for(int i=0;i<n;i++)
	if (a[y][i] && !U[y][i] && !U[i][y]) dfs(y,i,l-1);
	U[x][y]=0;
	U[y][x]=0;
}

void rec(int x,int y)
{
	st++;
//	cout<<x<<" "<<y<<"!"<<endl;
	z=0;
	dfs(x,y,3);
//	cout<<z<<endl;
	ans*=k-z;
	ans%=1000000009;
	u[x][y]=1;
	u[y][x]=1;
	for(int i=0;i<n;i++)
	if (a[x][i] && !u[x][i]) rec(x,i);
	for(int i=0;i<n;i++)
	if (a[y][i] && !u[y][i]) rec(y,i);
}

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout);
    cout.flags(ios::fixed);
    cout.precision(10);
    int T;
    cin>>T;
    for(int TT=0;TT<T;TT++)
    {
		cin>>n>>k;
		clr(a);
		clr(t);
		st=0;
		for(int i=0;i<n-1;i++)
		{
			scanf("%d%d",&x,&y);
			x--;
			y--;
			a[x][y]=1;
			a[y][x]=1;
		}
		clr(U);
		clr(u);
		ans=1;
		for(int i=1;i<n;i++)
		{
			if (a[i][0])
			{
				rec(0,i);
				break;
			}
		}
//		rec(0);
		cout<<"Case #"<<TT+1<<": ";
		cout<<ans;
		cout<<endl;
	}
    return 0;
}
