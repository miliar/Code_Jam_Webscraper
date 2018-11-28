#include <cstdio>
int main()
{
int T, N;
scanf("%d",&T);
for(int i =1; i <= T; i++)
{
int N;
scanf("%d",&N);
int res = 0;
int sum = 0;
int min = 10000000;
for(int k = 0; k < N; k++)
{
	int c;
	scanf("%d",&c);
	sum+= c;
	if(c < min)
		min = c;
	res ^= c;

}
if(res == 0)
	printf("Case #%d: %d\n",i,sum - min);
else 
	printf("Case #%d: NO\n",i);
	
}

return 0;
}
