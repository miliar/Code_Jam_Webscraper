#include <stdio.h>
#include <stdlib.h>

void main()
{
	FILE* input = ::fopen("a-small.in", "r");
	if(!input)
	{
		::printf("Cannot open input file.\n");
		::exit(1);
	}

	FILE* output = ::fopen("a-small.out", "w");
	if(!output)
	{
		::printf("Cannot open output file.\n");
		::exit(1);
	}

	register int t;
	::fscanf(input, "%d", &t);
	for(register int i = 0; i < t; ++i)
	{
		register int n;
		register int k;

		::fscanf(input, "%d%d", &n, &k);

		register bool spanners[30];
		for(int j = 0; j < 30; ++j)
			spanners[j] = false;

		for(register int j = 0; j < k; ++j)
		{		
			register int power = true;

			for(register int l = 0; l < n; ++l)
			{	
				power = spanners[l];
				spanners[l] = !spanners[l];

				if(!power)
					break;
			}
		}

		register int j = -1;
		while(++j < n && spanners[j]);

		::fprintf(output, "Case #%d: %s\n", i + 1, j == n? "ON": "OFF");
	}

	if(::fclose(output)) 
		::printf("Cannot close output file.\n");

	if(::fclose(input)) 
		::printf("Cannot close input file.\n");
}