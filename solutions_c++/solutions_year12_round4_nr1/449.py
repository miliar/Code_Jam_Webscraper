#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

#define oo 500005
#define inf 2147483647

int s[oo],f[oo],d[oo],L[oo];
int Test,n,p;

int fen2(int x)
{
	int l=1,r=n+1,ans=0;
	for (;l<=r;){
		int mid=(l+r)/2;
		if (d[mid]<=x){
			ans=mid;
			l=mid+1;
		}else r=mid-1;
	}
	return ans;
}

void build(int i,int l,int r)
{
	s[i]=inf;
	if (l==r) return;
	int mid=(l+r)/2;
	build(i+i,l,mid);
	build(i+i+1,mid+1,r);
}

void cover(int i,int l,int r,int x,int y,int z)
{
	if (l==x && r==y){
		s[i]=z;
		return;
	}
	int mid=(l+r)>>1;
	if (y<=mid) cover(i+i,l,mid,x,y,z);
	else if (x>mid) cover(i+i+1,mid+1,r,x,y,z);
	else{
		cover(i+i,l,mid,x,mid,z);
		cover(i+i+1,mid+1,r,mid+1,y,z);
	}
}

int ask(int i,int l,int r,int x)
{
	if (l==x && r==x) return s[i];
	int mid=(l+r)>>1;
	
	if (x<=mid) return min(s[i],ask(i+i,l,mid,x));
	else return min(s[i],ask(i+i+1,mid+1,r,x));
}

int main()
{
	freopen("input.txt","r",stdin);
	
	scanf("%d",&Test);
	for (int t=1;t<=Test;++t){
		printf("Case #%d: ",t);
		scanf("%d",&n);
		for (int i=1;i<=n;++i) scanf("%d%d",&d[i],&L[i]);
		scanf("%d",&d[n+1]);
		L[n+1]=0;
		
		for (int i=1;i<=n+1;++i) f[i]=-1;
//		for (int i=1;i<=n;++i)
//		if (d[i]<=L[i]) f[i]=d[i];
		if (d[1]<=L[1]) f[1]=d[1];
		
		f[1]=d[1];
		for(int i=2;i<=n+1;++i)
		{
			f[i]=-1;
			for(int j=i-1;j>=1;--j)
			if(f[j]>=d[i]-d[j])
				f[i]=max(f[i],min(d[i]-d[j],L[i]));
		}	
		
		printf("%s\n",(f[n+1]>=0) ? "YES":"NO");
	}
	return 0;
	
}
