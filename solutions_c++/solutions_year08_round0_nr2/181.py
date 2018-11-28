#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
	int cCnt, tCnt, abCnt, baCnt, cMin;
	int i,j,k,l;
	int cADep[100];
	int cARdy[100];
	int cBDep[100];
	int cBRdy[100];
	int cANeed[100];
	int cBNeed[100];
	int ctmp;
	
	scanf("%d",&cCnt);
	for(i=0;i<cCnt;i++)
	{
		scanf("%d",&tCnt);
		scanf("%d",&abCnt);
		scanf("%d",&baCnt);
		for(j=0;j<abCnt;j++)
		{
			scanf("%d:%d",&ctmp,&cADep[j]);
			cADep[j] = cADep[j] + ctmp*60;
			scanf("%d:%d",&ctmp,&cARdy[j]);
			cARdy[j] = cARdy[j] + ctmp*60 + tCnt;
			cANeed[j] = -1;
			//printf("A%d:d:%d a:%d\n",j,cADep[j],cARdy[j]);
		}
		for(j=0;j<baCnt;j++)
		{
			scanf("%d:%d",&ctmp,&cBDep[j]);
			cBDep[j] = cBDep[j] + ctmp*60;
			scanf("%d:%d",&ctmp,&cBRdy[j]);
			cBRdy[j] = cBRdy[j] + ctmp*60 + tCnt;
			cBNeed[j] = -1;
			//printf("B%d:d:%d a:%d\n",j,cBDep[j],cBRdy[j]);
		}
		
		for(j=0;j<abCnt;j++)
		{
			cMin = 100000000;
			ctmp = -1;
			for(k=0;k<baCnt;k++)
			{
				if(cBDep[k] >= cARdy[j] && cBNeed[k]==-1 && cMin > cBDep[k])
				{
					ctmp = k;
					cMin = cBDep[k];
				}
			}
			if(ctmp!=-1)
			{
				cBNeed[ctmp] = j;
				//printf("A%d B%d\n",j,ctmp);
			}
		}
		
		for(j=0;j<baCnt;j++)
		{
			cMin = 100000000;
			ctmp = -1;
			for(k=0;k<abCnt;k++)
			{
				if(cADep[k] >= cBRdy[j] && cANeed[k]==-1 && cMin > cADep[k])
				{
					ctmp = k;
					cMin = cADep[k];
				}
			}
			if(ctmp!=-1)
			{
				cANeed[ctmp] = j;
				//printf("B%d A%d\n",j,ctmp);
			}
		}
		
		printf("Case #%d: ", i+1);
		
		ctmp = 0;
		for(j=0;j<abCnt;j++)
		{
			if(cANeed[j]==-1)
			{
				ctmp++;
			}
		}
		
		printf("%d ", ctmp);
		
		ctmp = 0;
		for(j=0;j<baCnt;j++)
		{
			if(cBNeed[j]==-1)
			{
				ctmp++;
			}
		}
		
		printf("%d\n", ctmp);
	}
}
