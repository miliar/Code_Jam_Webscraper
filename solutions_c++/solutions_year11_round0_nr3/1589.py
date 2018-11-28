#include<iostream>
using namespace std;
int i,j,k,l,m,n,xys,ysc,ans,minn,tot;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&ysc);
	for (xys=1;xys<=ysc;++xys){
        ans=tot=0;minn=20000000;
		scanf("%d",&n);
		for (i=1;i<=n;++i){
			scanf("%d",&k);
			ans^=k;tot+=k;
			if (k<minn) minn=k;
		}
		if (ans!=0)
			printf("Case #%d: NO\n",xys);
        else printf("Case #%d: %d\n",xys,tot-minn);
	}
	return 0;
}
