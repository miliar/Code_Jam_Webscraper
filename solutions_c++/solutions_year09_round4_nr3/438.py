#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <iomanip>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

#define inf 1000000000
//typedef long long LL;
//typedef __int64 LL;

int p[105][30],mat[105][105],memo[1<<16],n,target,valid[1<<16];

struct pt{
	pt() {x=y=0;}
	pt(double xx,double yy) {x=xx;y=yy;}
	double x,y;
};

struct line{
	line() {a=b=c=0;}
	line(pt P,pt Q){a=P.y- Q.y;b=Q.x-P.x;c =P.y* (P.x-Q.x) - P.x *(P.y-Q.y);}
	double a,b,c;
};

double eps=1e-5;

int insegment(pt C,pt A,pt B)
{
	if(C.x<MIN(A.x,B.x) || C.y<MIN(A.y,B.y) || C.x>MAX(A.x,B.x) || 
	   C.y>MAX(A.y,B.y) ) return 0;
	return 1;
}

pt sect(line A,line B)
{
	pt ret(inf,inf);
	if((A.a*B.b-B.a*A.b)==0) return ret;
	ret.x=(A.b*B.c-B.b*A.c)/(A.a*B.b-B.a*A.b);
	ret.y=(A.c*B.a-B.c*A.a)/(A.a*B.b-B.a*A.b);
	return ret;
}

int solve(int mask)
{
	int i,j,k,ret=inf;

	if(mask==target) return 0;
	if(memo[mask]!=-1) return memo[mask];

	for (i=target; (i &= ~mask) > 0; i--)
	{
		if(!valid[i]) continue;

		int q=solve(mask|i);
		ret=MIN(ret,1+q);
	}

	return memo[mask]=ret;
}
int main()
{
	int i,j,k,l,tests,cs=0;
	
//	freopen("C:\\Csmall.in","r",stdin);
	freopen("Csmall7.out","w",stdout);

	scanf("%d",&tests);
	while(tests--)
	{
		scanf("%d%d",&n,&k);

		target=(1<<n)-1;


		for(i=0;i<n;i++)
			for(j=0;j<k;j++)
			{
				scanf("%d",&p[i][j]);
			}

		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				int ok=0;

				for(l=0;l<k;l++)
				{
					if(p[i][l]==p[j][l] ) ok=1;

					if(l==k-1) break;

					pt A(l,p[i][l]),B(l+1,p[i][l+1]);
					pt C(l,p[j][l]),D(l+1,p[j][l+1]);

					line AB(A,B);
					line CD(C,D);

					pt o=sect(AB,CD);

					if(o.x==inf || !insegment(o,A,B) || !insegment(o,C,D)) continue;
					ok=1;
					break;
				}

				//if(ok)
				//	printf("%d %d\n",i,j);

				mat[i][j]=mat[j][i]=ok;
			}
		}

		MEM(memo,-1);
		MEM(valid,0);

		for(i=0;i<=target;i++)
		{
			int ok=1;

			for(j=0;j<n && ok;j++) if(i&(1<<j))
				for(l=j+1;l<n && ok;l++) if(i&(1<<l))
				{
					if(mat[j][l]) ok=0;
				}
		
			//if(ok)
				//printf("%d\n",i);

			valid[i]=ok;
		}

		int ans=solve(0);

		printf("Case #%d: %d\n",++cs,ans);

	}


	return 0;
} 


