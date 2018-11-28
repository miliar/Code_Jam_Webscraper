#include <iostream>
#include <math.h>
#include <string>
#include <list>

using namespace std;

void swap(int *a, int *b)
{
  int t=*a; *a=*b; *b=t;
}

void sort(int arr[], int beg, int end)
{
  if (end > beg + 1)
  {
    int piv = arr[beg], l = beg + 1, r = end;
    while (l < r)
    {
      if (arr[l] <= piv)
        l++;
      else
        swap(&arr[l], &arr[--r]);
    }
    swap(&arr[--l], &arr[beg]);
    sort(arr, beg, l);
    sort(arr, r, end);
  }
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int N, min, mini, j;
	scanf("%d", &N);
	char snum[22];
	int num[22];
	int len;

	for(int n=1; n<=N; n++)
	{
		scanf ("%s", &snum);
		len = strlen(snum);

		for (int i = 0; i < len; i++)
			num[i] = snum[i] - '0';

		for (int i = len-1; i > 0; i--)
			if (num[i] > num[i-1])
			{
				min = num[i];
				mini = i;

				for (j = i; j < len; j++)
					if (num[j] < min && num[j] > num[i-1])
					{
						min = num[j];
						mini = j;
					}

				swap (&num[i-1], &num[mini]);
				sort (num, i, len);

				break;
			}

		bool vienodas = true;
		for (int i = 0; i < len; i++)
			vienodas = vienodas && num[i] == snum[i] - '0';

		if (vienodas)
		{
			sort (num, 0, len);
			for (int i = len; i > 0; i--)
				num[i] = num[i-1];
			num[1] = 0;

			if (num[0] == 0)
			{
				int i = 1;
				while (num[i] == 0)
				{
					i++;
				}
				swap (&num[0], &num[i]);
			}

			len++;
		}

		cout << "Case #" << n << ": ";

		for (int i = 0; i < len; i++)
			cout << num[i];

		cout << endl;
	}

	return 0;
}