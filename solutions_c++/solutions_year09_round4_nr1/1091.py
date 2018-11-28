#include <stdio.h>

using namespace std;

#define MAX 50

int main()
{
	int pos[MAX];
	int tmp;
	int i,j;
	int ncase, ccnt;
	int resp;
	int n;
	int t2;
	scanf("%d",&ncase);
	for(ccnt=1;ccnt<=ncase;++ccnt)
	{
		scanf("%d",&n);
		for(i=0;i<n;++i)
		{
			pos[i]=-1;
			for(j=0;j<n;++j)
			{
				scanf("%1d",&tmp);
				if(tmp)
					pos[i]=j;
			}
			
		}
		resp=0;
/*		while(sw)
		{
			sw=0;
			printf(" sw\n");
			for(i=n-1;i>=0;--i)
			{
				printf("%d ",i);
				if(pos[i]>i && pos[i]>pos[i+1])
				{
					sw=1;
					printf("trocou");
					++resp;
					tmp=pos[i];
					pos[i]=pos[i+1];
					pos[i+1]=tmp;
				}
				printf("\n");
			}
			printf("-> ");
			for(i=0;i<n;++i)
				printf("%d(%d) ",pos[i],i);
			printf("\n");
		}*/

		for(i=0;i<n-1;++i)
		{
			tmp=pos[i];
			for(j=i;j<n-1 && tmp>i;++j)
			{
				t2=pos[j+1];
				pos[j+1]=tmp;
				tmp=t2;
				++resp;
			}
		}
		printf("Case #%d: %d\n",ccnt,resp);
	}
	return 0;
}

