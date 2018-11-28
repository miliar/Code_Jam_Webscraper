#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

#define mset(c, val) memset((c), (val), sizeof((c)))
#define all(v) v.begin(), v.end()
#define INF 1000000000
#define EPS 1e-10

typedef vector<int> vi;
typedef long long lint;

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	char s[65536];
	char ch[65536];

	int test, tnum;
	int answer;

	int k, n;
	vi perm;

	void readdata()
	{
		fin >> k;
		fin >> s;
		n = (int)strlen(s);
	}

	void outputdata()
	{
		fout << "Case #" << (test + 1) << ": " << answer << endl;
	}

	void init()
	{
		answer = n;
		perm.clear();
		for (int i = 0; i < k; i++)
            perm.push_back(i);		
	}

	void run()
	{
		int parts = n / k;
		do {
			for (int i = 0; i < parts; i++) {
				for (int j = 0; j < k; j++) {
					ch[i * k + j] = s[i * k + perm[j]];
				}
			}
			int cur = 1;
			for (int i = 1; i < n; i++) {
				if (ch[i] != ch[i - 1])
					cur++;
			}
			answer = min(answer, cur);
		} while (next_permutation(all(perm)));
	}

int main()
{
    fin >> tnum;
	for (test = 0; test < tnum; test++) {
		readdata();
		init();
		run();
		outputdata();
	}
	return 0;
}
