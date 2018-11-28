#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <cstring> 
#include <cstdlib> 
#include <cstdio> 
#include <vector> 
#include <string> 
#include <cmath> 
#include <queue> 
#include <map> 
#include <set> 

using namespace std; 

typedef vector<int> VI; 
typedef vector<string> VS; 
typedef long long ll; 

#define sz size() 
#define pb push_back 
#define MAX 0xFFFFFFF 
#define all(x) (x).begin(),(x).end() 
#define For(i,n) for(int i=0, _n=(n);i<_n;++i) 
#define For2(i,a,b) for(int i=(a), _n=(b);i<_n;++i) 
//#define Forit(it,x) for(typeof((x).begin()) it=(x).begin(), ed=(x).end();it!=ed;++it) 

int n, n1;
int a[200000][2];
int b[200000][2];

int cal(int x, int v)
{
	if(b[x][v] != -1) return b[x][v];
	if(x >= n1) if(a[x][0] == v) return b[x][v]=0; else return b[x][v]=MAX;
	if(v)
	{
		if(a[x][0])
		{
			int x1 = cal(x*2+1, 1);
			int x2 = cal(x*2+2, 1);
			if(a[x][1] == 0)
			{
				if(x1 == MAX || x2 == MAX) return b[x][v]=MAX;
				return b[x][v]=x1+x2;
			}
			int x3 = cal(x*2+1, 0);
			int x4 = cal(x*2+2, 0);
			int q = x1 + x2;
			q = min(q, x1+x4+1);
			q = min(q, x2+x3+1);
			if(q >= MAX) return b[x][v]=MAX;
			return b[x][v]=q;
		}
		else
		{
			int x1 = cal(x*2+1, 1);
			int x2 = cal(x*2+2, 1);
			int x3 = cal(x*2+1, 0);
			int x4 = cal(x*2+2, 0);
			int q = x1 + x2;
			q = min(q, x1+x4);
			q = min(q, x2+x3);
			if(q >= MAX) return b[x][v]=MAX;
			return b[x][v]=q;
		}
	}
	else
	{
		if(a[x][0])
		{
			int x1 = cal(x*2+1, 1);
			int x2 = cal(x*2+2, 1);
			int x3 = cal(x*2+1, 0);
			int x4 = cal(x*2+2, 0);
			int q = x3 + x4;
			q = min(q, x1+x4);
			q = min(q, x2+x3);
			if(q >= MAX) return b[x][v]=MAX;
			return b[x][v]=q;
		}
		else
		{
			int x1 = cal(x*2+1, 1);
			int x2 = cal(x*2+2, 1);
			int x3 = cal(x*2+1, 0);
			int x4 = cal(x*2+2, 0);
			if(a[x][1] == 0)
			{
				if(x3 == MAX || x4 == MAX) return b[x][v]=MAX;
				return b[x][v]=x3+x4;
			}
			int q = x3 + x4;
			q = min(q, x1+x4+1);
			q = min(q, x2+x3+1);
			if(q >= MAX) return b[x][v]=MAX;
			return b[x][v]=q;
		}
	}
}

int main()
{
	FILE *in = fopen("A-large.in","r");
	FILE *out = fopen("output.txt","w");
	//in = stdin;
	//out = stdout;
	int ti = 0;
	int tn;
	fscanf(in,"%d",&tn);
	while(tn--)
	{
		int v;
		memset(b, -1, sizeof(b));
		fscanf(in,"%d %d",&n,&v);
		n1 = (n-1)/2;
		int n2 = (n+1)/2;
		int t = 0;
		For(i,n1) {fscanf(in,"%d %d",&a[t][0],&a[t][1]); t++;}
		For(i,n2) fscanf(in,"%d",&a[t++][0]);
		int ans = cal(0, v);
		int w = MAX;
		if(ans >= MAX) fprintf(out,"Case #%d: IMPOSSIBLE\n",++ti);
		else fprintf(out,"Case #%d: %d\n",++ti,ans);
	}
}

/*
2
9 1
1 0
1 1
1 1
0 0
1
0
1
0
1
5 0
1 1
0 0
1
1
0

*/