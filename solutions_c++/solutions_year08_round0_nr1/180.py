#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
	int cCnt, sCnt, qCnt;
	int i,j,k,l;
	char cName[100][100];
	char qName[100];
	int qID[1000];
	int qPathMin[100];
	int qIDLast,CurrMin;
	
	//printf("Started %d\n",cCnt);
	scanf("%d",&cCnt);
	//printf("Cases:%d", cCnt);
	for(i=0;i<cCnt;i++)
	{
		scanf("%d",&sCnt);
		//printf("\nCase %d:Eng: %d\n", i,sCnt);
		for(j=0;j<sCnt;j++)
		{
			scanf("%s",cName[j]);
			//printf("%s,", cName[j]);
		}
		scanf("%d",&qCnt);
		//printf("\nCase %d:Q: %d\n", i,qCnt);
		for(j=0;j<qCnt;j++)
		{
			scanf("%s",qName);
			for(k=0;k<sCnt;k++)
			{
				if(strcmp(cName[k],qName)==0)
				{
					//printf("%d," ,k);
					qID[j] = k;
					k=sCnt+1;
				}
			}
			if(k==sCnt)
			{
				printf("not found: %s\n", qName);
				return(0);
			}
		}
		//printf("\n");
		/*for(j=0;j<qCnt;j++)
		{
			printf("%s\n", cName[qID[j]]);
		}*/
		for(j=0;j<sCnt;j++)
		{
			qPathMin[j] = 0;
		}
		qIDLast = -1;
		for(l=0;l<qCnt;l++)
		{
			j = qCnt - l - 1;
			if(qIDLast != qID[j])
			{
				CurrMin = 10000;
				for(k=0;k<sCnt;k++)
				{
					if(qID[j] != k)
					{
						if(CurrMin>qPathMin[k])
						{
							CurrMin=qPathMin[k];
						}
					}
				}
				qPathMin[qID[j]] = CurrMin +1;
			}
		}
		printf("Case #%d: ", i+1);
		CurrMin = 10000;
		for(k=0;k<sCnt;k++)
		{
			if(qID[0] != k)
			{
				if(CurrMin>qPathMin[k])
				{
					CurrMin=qPathMin[k];
					j = k;
				}
			}
		}
		printf("%d\n",qPathMin[j]);
	}
}
