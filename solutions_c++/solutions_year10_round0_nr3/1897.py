#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int t,n,k,r,g[2040],d[2040],b[2040];
long long ans;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int q=1; q<=t; q++)
	{
		int i,acc=0;
		ans=0;
		scanf("%d %d %d",&r, &k, &n);
		for (i=0; i<n; i++) scanf("%d",&g[i]);
		int j=1; acc=g[0]; 
		if (acc<=k)
		{
		for (i=0; i<n; i++) 
		{
			if (i==j) acc=g[j++]; if (!(j<n)) j=0;
			while ((acc+g[j] <= k) && (j!=i)) { acc+=g[j++]; if (!(j<n)) j=0;}
			d[i]=acc; b[i]=j; 
			acc-=g[i];
		}
		j=i=0;
		while (j<r)
		if (d[i]<=k)
		{ 
			ans+=d[i]; 
			j++;i=b[i];
		}
		cout << "Case #" << q << ": " << ans <<endl;
		}else printf("Case #%d:0\n",&q);
	}
	return 0;
}