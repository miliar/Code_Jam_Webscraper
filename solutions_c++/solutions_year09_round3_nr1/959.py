#include <iostream>
#include <math.h>
#include <list>
#include <map>

using namespace std;


int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int N;
	scanf("%d", &N);
	char line[62];
	list<char> dif;
	map<char, int> sk;
	typedef pair <char, int> Pair;
	list<int> sk2;
	list<int>::iterator Iter;
	int base, i;

	unsigned __int64 ten;

	for(int n=1; n<=N; n++)
	{
		cin >> line;
		dif.clear();
		sk.clear();
		sk2.clear();

		for (int i = 0; i < strlen(line); i++)
		{
			dif.push_back(line[i]);
			sk.insert(Pair(line[i], -1));
		}

		dif.sort();
		dif.unique();
		base = dif.size();
		if (base == 1)
			base = 2;

		int j = 1;
		for (i = 0; i < strlen(line); i++)
		{
			if (sk[line[i]] == -1)
			{
				sk[line[i]] = j;
				sk2.push_back(j);

				if (j == 1) j = 0;
				else if (j == 0) j = 2;
				else j++;
			}
			else
			{
				sk2.push_back(sk[line[i]]);
			}
		}

		ten = 0;
		int eil = sk2.size() - 1;

		for (Iter = sk2.begin(); Iter != sk2.end(); Iter++)
		{
			ten += *Iter * pow((double)base, (double)eil);
			eil--;
		}
			

		cout << "Case #" << n << ": " << ten << endl;
	}

	return 0;
}