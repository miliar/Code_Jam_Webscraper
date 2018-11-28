#include <cstdio>

int main()
{
	int cases;
	scanf("%d", &cases);

	for (int t = 1; t <= cases; ++t)
	{
		int rows;
		scanf("%d", &rows);

		int right[40];
		for (int i = 0; i < rows; ++i)
		{
			char row[41];
			scanf("%s", row);

			right[i] = -1;

			for (int k = rows - 1; k >= 0; --k)
			if (row[k] == '1') { right[i] = k; break; };
		};

		int swaps = 0;

		for (int pos = 0; pos < rows; ++pos)
		{
			int k; for (k = pos; right[k] > pos && k < rows; ++k);

			swaps += (k - pos); 
			//printf("swapping %d\n", (k - pos));

			int t = right[k];
			for (int i = k; i > pos; --i) right[i] = right[i - 1];
			right[pos] = t;
		};

		printf("Case #%d: %d\n", t, swaps);
	};
};
