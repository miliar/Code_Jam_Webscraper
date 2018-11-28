#include <stdio.h>
FILE *in = fopen("input.txt","rt");
FILE *out = fopen("output.txt","wt");

int n, k;
bool answer = false;
int sum = 1, factor = 0;
int main()
{
	int test = 0;
	int i = 0;
	int ix = 1;
	fscanf(in,"%d",&test);
	while(test--)
	{
		sum = 1;
		fscanf(in,"%d %d",&n,&k);
		answer = false;
		for(i = 1;i <= n; i++)
		{
			sum *= 2;			
		}
		factor = sum;
		sum --;
		if((k - sum)%factor == 0 && k!=0) answer = true;

		fprintf(out,"Case #%d: ",ix);
		if(answer == false)
		{
			fprintf(out,"OFF\n");
		}else fprintf(out,"ON\n");
		ix++;
	}
	return 0;
}
