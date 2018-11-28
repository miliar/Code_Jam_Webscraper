#include <stdio.h>
#include <vector>

using namespace std;

int main()
{
	FILE *in = fopen("A-large.in", "r");
	FILE *out = fopen("A.out", "w");

	int l,d,n;
	fscanf(in, "%d %d %d", &l, &d, &n);

	vector<string> v;
	for(int i = 0; i < d; i++)
	{
		char buf[10000];
		fscanf(in, "%s", buf);
		v.push_back(buf);
	}

	for(int i = 1; i <= n; i++)
	{
		int res = 0;

		vector<vector<bool> > word;

		char buf[10000];
		fscanf(in, "%s", buf);

		int ind = 0;
		while(buf[ind])
		{
			if (buf[ind] == '(')
			{
				ind++;
				word.push_back(vector<bool>(26));
				while(buf[ind] != ')')
				{
					word.back()[buf[ind]-'a'] = true;
					ind++;
				}
				ind++;
			}
			else
			{
				word.push_back(vector<bool>(26));
				word.back()[buf[ind]-'a'] = true;
				ind++;
			}
		}

		for(int j = 0; j < v.size(); j++)
		{
			bool good = true;
			for(int k = 0; k < v[j].size(); k++)
			{
				if (!word[k][v[j][k]-'a'])
				{
					good = false;
					break;
				}
			}
			if (good)
				res++;
		}

		fprintf(out, "Case #%d: %d\n", i, res);
	}
}
