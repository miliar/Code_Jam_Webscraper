
#include <stdio.h>
#include <vector>


int cnr[501][501] = {0};

int main(int argc, char* argv[])
{

	for(int  n = 0 ; n <=500 ; n++)
	{
		cnr[n][0] = 1;
	}

	for(int  n = 1 ; n <=500 ; n++)
	{
		for(int r = 1 ; r <=n ; r++)
		{
			cnr[n][r] = (cnr[n-1][r-1]+cnr[n-1][r]) % 100003;
		}
	}

	freopen("c:\\C-small.in","r",stdin);
	freopen("C:\\C-small.out","w",stdout);


	int T = 0;

	scanf("%d", &T);

	std::vector<std::vector<int>> table;
	table.resize(501);
	for(int i = 2 ; i <= 500 ; i++)
	{
		table[i].resize(i,0);
	}
	table[2][1] = 1;

	for(int i = 3 ; i <= 500 ; i++)
	{
		int acculate = 1;
		table[i][1] = 1;

		// i in j-th position
		for(int j = 2 ; j < i ; j++)
		{
			// number j in k-th position
			for(int k = 1 ; k < j ; k++)
			{
				int n = i - j -1;
				int r = j - 2 - ( k- 1);

				if( n >= r && n >=0 && r >=0)
				{
					int b = cnr[n][r];
					int a = table[j][k]-table[j][k-1];
					acculate += a * b;
					acculate %= 100003;
				}
			}

			table[i][j] = acculate;
		}

	}

	for(int t = 0 ; t < T ; t++)
	{
		
		int n = 0 ;
		scanf("%d", &n);

//		ans = ans % 100003;
		printf("Case #%d: %d\n", t+1, table[n][n-1]);
	}

	return 0;
}