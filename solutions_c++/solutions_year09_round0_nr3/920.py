#include <vector>
#include <string>
#include <iostream>
#include <iomanip>
#include <memory.h>
#include <assert.h>
#include <stdlib.h>
using namespace std;

char pat[] = "welcome to code jam";

int main()
{
	int n;
	cin >> n;
	string el;
	getline(cin, el);
	for(int i = 0; i < n; ++i)
	{
		string s;
		getline(cin, s);
		int v[2][20];
		memset(v, 0, sizeof(v));

		for(int j = s.size() - 1; j >= 0; --j)
		{
			v[(j & 1) ^ 1][19] = 1;
			for(int p = 0; p < 19; ++p)
			{
				if(s[j] == pat[p])
					v[j & 1][p] = (v[(j & 1) ^ 1][p] + v[(j & 1) ^ 1][p + 1]) % 10000;
				else
					v[j & 1][p] = v[(j & 1) ^ 1][p];
			}
		}

		cout << "Case #" << (i + 1) << ": " << setw(4) << setfill('0') << v[0][0] << endl;
	}
	return 0;
}
