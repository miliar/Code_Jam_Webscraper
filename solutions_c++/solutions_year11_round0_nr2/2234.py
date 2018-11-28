#include <stdio.h>
#include<iostream>
#include<fstream>
#include<vector>
using namespace std;


bool findOppose(char oppose[][2],int ocount,char a,char result[],int count);
int matchpair(char pair[][3],char a,char b,int count);

int main()
{
	FILE *fPtr;
	FILE *fOut;
	int line;
	//vector<char> result;
	int index=-1;
	char tmp;

	char pair[36][3];
	char oppose[28][2];
	char result[10];

	int pairscount,opposecount;

	fstream flie;
	fOut=fopen("Blarge.out","w");
	if((fPtr=fopen("Blarge.in","r"))==NULL)
		printf("file can not be open");
	else
	{
		fscanf(fPtr,"%d ",&line);
		printf("%d\n",line);
		int count;
		for(int i=0;i<line;i++)
		{
			index=-1;
			fscanf(fPtr,"%d ",&pairscount);
			for(int j=0;j<pairscount;j++)
			{
				fscanf(fPtr,"%c%c%c ",&pair[j][0],&pair[j][1],&pair[j][2]);
			}
			
			fscanf(fPtr,"%d ",&opposecount);
			for(int j=0;j<opposecount;j++)
				fscanf(fPtr,"%c%c ",&oppose[j][0],&oppose[j][1]);
			
			fscanf(fPtr,"%d ",&count);
			for(int j=0;j<count;j++){
				fscanf(fPtr,"%c",&tmp);
				if(index>-1)
				{
					int pindex=matchpair(pair,tmp,result[index],pairscount);
					if(pindex>-1)
						result[index]=pair[pindex][2];
					else if(findOppose(oppose,opposecount,tmp,result,index+1))index=-1;							
					else result[++index]=tmp;
				}else result[++index]=tmp;
			}

//==========================Output==============================

			fprintf(fOut,"Case #%d: [",i+1);
			if(index>-1) {fprintf(fOut,"%c",result[0]);printf("%c",result[0]);}
			for(int j=0;j<index;)
			{
				fprintf(fOut,", %c",result[++j]);
				printf(", %c",result[j]);
			}
			fprintf(fOut,"]\n");

			printf("Case #%d: ",i+1);
			printf("\n");
		}
	}
	fclose(fPtr);
	fclose(fOut);
	printf("done");
	getchar();
	return 0;
}

int matchpair(char pair[][3],char a,char b,int count)
{
	for(int i=0;i<count;i++)
	{
		if((a==pair[i][0]&& b==pair[i][1])||(b==pair[i][0]&& a==pair[i][1]))
			return i;
	}
	return -1;

}
bool findOppose(char oppose[][2],int ocount,char a,char result[],int count)
{
	for(int i=0;i<ocount;i++)
	{
		if(a==oppose[i][0])
			for(int j=0;j<count;j++) {
				if(result[j]==oppose[i][1])return true;
			}
		else if(a==oppose[i][1])
			for(int j=0;j<count;j++) {
				if(result[j]==oppose[i][0])return true;
			}
	}
	return false;
}
/*
int findOppose1(int index,char tag,char result[])
{
	for(int i=0;i<index;i++)
	{
		if(tag==result[i]) return i;
	}
	return -1;

}*/