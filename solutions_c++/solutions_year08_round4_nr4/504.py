#include "stdio.h"
#include <algorithm>
using namespace std;
char x[50005],mid[50005];
int l,per[20],t,key;
int calc()
{
	int i,k,j;
	for(i=0;i<t;i++)
	{
		for(k=0;k<key;k++)
			mid[i*key+k]=x[i*key+per[k]-1];
	}
	j=1;
	for(i=1;i<l;i++)
		if(mid[i]!=mid[i-1])
			j++;
	return j;
}
int main()
{
	int tot,kase,i,k,j;
	scanf("%d",&tot);
	for(kase=1;kase<=tot;kase++)
	{
		scanf("%d",&key);
		scanf("%s",x);
		l=strlen(x);
		t=l/key;
		for(i=0;i<key;i++)
			per[i]=i+1;
		j=calc();
		while(next_permutation(per,per+key))
		{
			k=calc();
			if(k<j)
				j=k;
		}
		printf("Case #%d: %d\n",kase,j);
	}
	return 0;
}