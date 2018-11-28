
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>

using namespace std;

#define PATH "c:\\jam3\\jam3\\"

int main(void)
{
    ifstream fin(PATH "s.in");
    ofstream fout(PATH "s.out");

    string line;

    int count;
    fin >> count;
    for (int t = 1; t <= count; ++t)
    {
		int P, K,L;
		fin >> P >> K >>L;

		int i;

		int ans = 0;
		vector<int> v;
		for (i  =0; i < L; ++i)
		{
			int b;
			fin >> b;
			v.push_back(b);
		}
		sort(v.begin(), v.end());

		for (i = 0; i < L; ++i)
		{
			int b = v[v.size() - i - 1];
			ans += b * ((i / K) + 1);
		}

        fout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}

