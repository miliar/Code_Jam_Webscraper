#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

char sheet[555][555];
double xmass[555][555];
double ymass[555][555];
double mass[555][555];
const double eps=1e-8;
bool zero(double a)
{
	if(a>-eps&&a<eps) return 1;
	return 0;
}
int mmin(int a,int b)
{
	return a<b?a:b;
}
int main()
{
	int cas,cc=1,n,m,i,j,k,l;
	double d;
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>cas;
	while(cas--)
	{
		scanf("%d%d%lf",&n,&m,&d);
		for(i=0;i<n;i++) scanf("%s",&sheet[i]);
		memset(xmass,0,sizeof(xmass));
		memset(ymass,0,sizeof(ymass));
		memset(mass,0,sizeof(mass));
		double tmp=0;
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				tmp=sheet[i-1][j-1]-'0'+d;
				mass[i][j]=mass[i][j-1]+tmp;
				xmass[i][j]=xmass[i][j-1]+(j+0.5)*tmp;
				ymass[i][j]=ymass[i][j-1]+(i+0.5)*tmp;
			}
		}
		for(j=1;j<=m;j++)
			for(i=1;i<=n;i++)
			{
				mass[i][j]+=mass[i-1][j];
				xmass[i][j]+=xmass[i-1][j];
				ymass[i][j]+=ymass[i-1][j];
			}
		int ans=0;
		double x=0,y=0,z=0,xm=0,ym=0,mm=0;
		double d1,d2,d3,d4;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
			{
				k=mmin(n-i+1,m-j+1);
				for(;k>2;k--)
				{
					x=(k*1.0)/2+j*1.0;
					y=(k*1.0)/2+i*1.0;
					d1=sheet[i-1][j-1]-'0'+d;
					d2=sheet[i-1][j+k-2]-'0'+d;
					d3=sheet[i+k-2][j-1]-'0'+d;
					d4=sheet[i+k-2][j+k-2]-'0'+d;
					xm=xmass[i+k-1][j+k-1]-xmass[i-1][j+k-1]-xmass[i+k-1][j-1]+xmass[i-1][j-1];
					xm-=(j+0.5)*(d1+d3)+(j+k-1+0.5)*(d2+d4);
					ym=ymass[i+k-1][j+k-1]-ymass[i-1][j+k-1]-ymass[i+k-1][j-1]+ymass[i-1][j-1];
					ym-=(i+0.5)*(d1+d2)+(i+k-1+0.5)*(d3+d4);
					mm=mass[i+k-1][j+k-1]-mass[i-1][j+k-1]-mass[i+k-1][j-1]+mass[i-1][j-1];
					mm-=d1+d2+d3+d4;
					//if(k==5) cout<<xm<<" "<<mm*x<<" "<<ym<<" "<<mm*y<<endl;
					if(zero(xm-mm*x)&&zero(ym-mm*y))
					{
						if(k>ans) ans=k;
						break;
					}
				}
			}
		if(ans==0) printf("Case #%d: IMPOSSIBLE\n",cc++);
		else printf("Case #%d: %d\n",cc++,ans);
	}
}