#include <cstdio>
#include <cstdlib>
#include <cstring>

int main(void)
{
	char sename[120][120];
	int q[1200];
	int count[120];
	int qnum, senum, temp, result;
	
	char line[120];
	fgets(line, 120, stdin);

	int cases = atoi(line);
	for (int c = 0; c < cases; ++c)
	{
		fgets(line, 120, stdin);
		senum = atoi(line);
		for (int i = 0; i < senum; ++i)
		{
			fgets(sename[i], 120, stdin);
			count[i] = 0;
		}

		fgets(line, 120, stdin);
		qnum = atoi(line);
		for (int i = 0; i < qnum; ++i)
		{
			fgets(line, 120, stdin);
			
			for (int j = 0; j < senum; ++j)
			{
				if (0 == strcmp(sename[j], line))
				{
					temp = j;
					break;
				}
			}

			q[i] = temp;
		}

		// loading complete
		
		result = 0;
		if (0 < qnum)
		{
			result = -1;
			for (int i = 0; i < qnum; )
			{
				temp = -1;				
				for (int j = 0; j < senum; ++j)
				{					
					int k = i;
					for (; k < qnum; ++k)
					{
						if (j == q[k])
						{
							break;
						}						
					}

					if (temp < k - i)
					{
						temp = k - i;
					}
				}

				i += temp;
				++result;
			}
		}

		printf("Case #%d: %d\n", c + 1, result);
	}

	return 0;
}