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

string c[100],C[100];
int f[100],l[100],z[10100][100],u[100],x[100],n,ans,k;

void tst(int r)
{
	for(int i=1;i<=10000;i++)
	{
		int w=0;
		for(int j=0;j<11;j++)
		w+=z[i][j];
		if (w==0) return;
		if (w>3) return;
	}
	int w=0;
	for(int i=0;i<11;i++)
	w+=u[i];
	if (w>3) return;
	ans<?=r;
}

void rec(int q,int r)
{
	if (q==n) {tst(r); return;}
	if (u[x[q]])
	{
		for(int i=f[q];i<=l[q];i++)
		z[i][x[q]]++;
		rec(q+1,r+1);
		for(int i=f[q];i<=l[q];i++)
		z[i][x[q]]--;
		rec(q+1,r);
	} else
	{
		u[x[q]]++;
		for(int i=f[q];i<=l[q];i++)
		z[i][x[q]]++;
		rec(q+1,r+1);
		u[x[q]]--;
		for(int i=f[q];i<=l[q];i++)
		z[i][x[q]]--;
		rec(q+1,r);
	}
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
		cin>>n;
		k=0;
		clr(z);
		clr(f);
		clr(l);
		for(int i=0;i<100;i++)
		{
			c[i]="";
			C[i]="";
		}
		ans=10000;
		for(int i=0;i<n;i++)
		{
			cin>>c[i]>>f[i]>>l[i];
			bool can=true;
			for(int j=0;j<k;j++)
			if (c[i]==C[j]) {can=false; x[i]=j; break;}
			if (can) {x[i]=k; C[k]=c[i]; k++;}
		}
		clr(u);
		rec(0,0);
		cout<<"Case #"<<TT+1<<": ";
		if (ans==10000) cout<<"IMPOSSIBLE"; else
		cout<<ans;
		cout<<endl;
	}
    return 0;
}
