#include <stdio.h>
#include <stdlib.h>

void main()
{
	FILE* input = ::fopen("c-small.in", "r");
	if(!input)
	{
		::printf("Cannot open input file.\n");
		::exit(1);
	}

	FILE* output = ::fopen("c-small.out", "w");
	if(!output)
	{
		::printf("Cannot open output file.\n");
		::exit(1);
	}

	register int t;
	::fscanf(input, "%d", &t);

	int* groups = new int[1000];

	for(register int i = 0; i < t; ++i)
	{
		register int r;
		register int k;
		register int n;

		::fscanf(input, "%d%d%d", &r, &k, &n);

		int sum = 0;
		for(register int j = 0; j < n; ++j)
		{
			::fscanf(input, "%d", groups + j);
			sum += groups[j];
		}

		if(sum <= k)
			::fprintf(output, "Case #%d: %I64d\n", i + 1, (__int64)sum * (__int64)r);
		else
		{
			register __int64 total = 0;

			register int index = 0;
			register int current_sum = 0;

			for(register int j = 0; j < r; ++ j)
			{
				while(current_sum + groups[index] <= k)
				{
					current_sum += groups[index];
					if(++index >= n)
						index = 0;
				}

				total += current_sum;
				current_sum = 0;
			}

			::fprintf(output, "Case #%d: %I64d\n", i + 1, total);
		}
	}

	delete[] groups;

	if(::fclose(output)) 
		::printf("Cannot close output file.\n");

	if(::fclose(input)) 
		::printf("Cannot close input file.\n");
}