#include<cstdlib>
#include<cstdio>
int N;
int A[1000];
void Init()
{
	scanf("%d",&N);
	for (int i=0;i<N;i++) scanf("%d",&A[i]);
}
void Solve(int c)
{
	printf("Case #%d: ",c);
	int sum=0;
	for (int i=0;i<N;i++) sum=sum^A[i];
	if (sum!=0) printf("NO\n");
		else
		{
			int min=A[0];
			sum=0;
			for (int i=0;i<N;i++)
			{
				sum=sum+A[i];
				min=(min>A[i]?A[i]:min);
			}
			printf("%d\n",sum-min);
		}
}
int main()
{
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		Init();
		Solve(i+1);
	}
	return 0;
}
