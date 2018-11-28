#include <stdio.h>
#include <stdlib.h>

void main()
{
	FILE* in = ::fopen("c.in", "r");
	FILE* out = ::fopen("c.out", "w");

	int t;
	::fscanf(in, "%d", &t);

	int* g = new int[1000];

	for(int i = 0; i < t; ++i)
	{
		int r, k, n;

		::fscanf(in, "%d%d%d", &r, &k, &n);

		__int64 s = 0;
		for(int j = 0; j < n; ++j)
		{
			::fscanf(in, "%d", g + j);
			s += g[j];
		}

		if(s <= k)
			::fprintf(out, "Case #%d: %lld\n", i + 1, s * r);
		else
		{
			__int64 total_l = 0;
			__int64 total_h = 0;

			int index = 0;
			__int64 sum = 0;

			for(int j = 0; j < r; ++j)
			{
				while(sum + g[index] <= k)
				{
					sum += g[index];
					if(++index >= n)
						index = 0;
				}

				total_l += sum % 1000000000;
				total_h += sum / 1000000000;
				total_h += total_l / 1000000000;
				total_l %= 1000000000;

				sum = 0;

				if(index == 0)
				{
					int multi = r / (j + 1);
					total_l *= multi;
					total_h *= multi;
					total_h += total_l / 1000000000;
					total_l %= 1000000000;

					r %= (j + 1);

					for(j = 0; j < r; ++j)
					{
						while(sum + g[index] <= k)
						{
							sum += g[index];
							if(++index >= n)
								index = 0;
						}

						total_l += sum % 1000000000;
						total_h += sum / 1000000000;
						total_h += total_l / 1000000000;
						total_l %= 1000000000;

						sum = 0;
					}
					break;
				}
			}

			if(total_h == 0)
				::fprintf(out, "Case #%d: %d\n", i + 1, (int)total_l);
			else
				::fprintf(out, "Case #%d: %lld%9.9d\n", i + 1, total_h, (int)total_l);
		}
	}

	delete[] g;

	::fclose(out);
	::fclose(in);
}