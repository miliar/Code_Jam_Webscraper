#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
const int MAXN=1009;
int c[MAXN],T,n,m,s,xs;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("c_l.out","w",stdout);
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		scanf("%d",&n);		m=2147483647;	xs=s=0;
		for (int i=1;i<=n;i++) 
		{			
			scanf("%d",&c[i]);	m=min(m,c[i]);	xs^=c[i];	s+=c[i];
		}
		printf("Case #%d: ",t);
		if (xs) printf("NO\n");	else printf("%d\n",s-m);
	}
	return 0;
}




