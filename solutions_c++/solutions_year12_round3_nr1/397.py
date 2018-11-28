#include <iostream>
#include <fstream>
#include <vector>

int met[1010];
bool res;
int a[1020][520] = {0};

void rec(int x)
{
	if (res)
		return;
	if (met[x] != 0)
	{
		res = true;
		return;
	}
	met[x] = 1;
	for (int i = 1; i <= a[x][0]; ++i)
		rec(a[x][i]);
}

int main()
{
	std::ifstream input("input_a.txt");
	std::ofstream output("output_a.txt");
	int t;
	input >> t;
	for (int tt = 0; tt < t; ++tt)
	{
		int n;
		input >> n;
		memset(a, 0, sizeof(a));
		//int a[52][52] = {0};
		for (int i = 1; i <= n; ++i)
		{
			input >> a[i][0];
			for (int j = 1; j <= a[i][0]; ++j)
				input >> a[i][j];
		}
		
		for (int i = 1; i <= n; ++i)
		{
			memset(met, 0, sizeof(met));
			res = false;
			rec(i);
			if (res)
				break;
		}
		if (res)
			output << "Case #" << tt+1 << ": Yes" << std::endl;
		else
			output << "Case #" << tt+1 << ": No" << std::endl;
	}
	input.close();
	output.close();
	return 0;
}