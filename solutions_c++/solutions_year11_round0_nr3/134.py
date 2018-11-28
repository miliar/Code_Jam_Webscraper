#include<stdio.h>
#include<string.h>
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T, n, x, sumValue, minValue,xorValue;
	scanf("%d",&T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d",&n);
		scanf("%d",&x);
		sumValue = x;
		xorValue = x;
		minValue = x;
		for(int i = 1; i < n; i++){
			scanf("%d",&x);
			sumValue += x;
			xorValue ^= x;
			minValue = (minValue>x?x:minValue);
		}
		if(xorValue){
			printf("Case #%d: NO\n", t);
		}else{
			printf("Case #%d: %d\n",t, sumValue-minValue);
		}
	}
	return 0;
}

