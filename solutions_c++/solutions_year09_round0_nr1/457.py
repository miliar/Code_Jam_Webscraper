#include <cstdio>
#include <vector>

using namespace std;

int n, l, d;
char dict[5000][16];

bool within(char what, vector<char> where)
{
	int i;
	for (i = 0; i < where.size(); i++)
		if (where[i] == what)
			return 1;
	return 0;
}

bool matches(int word, vector<char> poss[15])
{
	int i;
	for (i = 0; i < l; i++)
		if (!within(dict[word][i], poss[i]))
			return 0;
	return 1;
}

int main()
{
	FILE* input = fopen("alien.in", "r");
	FILE* output = fopen("alien.out", "w");
	fscanf(input, "%d %d %d", &l, &d, &n);
	int i, j, k;
	for (i = 0; i < d; i++)
		fscanf(input, "%s", &dict[i][0]);
	char temp[2000];
	for (i = 0; i < n; i++)
	{
		vector<char> poss[15];
		fscanf(input, "%s", &temp);
		k = 0;
		for (j = 0; j < l; j++)
		{
			if (temp[k] == '(')
			{
				k++;
				while (temp[k] != ')')
				{
					poss[j].push_back(temp[k]);
					k++;
				}
			}
			else
				poss[j].push_back(temp[k]);
			k++;
		}
		int t = 0; 
		for (j = 0; j < d; j++)
			t+=matches(j, poss);
		fprintf(output, "Case #%d: %d\n", i+1, t);
	}
}