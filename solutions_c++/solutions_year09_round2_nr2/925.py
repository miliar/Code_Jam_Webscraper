#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

#define sqr(a) ((a) * (a))
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define pb push_back
#define mp make_pair

using namespace std;

typedef long double dd;

int main()
{
    freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d\n", &t);
	for(int itm = 1; itm <= t; ++itm)
	{
		string line;
		getline(cin, line);
		bool flag = false;
		for(int i = line.size() - 1; i > 0; --i)
		{
			if(line[i] > line[i - 1])
			{
				int minI = i, minV = line[i];
				for(int j = i; j < line.size(); ++j)
				{
					if(line[j] > line[i - 1] && line[j] < minV)
					{
						minI = j;
						minV = line[j];
					}
				}
				line[minI] ^= line[i - 1];
				line[i - 1] ^= line[minI];
				line[minI] ^= line[i - 1];
				sort(line.begin() + i, line.end());
				flag = true;
				break;
			}
		}
		if(!flag)
		{
			sort(line.begin(), line.end());
			if(line[0] == '0')
			{
				forn(j, line.size())
				{
					if(line[j] != '0')
					{
						line[0] ^= line[j];
						line[j] ^= line[0];
						line[0] ^= line[j];
						break;
					}
				}
			}
			line.insert(1, "0");
		}
		cout << "Case #" << itm << ": " << line << endl;
	}
	return 0;
}
