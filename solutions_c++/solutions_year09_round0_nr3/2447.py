#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main()
{

	FILE *fp;
	char line[520];
	char match[22];
	int count[20] = {0};int n;

	int bigCnt[20][501]={0};

	fp = fopen("cur.in","r");

	// welcome to code jam
	sprintf(match,"welcome to code jam");
	
	if(fp != NULL)	
		fscanf(fp,"%d",&n);

  fgetc(fp);

  for(int k=0;k<n;k++)
  {
	fgets(line,510,fp);
	//printf("%s",line);

	//printf("%s",match);

	int L = strlen(line);
	L--;

	for (int i=0;i<20;i++) {
	    for (int j= 0;j<501;j++)
		   bigCnt[i][j] = 0;
	}


	for (int j= L-1;j>=0;j--)
	{	
		
		for(int i=0;i<19;i++)
		{

			if(i == 0) {
				bigCnt[i][j] =  bigCnt[i][j+1];
				if(match[18-i] == line[j])
					bigCnt[i][j] += 1;
			} else {
					bigCnt[i][j] = bigCnt[i][j+1];
				if(match[18-i] == line[j])
					bigCnt[i][j] += bigCnt[i-1][j+1];
			}


			bigCnt[i][j] %= 10000;
						
			

					
		}
	}

	printf("Case #%d: %d%d%d%d\n",(k+1),bigCnt[18][0]/1000, (bigCnt[18][0]%1000)/100, (bigCnt[18][0]%100)/10, bigCnt[18][0]%10);
  }

	return 0;
}

