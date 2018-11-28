#include <cstdio>
#include <iostream>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <cctype>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef vector<int> VI;

#define rep(i,n) for(int i=0;i<n;i++)
#define forr(i,a,b) for(int i=a;i<=b;i++)
#define ford(i,a,b) for(int i=a;i>=b;i--)
#define sz(a) ((int)(a).size())
#define ALL(a) (a).begin(),(a).end()

const int maxn=40;
const double eps=1e-6;

int t,test,n;
int x[maxn],y[maxn],r[maxn];
bool used[maxn];
double ll,rr,R,X1,Y1,d1,csa1,sna1,X2,Y2,d2,csa2,sna2,ans;
bool flag;
int cnt;

inline double dist(double x1,double y1,double x2,double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	scanf("%d",&test);
	forr(t,1,test)
	{
		scanf("%d",&n);
		rep(i,n)
			scanf("%d%d%d",&x[i],&y[i],&r[i]);
		ans=1e20;
		if(n==1)
		{
			ans=r[0];
		}else
		if(n==2)
		{
			ans=max(r[0],r[1]);
		}else
		if(n==3)
		{
			ans=min(ans,max((double)2*r[2],r[0]+r[1]+sqrt((double)(x[0]-x[1])*(x[0]-x[1])+(y[0]-y[1])*(y[0]-y[1])))/2);
			ans=min(ans,max((double)2*r[1],r[0]+r[2]+sqrt((double)(x[0]-x[2])*(x[0]-x[2])+(y[0]-y[2])*(y[0]-y[2])))/2);
			ans=min(ans,max((double)2*r[0],r[2]+r[1]+sqrt((double)(x[2]-x[1])*(x[2]-x[1])+(y[2]-y[1])*(y[2]-y[1])))/2);
		}else
		{
			ll=3000;
			rr=0;
			while(ll-rr>eps)
			{
				R=(ll+rr)/2;
				flag=0;
				rep(i,n) if(!flag)
					forr(j,i+1,n-1) if(!flag)
					{
						d1=dist(x[i],y[i],x[j],y[j]);
						csa1=((R-r[i])*(R-r[i])+d1*d1-(R-r[j])*(R-r[j]))/(2*(R-r[i])*d1);
						if(fabs(csa1-1)<eps)
							sna1=0;else
							sna1=sqrt(1-csa1*csa1);
						X1=x[i]+(R-r[i])/d1*((x[j]-x[i])*csa1-(y[j]-y[i])*sna1);
						Y1=y[i]+(R-r[i])/d1*((x[j]-x[i])*sna1+(y[j]-y[i])*csa1);
						memset(used,0,sizeof(used));	
						rep(k,n)	
							if(R+eps>=dist(x[k],y[k],X1,Y1)+r[k])
								used[k]=1;
						flag=1;
						cnt=0;
						rep(k,n)
							if(!used[k])
								cnt++;
						if(cnt==0)break;
						if(cnt==1)
						{
							int k=0;
							while(used[k]) k++;
							if(r[k]<=R+eps)break;
						}
						flag=0;
						rep(ii,n) if(!used[ii] && !flag)
							forr(jj,ii+1,n) if(!used[jj] && !flag)
							{
								d2=dist(x[ii],y[ii],x[jj],y[jj]);
								csa2=((R-r[ii])*(R-r[ii])+d2*d2-(R-r[jj])*(R-r[jj]))/(2*(R-r[ii])*d2);
								if(fabs(csa2-1)<eps)
									sna2=0;else
									sna2=sqrt(1-csa2*csa2);
								X2=x[ii]+(R-r[ii])/d2*((x[jj]-x[ii])*csa2-(y[jj]-y[ii])*sna2);
									Y2=y[ii]+(R-r[ii])/d2*((x[jj]-x[ii])*sna2+(y[jj]-y[ii])*csa2);
								flag=1;
								rep(k,n)	
									if(!(used[k] || R+eps>=dist(x[k],y[k],X2,Y2)+r[k]))
									{
										flag=0;
										break;
									}
								if(flag)break;
								d2=dist(x[ii],y[ii],x[jj],y[jj]);
								csa2=((R-r[ii])*(R-r[ii])+d2*d2-(R-r[jj])*(R-r[jj]))/(2*(R-r[ii])*d2);
								if(fabs(csa2-1)<eps)
									sna2=0;else
									sna2=sqrt(1-csa2*csa2);
								X2=x[ii]+(R-r[ii])/d2*((x[jj]-x[ii])*csa2+(y[jj]-y[ii])*sna2);
								Y2=y[ii]+(R-r[ii])/d2*(-(x[jj]-x[ii])*sna2+(y[jj]-y[ii])*csa2);
								flag=1;
								rep(k,n)	
									if(!(used[k] || R+eps>=dist(x[k],y[k],X2,Y2)+r[k]))
									{
										flag=0;
										break;
									}
								if(flag)break;
							}
						if(flag)break;
						d1=dist(x[i],y[i],x[j],y[j]);
						csa1=((R-r[i])*(R-r[i])+d1*d1-(R-r[j])*(R-r[j]))/(2*(R-r[i])*d1);
						if(fabs(csa1-1)<eps)
							sna1=0;else
							sna1=sqrt(1-csa1*csa1);
						X1=x[i]+(R-r[i])/d1*((x[j]-x[i])*csa1+(y[j]-y[i])*sna1);
						Y1=y[i]+(R-r[i])/d1*(-(x[j]-x[i])*sna1+(y[j]-y[i])*csa1);
						memset(used,0,sizeof(used));	
						rep(k,n)	
							if(R+eps>=dist(x[k],y[k],X1,Y1)+r[k])
								used[k]=1;
						flag=1;
						cnt=0;
						rep(k,n)
							if(!used[k])
								cnt++;
						if(cnt==0)break;
						if(cnt==1)
						{
							int k=0;
							while(used[k]) k++;
							if(r[k]<=R+eps)break;
						}
						flag=0;
						rep(ii,n) if(!used[ii] && !flag)
							forr(jj,ii+1,n) if(!used[jj] && !flag)
							{
								d2=dist(x[ii],y[ii],x[jj],y[jj]);
								csa2=((R-r[ii])*(R-r[ii])+d2*d2-(R-r[jj])*(R-r[jj]))/(2*(R-r[ii])*d2);
								if(fabs(csa2-1)<eps)
									sna2=0;else
									sna2=sqrt(1-csa2*csa2);
								X2=x[ii]+(R-r[ii])/d2*((x[jj]-x[ii])*csa2-(y[jj]-y[ii])*sna2);
									Y2=y[ii]+(R-r[ii])/d2*((x[jj]-x[ii])*sna2+(y[jj]-y[ii])*csa2);
								flag=1;
								rep(k,n)	
									if(!(used[k] || R+eps>=dist(x[k],y[k],X2,Y2)+r[k]))
									{
										flag=0;
										break;
									}
								if(flag)break;
								d2=dist(x[ii],y[ii],x[jj],y[jj]);
								csa2=((R-r[ii])*(R-r[ii])+d2*d2-(R-r[jj])*(R-r[jj]))/(2*(R-r[ii])*d2);
								if(fabs(csa2-1)<eps)
									sna2=0;else
									sna2=sqrt(1-csa2*csa2);
								X2=x[ii]+(R-r[ii])/d2*((x[jj]-x[ii])*csa2+(y[jj]-y[ii])*sna2);
								Y2=y[ii]+(R-r[ii])/d2*(-(x[jj]-x[ii])*sna2+(y[jj]-y[ii])*csa2);
								flag=1;
								rep(k,n)	
									if(!(used[k] || R+eps>=dist(x[k],y[k],X2,Y2)+r[k]))
									{
										flag=0;
										break;
									}
								if(flag)break;
							}
						if(flag)break;
					}
				if(flag)
					ll=R;else
					rr=R;
			}
			ans=ll;
		}
		printf("Case #%d: %.9lf\n",t,ans);
	}
	return 0;
}
