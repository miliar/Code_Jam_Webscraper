#include <iostream>
#include <fstream>
using namespace std;
long fa[2000],x1[2000],x2[2000],y1[2000],y2[2000],i,numtest,test,Min[2000],Max_x[2000],Max_y[2000],j,k,ans,fx,fy,n;

bool contain(long u,long x,long y)
{
	if(x1[u]<=x && x<=x2[u] && y1[u]<=y && y<=y2[u]) return(true);
	if(y2[u]-y==-1 && x1[u]<=x && x<=x2[u])return(true);
	if(y1[u]-y==1 && x1[u]<=x && x<=x2[u])return(true);
	if(x1[u]-x==1 && y1[u]<=y && y<=y2[u])return(true);
	if(x2[u]-x==-1 && y1[u]<=y && y<=y2[u])return(true);
	if(x-x2[u]==1 && y-y1[u]==-1) return(true);
	if(x-x1[u]==-1 && y-y2[u]==1) return(true);
	
	return(false);
}

bool cross (long u, long v)
{
	if(x1[u]<=x1[v] && x2[v]<=x2[u] && y1[v]<=y1[u] && y2[u] <= y2[v]) return(true);
	if(x1[v]<=x1[u] && x2[u]<=x2[v] && y1[u]<=y1[v] && y2[v] <= y2[u]) return(true);
	return(false);
}

long find(long v)
{
	while(fa[v]!=fa[fa[v]]) fa[v]=fa[fa[v]];
	return(fa[v]);
}

int main()
{
	ifstream cin ("input.txt");
	ofstream cout ("output.txt");
	cin >> numtest;
	for(test=1;test<=numtest;test++)
	{
		
		cin >> n;
		for(i=1;i<=n;i++) fa[i]=i;
		for(i=1;i<=n;i++)
		{
			cin >> x1[i] >> y1[i];
			cin >> x2[i] >> y2[i];
			if(x1[i]>x2[i]){k=x1[i];x1[i]=x2[i];x2[i]=k;};
			if(y1[i]>y2[i]){k=y1[i];y1[i]=y2[i];y2[i]=k;};
			Min[i]=x1[i]+y1[i];
			Max_x[i]=x2[i];
			Max_y[i]=y2[i];	
		}
		
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++) if(find(i)!=find(j) &&(contain(i,x1[j],y1[j])||contain(i,x1[j],y2[j])||contain(i,x2[j],y1[j])||contain(i,x2[j],y2[j])||cross(i,j)))
			{
				fx=find(j);
				fy=find(i);
				fa[fx]=fy;
				if(Min[fx]<Min[fy]) Min[fy]=Min[fx];
				if(Max_x[fx]>Max_x[fy]) Max_x[fy]=Max_x[fx];
				if(Max_y[fx]>Max_y[fy]) Max_y[fy]=Max_y[fx];
			}
			
		ans=0;
		for(i=1;i<=n;i++) if(Max_x[i]+Max_y[i]-Min[i]+1>ans) ans=Max_x[i]+Max_y[i]-Min[i]+1;
		cout << "Case #" << test << ": " << ans << endl;
		//for(i=1;i<=n;i++) cout << fa[i] << ' ' << Min[i] << ' ' << Max_x[i] << ' ' << Max_y[i] << endl;
	}
	return 0;
}
