#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
int tmp,c,i,j,k,l,m,n,h,hh,ans,fact[]={1,2,6,24,120},perm[5];
char st[1005],st2[1005];
int main()
{
	freopen("d-small.in","r",stdin);
	freopen("d-small.out","w",stdout);
	scanf("%d\n",&hh);
	for(h=1;h<=hh;h++)
	{
		scanf("%d\n",&k);
		scanf("%s\n",st);
		n=strlen(st);
		ans=1000000;
		for(c=0;c<5;c++) {perm[c]=c+1;}
		for(j=0;j<fact[k-1];j++)
		{			
		 for(i=0;i<n/k;i++)
			{
				for(c=0;c<5;c++)
				{
					st2[i*k+c]=st[i*k+perm[c]-1];
				}
			}
			tmp=1;
			for(i=0;i<n-1;i++)
			{
				if (st2[i]!=st2[i+1]) {tmp++;}
			}
			if (tmp<ans) {ans=tmp;}
			next_permutation(perm,perm+k);
		}
		printf("Case #%d: %d\n",h,ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}