#include <stdio.h>
#include <string>
#include <cstring>

int main()
{
	freopen("F:\\code\\topcoder\\compete\\compete\\codejam_2011\\C-large.in","r",stdin);
	freopen("F:\\code\\topcoder\\compete\\compete\\codejam_2011\\result.txt","w",stdout);

	int caseNum;
	int sum;
	int t;
	scanf("%d",&t);
	int bit_num[30];
	bool isEnd = 0;
	caseNum = 0;
	while (caseNum<t)
	{
		isEnd = 0;
		sum = 0;
		printf("Case #%d: ",caseNum+1);
		memset(bit_num,0,sizeof(bit_num));
		int n;
		scanf("%d",&n);
		int m = 10000000;
		for (int i = 0;i<n;i++)
		{
			int c;
			scanf("%d",&c);
			if (c<m)
			{
				m = c;
			}
			sum+=c;
			for (int j = 0;j<21;j++)
			{
				if ((c&(1<<j)) > 0)
				{
					bit_num[j]++;
				}
			}
		}
		for (int i = 0;i<21;i++)
		{
			if (bit_num[i]%2>0)
			{
				printf("NO\n");
				isEnd = 1;
				break;
			}
		}
		if (!isEnd)
		{
			printf("%d\n",sum-m);
		}
		caseNum++;
	}
}