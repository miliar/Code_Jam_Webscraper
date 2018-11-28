#include <stdio.h>

int main()
{
	int num,k;
	int ncases;
	int ccnt;
	int flag;
	scanf("%d",&ncases);
	for(ccnt=1;ccnt<=ncases;++ccnt)
	{
		flag=1;
		scanf("%d %d",&k,&num);
		for(int i=0;i<k;++i)
			if(!(num&(1<<i)))
				flag=0;
		printf("Case #%d: %s\n",ccnt,flag?"ON":"OFF");
	}
	return 0;
}
