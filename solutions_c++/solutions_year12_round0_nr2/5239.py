#include <cstdio>
#include <cstdlib>

/*int compare(const void * a,const void * b)
{
	return *(int*)b-*(int*)a;
}
*/
int main(void)
{
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	int N;
	scanf("%d\n", &N);
	for(int j=0; j<N; j++) 
	{	
		int max=0,p,S,T;
		scanf("%d %d %d",&T,&S,&p);
		int marks[T];
		for(int i=0; i<T; i++)
			scanf(" %d", &marks[i]);
		scanf("\n");
		//qsort(marks,T,sizeof(int),compare);
		//printf("%d ", p);
		for(int i=0; i<T; i++)
		{
		  	int maximum=marks[i]/3;
		  	if(marks[i]%3!=0)
		  		maximum++;
			if(maximum<p && S>0 && maximum+1>=p && marks[i]!=0)
			{
				S--;
				maximum++;
			}
			if(maximum-(marks[i]-maximum-(marks[i]/3))>2)
				continue;
			if(maximum>=p) 
			{
				max++;
				//printf("%d ", maximum);
			}
		}   
		printf("Case #%d: %d\n", j+1,max);
	}
	return 0;
}
