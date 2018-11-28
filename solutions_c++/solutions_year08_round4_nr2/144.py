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
#define MAX 0x3FFFFFFF 
#define all(x) (x).begin(),(x).end() 
#define For(i,n) for(int i=0, _n=(n);i<_n;++i) 
#define For2(i,a,b) for(int i=(a), _n=(b);i<_n;++i) 
//#define Forit(it,x) for(typeof((x).begin()) it=(x).begin(), ed=(x).end();it!=ed;++it) 


int main()
{
	FILE *in = fopen("B-large.in","r");
	FILE *out = fopen("output.txt","w");

	//in = stdin;
	//out = stdout;
	int ti = 0;
	int tn;
	fscanf(in,"%d",&tn);
	while(tn--)
	{
		int n, m, A;
		int x1,y1,x2,y2,x3,y3;
		int po = 0;
		fscanf(in,"%d %d %d",&n,&m,&A);
		x1=y1=0;
		x2 = 0;
		y3 = 0;
		For2(j,1,m+1)
		{
			y2 = j;
			if(A % y2 == 0) 
			{
				x3 = A / y2;
				if(x3 > n) continue;
				fprintf(out,"Case #%d: %d %d %d %d %d %d\n",++ti,x1,y1,x2,y2,x3,y3);
				goto nn;
			}
		}
		x2 = 1;
		x3 = n;
		For(j,m+1)
		{
			y2 = j; 
			y3 = A + x3*y2;
			if(y3 < m) 
			{
				fprintf(out,"Case #%d: %d %d %d %d %d %d\n",++ti,x1,y1,x2,y2,x3,y3);
				goto nn;
			}
			y3 = x3*y2 - A;
			if(y3 < m && y3 >= 0) 
			{
				fprintf(out,"Case #%d: %d %d %d %d %d %d\n",++ti,x1,y1,x2,y2,x3,y3);
				goto nn;
			}
		}
		x2 = 1;
		x3 = n-1;
		For(j,m+1)
		{
			y2 = j; 
			y3 = A + x3*y2;
			if(y3 < m) 
			{
				fprintf(out,"Case #%d: %d %d %d %d %d %d\n",++ti,x1,y1,x2,y2,x3,y3);
				goto nn;
			}
			y3 = x3*y2 - A;
			if(y3 < m && y3 >= 0) 
			{
				fprintf(out,"Case #%d: %d %d %d %d %d %d\n",++ti,x1,y1,x2,y2,x3,y3);
				goto nn;
			}
		}


		x2 = 1;
		y2 = m;
		For(j,n+1)
		{
			x3 = j; 
			y3 = A + x3*y2;
			if(y3 < m) 
			{
				fprintf(out,"Case #%d: %d %d %d %d %d %d\n",++ti,x1,y1,x2,y2,x3,y3);
				goto nn;
			}
			y3 = x3*y2 - A;
			if(y3 < m && y3 >= 0) 
			{
				fprintf(out,"Case #%d: %d %d %d %d %d %d\n",++ti,x1,y1,x2,y2,x3,y3);
				goto nn;
			}
		}
		x2 = 1;
		x2 = m-1;
		For(j,n+1)
		{
			x3 = j;
			y3 = A + x3*y2;
			if(y3 < m) 
			{
				fprintf(out,"Case #%d: %d %d %d %d %d %d\n",++ti,x1,y1,x2,y2,x3,y3);
				goto nn;
			}
			y3 = x3*y2 - A;
			if(y3 < m && y3 >= 0) 
			{
				fprintf(out,"Case #%d: %d %d %d %d %d %d\n",++ti,x1,y1,x2,y2,x3,y3);
				goto nn;
			}
		}
		fprintf(out,"Case #%d: IMPOSSIBLE\n",++ti);
nn:;
	}
}

/*
3
1 1 1
1 2 64
10 10 1
*/
