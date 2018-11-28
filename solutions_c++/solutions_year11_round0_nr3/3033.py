#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int T, N;
	int ans;
	int i,j;
	int num, min, sum;
	int cnt;
	bool NO;

	freopen("D:\\VC2005\\google\\2011\\P3\\p3.in","r",stdin);
	freopen("D:\\VC2005\\google\\2011\\P3\\p3.out","w",stdout);

	scanf("%d\n", &T);
	
	for(i=1;i<=T;i++)
	{
		NO = false;
		scanf("%d\n", &N);
		
		scanf("%d", &ans);
		min = ans;
		sum = ans;
		for(j=1;j<N;j++)
		{
			scanf("%d", &num);
			if(min > num) min = num;
			ans = ans ^ num;
			sum = sum + num;
		}
		scanf("\n");
		//printf("%d\n", ans);
		/*cnt = 0;
		for(j=0;j<32;j++)
			if(ans & (1<<j)) cnt++;*/

		if(ans) printf("Case #%d: NO\n", i);
		else printf("Case #%d: %d\n", i, sum-min);
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
