#include <stdio.h>

int main()
{
	int t, ccnt;
	int n;

	scanf("%d",&t);

	for(ccnt=1;ccnt<=t;++ccnt)
	{
		scanf("%d",&n);
		int resp=0,sum=0;
		int men = 1111000;
		for(int i=0;i<n;++i)
		{
			int tmp;
			scanf("%d",&tmp);
			sum+=tmp;
			resp^=tmp;
			if(tmp<men)
				men=tmp;
		}

		printf("Case #%d: ",ccnt);
		if(!resp)
			printf("%d\n",sum-men);
		else
			printf("NO\n");
	}
	return 0;
}

