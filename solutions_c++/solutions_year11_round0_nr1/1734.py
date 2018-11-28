#include <stdio.h>
#include <stdlib.h>

#define MAX 110

int main()
{
	int p1,p2;
	int t1,t2;
	int resp;
	char tmp;
	int pb;

	int t,ccnt;
	scanf("%d",&t);

	for(ccnt=1;ccnt<=t;++ccnt)
	{
		int n;
		resp=0;
		p1=p2=1;
		t1=t2=0;
		scanf("%d",&n);

		for(int i=0;i<n;++i)
		{
			scanf(" %c %d",&tmp,&pb);
			int parc=0;
			if(tmp == 'O')
			{
				parc=abs(pb-p1);
				parc-=t1;
				if(parc<0)
					parc=0;
				++parc;
				t1=0;
				t2+=parc;
				resp+=parc;
				p1=pb;
			}
			else
			{
				parc=abs(pb-p2);
				parc-=t2;
				if(parc<0)
					parc=0;
				++parc;
				t2=0;
				t1+=parc;
				resp+=parc;
				p2=pb;
			}
		}

		printf("Case #%d: %d\n",ccnt,resp);
	}
	return 0;
}


