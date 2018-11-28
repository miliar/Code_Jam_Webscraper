#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
#include <cmath>
#include <map>
#include <set>
#include <cstring>
#include <sstream>
#include <cctype>

#define FIN for(i=0;i<N;i++)
#define FIM for(i=0;i<M;i++)
#define FJN for(j=0;j<N;j++)
#define FJM for(j=0;j<M;j++)
#define FOR(i,N) for(i=0;i<N;i++)
#define FAB(i,A,B) for(i=A;i<=B;i++)
using namespace std;

int N;
int X[555],Y[555],R[555];
vector< pair<__int64,double>> V;
const double eps=1e-5;

double dist(double x1,double y1,double x2,double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}
void build(double xx,double yy,double r)
{
	__int64 one=1;

	int i;
	__int64 mask=0;
	FIN if( r>double(R[i])-eps &&
		(double(X[i])-xx)*(double(X[i])-xx)+(double(Y[i])-yy)*(double(Y[i])-yy)<(r-double(R[i]))*(r-double(R[i]))+eps)
		mask|=(one<<i);

	V.push_back(make_pair(mask,r));
}

double XX[3],YY[3],RR[3],RF[3];
void build_on(int i, int j,int k)
{
	XX[0]=X[i];
	YY[0]=Y[i];
	RR[0]=R[i];
	XX[1]=X[j];
	YY[1]=Y[j];
	RR[1]=R[j];
	XX[2]=X[k];
	YY[2]=Y[k];
	RR[2]=R[k];

	double xx=(XX[0]+XX[1]+XX[2])/3.0,yy=(YY[0]+YY[1]+YY[2])/3.0,r;

	FOR(i,3) RF[i]=(xx-XX[i])*(xx-XX[i])+(yy-YY[i])*(yy-YY[i])+RR[i]*RR[i];

	int mj;
	double dx,dy;
	double a,b,m;
	FOR(k,1000)
	{
		mj=0;
		FOR(j,3) if(RF[j]>RF[mj]) mj=j;
		dx=XX[mj]-xx;
		dy=YY[mj]-yy;

		a=0;
		b=0.7;
	}

}
void test()
{
	int i,j,k;

	scanf("%d",&N);

	FIN scanf("%d%d%d",&X[i],&Y[i],&R[i]);

	
	double ans=0,cur;

	if(N==1) ans=R[0];

	else if(N==2) ans=max(R[1],R[0]);
	else if(N==3)
	{
		ans=1e10;

		FOR(i,3)
		{
			cur=dist(X[(i+1)%3],Y[(i+1)%3],X[(i+2)%3],Y[(i+2)%3])+double(R[(i+1)%3])+double(R[(i+2)%3]);
			cur/=2.0;
			cur=max(cur,double(R[i]));
			if(cur<ans) ans=cur;
		}
	}

	printf("%.10lf\n",ans);
		
}
int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);

	int t=0,T;

	scanf("%d",&T);

	for(t=0;t<T;t++)
	{
		printf("Case #%d: ",t+1);
		test();
	}
}