/*
Snapper Chain
Name: Wenting Deng
Date: 5/7/2010
Email: wtdeng@gmail.com
*/

/*
T 1, 10000
small: N 1,10, K 0,100
large: N 1,30  K 0,1e8
*/
#define maxT 10000
#define BUF_SIZE 1024
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;
int dec2bin(int dec, int *bint);
int main()
{
	FILE *buffer;
	FILE *output;
	char readaline[BUF_SIZE];
	char inputname[BUF_SIZE];
	int t,s;
	int n,k;
	int onlist[maxT];
	int alln[maxT];
	int allk[maxT];
	scanf("%s", inputname);
	if((buffer=fopen(inputname, "r")) == NULL)
		printf("File has NOT been opened\n");
	if(fgets(readaline, BUF_SIZE, buffer)==NULL)
		printf("read number of cases error\n");
	else
		sscanf(readaline, "%d%*c", &t);
	s = t;	
	while(s!=0)
	{
		fgets(readaline, BUF_SIZE, buffer);
		readaline[strlen(readaline)-1] = '\0';
		sscanf(readaline, "%d %d%*c", &n, &k);
		alln[t-s] = n;
		allk[t-s] = k;
		s--;
	}
	fclose(buffer);
	
	for (int it=0; it<t; it++)
	{
		int decimal;
		decimal = allk[it];
		int num;
		num = alln[it];
		int binary[80];//initialize to zeros ?
		int length=0;
		int on;
		length = dec2bin(decimal, binary);
		on = binary[length-num];
		for(int i=length-num+1;i<length;i++)
			on = on & binary[i];		
		onlist[it] = on;	
//		printf("i=%d, on=%d\n", it, on);
// 0-OFF, 1-ON
	}
	
	char outputname[BUF_SIZE];
	inputname[strlen(inputname)-2] = 'o';
	inputname[strlen(inputname)-1] = 'u';
	inputname[strlen(inputname)] = 't';
	inputname[strlen(inputname)+1] = '\0';

	strcat(outputname, inputname);
	printf("%s\n", outputname);
	
	output = fopen(outputname,"w");
	for(int j=0; j<t; j++)
	{
		if(onlist[j]==1)
		fprintf(output, "Case #%d: %s\n", j+1, "ON");

		if(onlist[j]==0)
		fprintf(output, "Case #%d: %s\n", j+1, "OFF");
	}
	fclose(output);
	return 0;
}
int dec2bin(int dec, int *bint)
{
	int k=0;
	int n=0;
	int res=0;
	int test=0;
	int revbint[80];
	do 
	{
		res = dec%2;
		dec = dec/2;
		revbint[k] = res;
		k++;
	} while(dec>0);
	while(k>=0)
	{
		bint[n++] = revbint[--k];
	}
	return n-1;
}

