#include<stdio.h>
#include<math.h>

int main()
{
	//FILE* in = fopen("A-large-practice.in","r");	//¶óÁö 
	FILE* in = fopen("A-large.in","r");	//½º¸ô
	FILE* out = fopen("output.out","w");
	int t;
	fscanf(in,"%d",&t);
	for(int test = 1; test <= t;test++)
	{
		int n,k;
		fscanf(in,"%d %d",&n,&k);
		if(n > k)
			fprintf(out,"Case #%d: OFF\n",test);
		else
		{
			while( pow(2.0,n) < k)
				k = k % (int)pow(2.0,n);
			if(k == (pow(2.0,n) -1) )
				fprintf(out,"Case #%d: ON\n",test);
			else	
				fprintf(out,"Case #%d: OFF\n",test);
		}	
	}
	fclose(in);
	fclose(out);
	return 0;
}