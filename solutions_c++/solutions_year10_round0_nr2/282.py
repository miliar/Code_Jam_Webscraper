// codeJam.cpp : Defines the entry point for the console application.
//

#include "StdAfx.h"
#include <string.h>

#define CHARSIZE 64

int Compare(int s1[CHARSIZE],int s2[CHARSIZE])
{
	int i=0;
	// s1 >= s2 return 1
	// s1 < s2 return -1
	for (i=0; i<CHARSIZE; i++)
	{
		if (s1[i] > s2[i])
			return 1;
		if (s1[i] < s2[i])
			return -1;
	}
	return 0;
}

void Subtract(int s1[CHARSIZE],int s2[CHARSIZE])
{
	int i=0,tmp=0;
	int flag=Compare(s1,s2);
	
	if (flag==0)
		memset((void*)s1,0,sizeof(s1));

	for (i=CHARSIZE-1;i>=0;i--)
	{
		if (flag==1)
			s1[i] = s1[i] + tmp - s2[i];
		else
			s1[i] = s2[i] + tmp - s1[i];
		if (s1[i] < 0)
		{
			s1[i] += 10;
			tmp = -1;
		}
		else 
			tmp = 0;
	}	
}

void IntCopy(int a[CHARSIZE],int b[CHARSIZE])
{
	int i=0;
	for (i=0; i<CHARSIZE; i++)
		a[i] = b[i];
}

int Len(int a[CHARSIZE])
{
	int i=0;
	for (i=0; i<CHARSIZE; i++)
		if (a[i])
			break;
	return CHARSIZE - i;
}

void print(int a[CHARSIZE])
{
	int i=0;
	for(i=0; i<CHARSIZE; i++)
		printf("%d",a[i]);
	printf("\n");
}

void mod(int a[CHARSIZE],int b[CHARSIZE])
{
	int lena=0,lenb=Len(b);;
	int c[CHARSIZE];
	int i=0;

	while(Compare(a,b)>=0)
	{
		lena=Len(a);		
		
		if (lena > lenb)
		{
			memset((void*)c,0,sizeof(c));
			for (i=CHARSIZE-lenb; i<CHARSIZE; i++)
				c[i-(lena-lenb-1)] = b[i];
			Subtract(a,c);			
		}
		else
		{
			Subtract (a,b);						
		}		
	}
}

void gcd(int a1[CHARSIZE],int b1[CHARSIZE])
{
	int c[CHARSIZE],a[CHARSIZE],b[CHARSIZE];
	int i=0,flag=0;
	int lena,lenb;

	// print(a1);
	// print(b1);

	IntCopy(a,a1);
	IntCopy(b,b1);

	lena = Len(a);
	lenb = Len(b);

	while (1)
	{		
		if(lena == 0 || lenb == 0)
			break;	
		
		if (lena > lenb)
		{
			memset((void*)c,0,sizeof(c));
			for (i=CHARSIZE-lenb; i<CHARSIZE; i++)
				c[i-(lena-lenb-1)] = b[i];
			Subtract(a,c);
			lena = Len(a);
		}
		else if(lena < lenb)
		{
			memset((void*)c,0,sizeof(c));
			for (i=CHARSIZE-lena; i<CHARSIZE; i++)
				c[i-(lenb-lena-1)] = a[i];
			Subtract(b,c);
			lenb = Len(b);
		}
		else
		{
			flag = Compare(a,b);
			if (flag == 1)
			{
				Subtract (a,b);
				lena = Len(a);
			}
			else
			{
				Subtract(b,a);
				lenb = Len(b);
			}			
		}
	}

	if (lena)
		IntCopy (a1,a);
	else if(lenb)
		IntCopy(a1,b);
	// print(a1);
}

int main(int argc, char* argv[])
{

	/* ! ( (k+1)%(2^n) )*/
	FILE *fpIn,*fpOut;
	int caseNo=0,num=0,tmpNum=0;
	char input[1024][CHARSIZE];
	int large[1024][CHARSIZE];
	long len0=0;
	int i=0,k=0,j=0,m=0,tmpLen=0;
	

	fpIn = fopen("B-large.in","r");
	fpOut = fopen("B-large.out","w");

	fscanf(fpIn,"%d",&caseNo);		
	for (i=1; i<=caseNo; i++)
	{
		fscanf(fpIn,"%d",&num);		
		for (k=0; k<num; k++)
		{
			fscanf(fpIn,"%s",input[k]);		
		}		
		for (k=0; k<num; k++)
			for (j=k+1; j<num; j++)
				if (strcmp(input[k],input[j])==0)
				{
					strcpy(input[j],input[num-1]);
					num--;
				}
		tmpNum = num;
		for (k=0; k<num; k++)
		{
			tmpLen = strlen(input[k]);
			for (m=0,j=CHARSIZE-1;m<tmpLen; m++,j--)
				large[k][j] = input[k][tmpLen-m-1] - '0';
			for (;j>=0;j--)
				large[k][j] = 0;			
		}
		//////////////////////////////////////////////////////////////////////////
		
		for (k=0; k<num-1; k++)		
			Subtract(large[k],large[num-1]);
		num --;

		while (num!=1)
		{
			for (k=0; k<num-1; k++)
				gcd(large[k],large[k+1]);				
			num --;
		}

		IntCopy(large[tmpNum],large[tmpNum-1]);		
		mod(large[tmpNum],large[0]);
		// if ( Compare(large[tmpNum],large[0]) == 0 || Compare(large[tmpNum],large[tmpNum-1])==0)
		if (Len(large[tmpNum]) == 0)
		{
			memset((void*)large[0],0,sizeof(large[0]));
		}
		else
		{
			Subtract(large[0],large[tmpNum]);
		}

		fprintf(fpOut,"Case #%d: ",i);
		len0 = Len(large[0]);
		if (len0==0)
		{
			fprintf(fpOut,"0\n");
		}
		else
		{
			for(k=CHARSIZE-len0; k<CHARSIZE; k++)
				fprintf(fpOut,"%d",large[0][k]);
			fprintf(fpOut,"\n");
		}
	}

	fclose(fpOut);
	fclose(fpIn);

	return 0;
}

