#include <stdio.h>
#define max_size_n 1001
FILE *in = fopen("input.txt","rt");
FILE *out = fopen("output.txt","wt");
int k, n, g;
int group[max_size_n];
int euro[max_size_n];
int shift[max_size_n];
__int64 answer;
int ix = 1;
int main()
{
	int R = 0;
	int i, j;
	fscanf(in,"%d",&R);
	while(R--)
	{
		answer = 0;
		fscanf(in,"%d %d %d",&k,&n,&g);
		for(i = 1;i <= g; i++)
		{
			euro[i] = 0;
			shift[i] = 0;
			fscanf(in,"%d",&group[i]);
		}
		for(i=1;i<=g;i++)
		{
			
			if(group[i] <= n) euro[i] = group[i];
			j = i + 1;
			if(j > g) j = 1;
			shift[i] = j;
			while(true)
			{
				
				if(euro[i] + group[j] > n || i == j) break;
				euro[i] += group[j];
				shift[i] = j==g?1:j+1;
				++j;
				if(j > g) j = 1;
			}
		}
		j = 1;
		for(i=1;i<=k;i++)
		{
			answer += euro[j];
			j = shift[j];
		}
		fprintf(out,"Case #%d: %lld\n",ix,answer);
		++ix;
	}
	return 0;
}