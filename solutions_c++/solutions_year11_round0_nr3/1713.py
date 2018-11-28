#include<iostream>
using namespace std;

int main()
{
	freopen("C-large.in.txt","r",stdin);
	freopen("cout.txt","w+",stdout);

	int t,test=1,i,j,n,k,mm,sum;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		mm=1100000,sum=0;
		for(j=0,i=0;i<n;i++)
		{
			scanf("%d",&k);
			sum+=k;
			j=j^k;
			if(k<mm) mm=k;
		}
		printf("Case #%d: ",test++);
		if(j) printf("NO\n");
		else printf("%d\n",sum-mm);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}