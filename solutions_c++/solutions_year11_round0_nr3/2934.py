#include <stdio.h>

int main()
{
	int t;
	int n;
	int c;
	int min;
	int sum;
	int flag;
	int i;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	for(i = 1; i <= t; i++)
	{
		min = 1000001;
		sum = 0;
		flag = 0;
		
		scanf("%d",&n);
		while(n--)
		{
			scanf("%d",&c);
			sum += c;
			if(c < min)
				min = c;
			flag ^= c; 
		}
		if(flag == 0)             /*根据异或计算，如果存在两等份，则flag必为0*/
		{
			printf("Case #%d: %d\n",i,sum-min);  /*(sum-min) ^ min == 0*/ 
		}	
		else
			printf("Case #%d: NO\n",i);
	}
/*	fclose(stdin);
	fclose(stdout);
*/	return 0;
}
