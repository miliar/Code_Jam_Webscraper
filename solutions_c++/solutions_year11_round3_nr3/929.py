#include<iostream>
using namespace std;
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("2-small.txt","w",stdout);
	int N,L,H,j,cases,T,i;
	int array[10001];
	scanf("%d",&T);
	for(cases=1;cases<=T;cases++)
	{
		scanf("%d%d%d",&N,&L,&H);
		for(i=0;i<N;i++)
			scanf("%d",array+i);
		for(i=L;i<=H;i++)
		{
			for(j=0;j<N;j++)
				if(array[j]%i!=0 && i%array[j]!=0)
					break;
			if(j==N)
				break;
		}
		printf("Case #%d: ",cases);
		if(i<=H)
			printf("%d\n",i);
		else
			printf("NO\n");
	}
	return 0;
}
