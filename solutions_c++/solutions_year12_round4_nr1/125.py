#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<iostream>
#include<cmath>
using namespace std;
const int V=100100;
const int oo=2000000000;
int p[V],d[V],_,n,D,ca,i,j,te,pr[V];
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&_);
	for(ca=1;ca<=_;ca++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		scanf("%d%d",&p[i],&d[i]);
		for(i=0;i<n;i++)pr[i]=oo;
		pr[0]=0;
		scanf("%d",&D);
		for(i=0;i<n;i++)
		{
			if(pr[i]==oo)continue;
			te=p[i]+min(p[i]-pr[i],d[i]);
			for(j=i+1;j<n;j++)
			{
				if(pr[j]!=oo)continue;
				if(te<p[j])break;
				pr[j]=p[i];
			}
		}
		bool has=false;
		for(i=0;i<n;i++)
		if(pr[i]!=oo&&p[i]+min(p[i]-pr[i],d[i])>=D)has=true;
		printf("Case #%d: ",ca);
		if(has)puts("YES");
		else puts("NO");
	}
}
