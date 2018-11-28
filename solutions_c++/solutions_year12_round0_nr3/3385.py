#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void main()
{
	FILE *infp = fopen("input.txt","r");
	FILE *outfp = fopen("output.txt","w");

	int A, B;
	int i,j,k,m;
	int l;
	int T;
	int cnt;

	char s[9];
	

	fscanf(infp,"%d",&T);

	for(k=1;k<=T;k++)
	{
		int *arr;
		cnt=0;

		fscanf(infp,"%d %d",&A,&B);

		arr = (int *) malloc(sizeof(int) * (B+1));

		for(i=A;i<=B;i++)
		{
			int n;
			itoa(i,s,10);
			l=strlen(s);
			for(j=1;j<=l-1;j++)
			{
				char tmp = s[l-1];
				s[l-1] = 0;
				for(m=l;m>0;m--)
				{
					s[m] = s[m-1];
				}
				s[0] = tmp;
				n = atoi(s);
				if(n <= B && i < n)// && arr[n] != 1)
				{
					arr[n] = 1;
 					cnt++;
				}
			}
		}
		fprintf(outfp,"Case #%d: %d\n",k,cnt);
		free(arr);
	}

}