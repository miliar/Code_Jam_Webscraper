#include <iostream>
#include <string>
#include <fstream>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");
#define cin fin
#define cout fout

char inputs[100];

int num[10];
int other[10];

int main()
{
	int t;

	cin >> t;
	for (int cases = 1; cases <= t; cases++)
	{
		cin >> inputs;

		int m = strlen(inputs);

		memset(num, 0, sizeof(num));
		for (int i = 0; i < m; i++)
			num[inputs[i] - '0']++;

		bool flag = false;
		for (int i = m-1; i > 0; i--)
		if (inputs[i] > inputs[i-1])
		{
			int k = i;
			for (int j = i+1; j < m; j++)
				if (inputs[j] > inputs[i-1] && inputs[j] < inputs[k])
					k = j;

			memset(other, 0, sizeof(other));
			for (int j = i; j < m; j++)
				if (j != k) other[inputs[j] - '0']++;
			other[inputs[i-1] - '0']++;

			inputs[i-1] = inputs[k];
			int h = i;
			for (int j = 0; j < 10; j++)
				for (int g = 0; g < other[j]; g++)
				{
					inputs[h] = '0' + j;
					h++;
				}

			flag = true;
			break;
		}

		if (flag == false)
		{
			num[0]++;

			memset(inputs, 0, sizeof(inputs));

			for (int j = 1; j < 10; j++)
				if (num[j] > 0)
				{
					inputs[0] = '0' + j;
					num[j]--;
					break;
				}

			int h = 1;
			for (int j = 0; j < 10; j++)
				for (int g = 0; g < num[j]; g++)
				{
					inputs[h] = '0' + j;
					h++;
				}
		}

		cout << "Case #" << cases << ": " << inputs << endl;
	}

	return 0;
}