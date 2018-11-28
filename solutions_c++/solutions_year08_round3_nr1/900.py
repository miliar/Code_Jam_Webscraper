/*
	Text Messaging Outrage
	Small Input
	Google Code Jam '08 - Round 1C
	-trisha
	27th July 2008
*/

#include<stdio.h>
#include<string.h>
#include<conio.h>
#include<math.h>
#include<iostream.h>

#define N_MAX 100
#define P_MAX 1000
#define K_MAX 1000
#define L_MAX 1000
#define F_MAX 100000

long freq[L_MAX];
int n, p, k, l;

void sort()
{
	int i,j, temp, max;

	for(i=0; i<(l-1); i++)
	{
		max=i;

		for(j=i+1; j<l; j++)
		{
			if(freq[j]>freq[max])
				max=j;
		}
		temp=freq[i];
		freq[i]=freq[max];
		freq[max]=temp;
	}
}

void main()
{
	int i, j, m, temp;
	long output;

	scanf("%d", &n);

	for(i=1;i<=n;i++)
	{
 		scanf("%d", &p);
		scanf("%d", &k);
		scanf("%d", &l);

		for(j=0; j<L_MAX; j++)
			freq[j]=0;
	
		for(j=0; j<l; j++)
			scanf("%ld", &freq[j]);

		sort();

		output=0;
		temp=0;

		for(j=1; j<=p; j++)
		{
			for(m=0; m<k; m++)
			{
				if(temp>=l)
					break;
				output+=freq[temp++]*j;
			}
		}
		printf("Case #%d: %ld\n", i, output);
	}
}




