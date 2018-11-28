#include<stdio.h>
#include<algorithm>
using namespace std;

int ar[1010];
int main()
{
	freopen("C-large.in","r",stdin);
 	freopen("out.txt","w",stdout);

	int tcase, i, n, j, sum, res, s;
	scanf("%d",&tcase);
	for(i = 0;i<tcase;i++)
	{
		scanf("%d",&n);
		
		for(j = 0;j<n;j++)
			scanf("%d",&ar[j]);

	
		res = -1;
		sum = 0;
		s = 0;
		for(j = 0;j<n;j++)
		{	
			sum = sum^ar[j];
			s += ar[j];
		}

		if(sum==0)
		{
			sort(ar,ar+n);
			s = s - ar[0];
			res= 0;
		
		}
		
		if(res==-1)
			printf("Case #%d: NO\n",i+1);
		else
			printf("Case #%d: %d\n",i+1,s);
	

		
	
	
	
	}
return 0;
}