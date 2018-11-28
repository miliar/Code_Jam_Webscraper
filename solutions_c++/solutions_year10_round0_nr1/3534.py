#include <stdio.h>
#include <cmath>

int main()
{
	FILE* file;
	file = fopen("test.txt", "r");
	
	FILE* output;
	output = fopen("output.txt", "w");

	
	int total;
	fscanf(file, "%d", &total);
	int i;
	for(i = 1; i <= total; i++)
	{
		unsigned long n;
		unsigned long k;
		fscanf(file, "%d %d", &n, &k);
		unsigned long n2 = 1 << n;
		while(k - n2 < k)
			k -= n2;
		if(k == n2 - 1)
		{
			fprintf(output, "Case #%d: ON\n", i);
		}
		else
		{
			fprintf(output, "Case #%d: OFF\n", i);
		}
	}
}