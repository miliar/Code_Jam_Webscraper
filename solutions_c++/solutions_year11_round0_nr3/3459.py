#include<cstdio>
using namespace std;
int c[2000];
void work(int x)
{
	int tot =0;
	int ans = 0;
	int min = 0x7fffffff;
	int n;
	printf("Case #%d: ",x);
	scanf("%d",&n);
	for(int i =0 ; i <n;i++){
		scanf("%d",&c[i]);
		tot ^= c[i];
		if(c[i] < min)min = c[i];
		ans += c[i];
	}
	if(tot != 0){
		printf("NO\n");
		return;
	}
	printf("%d\n",ans - min);
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i = 1; i <= t; i++)work(i);
}
