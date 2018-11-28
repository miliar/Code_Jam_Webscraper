#include<stdio.h>
#include<math.h>

int ans;

void func(int * M , int start , int end)
{

	int i;
	for(i=start ; i <=end ; i++)
	{
		if(M[i]>0)
			break;
	}
	if(i==end+1)
		return ;


	ans++;

	for(int i=start ; i<=end ; i++)
	{
		if(M[i] != 0 )
			M[i] --;
	}
	func(M,start,(start+end)/2);
	func(M,(start+end)/2+1, end);
	return ;
}

int main(){
	int tc , p;
	int M[2000];
	char str[100000];
	scanf("%d",&tc);
	int n;
	for(int Q=0 ; Q<tc ; Q++)
	{
		ans=0;
		scanf("%d",&p);
		for(int i=0; i <pow(2,p) ; i++)
		{
			scanf("%d",&M[i]);
			M[i] = p-M[i];
		}


		for(int i=p-1 ; i>=0 ; i--)
		{
			for(int j=0;j<pow(2,i) ; j++)
			{
				scanf("%d",&n);
			}

		}

		func(M, 0 , pow(2,p)-1);
		printf("Case #%d: %d\n",Q+1 , ans);

	}
	return 0;
}
