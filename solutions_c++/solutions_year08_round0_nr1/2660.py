#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int mapIsFull(int charMap[100],int searchCount);

void main(){
	FILE *fp;
	FILE *ofp;
	int loop, loopBound, i, j, cnt, flag;
	int searchCount,queryCount;

	char searchEngine[100][100];
	char queryName[1000][100];
	int searchMap[100];

	fp=fopen("A-small-attempt2.in","r");
	ofp=fopen("A-small-attempt2.out","w");
	fscanf(fp,"%d",&loopBound);
	for(loop=0;loop<loopBound;loop++)
	{
		flag=1;
		cnt=0;
		memset(searchMap,0,100);
		fscanf(fp,"%d",&searchCount);
		fflush(stdin);
		for(i=0;i<searchCount;i++)
		{
			fgets(searchEngine[i],100,fp);
			if (searchEngine[i][0] == '\n') { i --; continue; }
		}
		fscanf(fp,"%d",&queryCount);
		fflush(stdin);
		for(i=0;i<queryCount;i++)
		{
			fgets(queryName[i],100,fp);
			if (queryName[i][0] == '\n') { i --; continue; }
		}
		for(i=0;i<queryCount;i++)
		{
			for(j=0;j<searchCount;j++){
				if(!strcmp(queryName[i],searchEngine[j])){
					searchMap[j]++;
					if(mapIsFull(searchMap,searchCount)){
						cnt++;
						i--;
						memset(searchMap,0,100);
					}
					break;
				}
			}
		}		
		fprintf(ofp,"Case #%d: %d\n",loop+1,cnt);
	}
}

int mapIsFull(int searchMap[100],int searchCount){
	int i;
	int value=0;
	for(i=0;i<searchCount;i++){
		if(searchMap[i]==0)
			value++;
	}
	if(value>0)
		return 0;
	return 1;
}