////#include<iostream>
////#include<cstring>
////#include<queue>
////using namespace std;
////
////int d[10005],l[10005],a[10005],vis[10005];
////queue<int> q;
////
////int Min(int x,int y) { return x<y?x:y;} 
////
////int main()
////{
////	freopen("a.txt","r",stdin);
////	freopen("ans.txt","w",stdout);
////	int T,tc,D,n,i,x,y,f;
////	cin>>T;
////	for(tc=1;tc<=T;tc++)
////	{
////		cin>>n;
////		memset(vis,0,sizeof(vis));
////		for(i=0;i<n;i++)
////			cin>>d[i]>>l[i];
////		cin>>D;
////		d[n]=D; l[n]=1;
////		while(!q.empty())
////			q.pop();
////		if(d[0]>l[0])
////		{
////			cout<<"Case #"<<tc<<": NO"<<endl;
////			continue;
////		}
////		q.push(0);
////		q.push(d[0]);
////		a[0]=d[0];
////		f=0;
////		while(!q.empty())
////		{
////			x=q.front(); q.pop();
////			y=q.front(); q.pop();
////			if(x==n)
////			{
////				f=1;
////				break;
////			}
////			if(a[x]!=y) continue;
////			for(i=x+1;i<=n&&d[i]-d[x]<=y;i++)
////			{
////				if(vis[i]&&Min(l[i],d[i]-d[x])<=a[i]) continue;
////				vis[i]=1; a[i]=Min(l[i],d[i]-d[x]);
////				q.push(i);
////				q.push(a[i]);
////			}
////		}
////		if(f)
////			cout<<"Case #"<<tc<<": YES"<<endl;
////		else
////			cout<<"Case #"<<tc<<": NO"<<endl;
////	}
////	return 0;
////}
////
////
////
//
//
//#include<stdio.h>
//#include<string.h>
//
//int ans[2100],a[2100];
//int bs(int i,int t,int j)
//{
//	long long ai=a[i],l=0,r=1000000000,mid,aj=a[j];
//
//	while(l<r-1)
//	{
//		mid=(l+r)>>1;
//
//		if((mid-ai)*(j-i)>=(aj-ai)*(t-i))
//			r=mid;
//		else
//			l=mid;
//	}
//	if(r>0&&((r-1)-ai)*(j-i)>=(aj-ai)*(t-i))
//		r--;
//	return r;
//}
//int ff(int n)
//{
//	int i,j;
//	for(i=1;i<n;i++)if(a[i]<=i)
//		return 0;
//	for(i=1,j=0;i<n;i++)
//	{
//		if(j>i&&a[i]>j)
//			return 0;
//		j=a[i]>j?a[i]:j;
//	}
//	memset(ans,-1,sizeof(ans));
//	i=1;a[n]=0;
//	while(i)
//		ans[i]=1000000000,i=a[i];
//	for(i=2;i<=n;i++)if(ans[i]<0)
//	{
//		ans[i]=0;
//		for(j=i+1;ans[j]<0;j++);
//
//		while(ans[a[i]]<0)
//		{
//			int t=a[i];
//			ans[t]=bs(i,t,j);
//			if(ans[t]==ans[j])
//				return 0;
//			i=a[i];
//		}
//	}
//	return 1;
//}
//
//int main()
//{	
//	freopen("a.txt","r",stdin);
//	freopen("ans.txt","w",stdout);
//	int t,i,j,n,ii=0;
//	scanf("%d",&t);
//	while(t--)
//	{
//		scanf("%d",&n);
//		for(i=1;i<n;i++)
//			scanf("%d",&a[i]);
//			printf("Case #%d:",++ii);
//		if(ff(n))
//		{
//			for(i=1;i<=n;i++)
//				printf(" %d",ans[i]);
//			printf("\n");
//		}
//		else
//			printf(" Impossible\n");
//	}
//}


#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#define INF 99999999
using namespace std;

int n,w,l,r[1005],h[1005];
bool ok;
double x[1005],y[1005],s[1005];
double make(int x,int y)
{
      int t=rand()%1000000+1;
      int s=rand()%t+1;
      return (y-x)*(s*1.0/t)+x;
}
double dis(double x,double y,double a,double b)
{
      return sqrt( (x-a)*(x-a)+(y-b)*(y-b) );
}
void dfs(int m)
{
     double xx,yy;
     int i,j;
     bool f=false;
     s[h[m]]=INF;
     if (m>n)
      {
         for (i=1;i<=n;i++) 
         {
               printf(" %.2lf %.2lf",x[i],y[i]);
          }
   puts("");
               ok=true;
              return ;
       }
     for (i=1;i<=100;i++)
     {
        double ss=INF,t;
        xx=make(0,w);
        yy=make(0,l);
        for (j=1;j<m;j++)
            if ((t=dis(x[h[j]],y[h[j]],xx,yy))<r[h[j]]+r[h[m]])
            {
              if (ss>t) ss=t;
              break;
             }
        if (j==m)
        {
            if (s[h[m]]==INF || s[h[m]]>ss)
               x[h[m]]=xx,y[h[m]]=yy,s[h[m]]=ss;
            f=true;
         }
     }
     if (!f) return;
     dfs(m+1);
     if (ok==false) dfs(m);
}
int cmp(int x,int y)
{
    return r[x]>r[y];
}

int main()
{
    int T,cas=0,i;
    freopen("a.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    scanf("%d",&T);
    for(cas=1;cas<=T;cas++)
    {
        scanf("%d%d%d",&n,&w,&l);
        for (i=1;i<=n;i++) scanf("%d",&r[i]),h[i]=i;
        sort(h+1,h+n+1,cmp);
        printf("Case #%d:",cas);
        ok=false;
        dfs(1);
        for (int i=1;i<=n;i++)     
           for (int j=i+1;j<=n;j++)   
			   if (dis(x[i],y[i],x[j],y[j])<r[i]+r[j]) puts("!!!!!!!!!!!");
    }
}
