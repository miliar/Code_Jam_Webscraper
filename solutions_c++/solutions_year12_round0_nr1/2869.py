#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
using namespace std;
char arr[110];
int main()
{
	char map[26] = {'y','h','e','s','o',
				'c','v','x','d','u',
				'i','g','l','b',
				'k','r','z','t','n',
				'w','j','p','f','m',
				'a','q'};
	int cases =0;
	int num = 1;
	FILE * pFile;
	pFile = fopen ("abc.in","r");
	FILE * pFile2;
	pFile2 = fopen("output.txt","w+");
	fscanf(pFile,"%d\n",&cases);
	
	while(cases>0)
	{
		fgets(arr,110,pFile);
		//fprintf(pFile2,"%s\n",arr);
		int length = strlen(arr);
		fprintf(pFile2,"Case #%d: ",num);
		num++;
		for(int i =0;i<length-1;i++)
		{
			if(arr[i]== ' ')
			{
				fprintf(pFile2," ");
			}
			else
			{
				fprintf(pFile2,"%c",map[arr[i]-'a']);
			}
		}
		if(cases>1)
			fprintf(pFile2,"\n");
		cases--;
	}
	fclose(pFile2);
}