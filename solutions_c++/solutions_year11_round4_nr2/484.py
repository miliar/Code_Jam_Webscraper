// AAA
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<iomanip>
#include<cmath>
using namespace std;
const int MAX=550;
const double eps=1e-6;

double D;
int R,C;
double g[MAX][MAX];

void out(double g[][MAX])
{
	for(int i=1;i<=R;i++)
	{
		for(int j=1;j<=C;j++) cout<<g[i][j]<<" ";cout<<endl;
	}
}

double mass[MAX][MAX];
void getMass()
{
	for(int i=0;i<=R;i++) for(int j=0;j<=C;j++) mass[i][j]=0.0;
	
	for(int i=1;i<=R;i++)
	{
		for(int j=1;j<=C;j++)
		{
			mass[i][j]=mass[i][j-1]+mass[i-1][j]-mass[i-1][j-1]+g[i][j];
		}
	}
}

double X[MAX][MAX];
void getX()
{
	for(int i=0;i<=R;i++) for(int j=0;j<=C;j++) X[i][j]=0.0;
	
	for(int i=1;i<=R;i++)
	{
		for(int j=1;j<=C;j++)
		{
			double pos=-0.5+(double)i;
			X[i][j]=X[i][j-1]+X[i-1][j]-X[i-1][j-1]+g[i][j]*pos;
		}
	}
}
double Y[MAX][MAX];
void getY()
{
	for(int i=0;i<=R;i++) for(int j=0;j<=C;j++) Y[i][j]=0.0;
	
	for(int i=1;i<=R;i++)
	{
		for(int j=1;j<=C;j++)
		{
			double pos=-0.5+(double)j;
			Y[i][j]=Y[i][j-1]+Y[i-1][j]-Y[i-1][j-1]+g[i][j]*pos;
		}
	}
}
double gs(int i,int j,int tx,int ty,double mm)
{
	double ans=0;
	ans+=((double)i-0.5-mm)*g[i][j];
	ans+=((double)i-0.5-mm)*g[i][ty];
	ans+=((double)tx-0.5-mm)*g[tx][j];
	ans+=((double)tx-0.5-mm)*g[tx][ty];
	return ans;
}
double joy(int i,int j,int tx,int ty,double mm)
{
	double ans=0;
	ans+=((double)j-0.5-mm)*g[i][j];
	ans+=((double)ty-0.5-mm)*g[i][ty];
	ans+=((double)j-0.5-mm)*g[tx][j];
	ans+=((double)ty-0.5-mm)*g[tx][ty];
	return ans;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;scanf("%d",&T);
	int CN=0;
	
	while(T--)
	{
		scanf("%d%d%lf",&R,&C,&D);
		
		for(int i=1;i<=R;i++)
		{
			string s;cin>>s;
			for(int j=0;j<s.size();j++) g[i][j+1]=D+(s[j]-'0');
		}
		
		//out(g);
		
		getMass();
		
		getX();
		getY();
		
		int ans=-1;
		for(int i=1;i+2<=R;i++)
		{
			for(int j=1;j+2<=C;j++)
			{
				for(int r=max(ans,3);i+r-1<=R&&j+r-1<=C;r++)
				{
					double xx=(double)i-1.0+(double)r/2;
					double yy=(double)j-1.0+(double)r/2;
					
					int tx=i+r-1,ty=j+r-1;
					double mam=mass[tx][ty]-mass[i-1][ty]-mass[tx][j-1]+mass[i-1][j-1];
					double ax=X[tx][ty]-X[i-1][ty]-X[tx][j-1]+X[i-1][j-1]-xx*mam;
					double ay=Y[tx][ty]-Y[i-1][ty]-Y[tx][j-1]+Y[i-1][j-1]-yy*mam;
					
					ax-=gs(i,j,tx,ty,xx);
					ay-=joy(i,j,tx,ty,yy);
					if(fabs(ax)<eps&&fabs(ay)<eps) ans=max(ans,r);
				}
			}
		}
		
		printf("Case #%d: ",++CN);
		if(ans==-1) puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
    
    return 0;
}
