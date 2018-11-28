#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"
#include "iostream"
#include "string"
#include "algorithm"
#include "vector"
#include "queue"
#include "map"

using namespace std;

#define all(s) s.begin(), s.end()



int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

int test_count;
cin >> test_count;
string s;
getline(cin, s);

const char phrase[] = "welcome to code jam";
int phrase_len = sizeof phrase;

for (int test = 0; test < test_count ; test++)
{
	getline(cin, s);
	int n = s.length();

	vector<vector<int> > d(phrase_len, vector<int> (n, 0));
	for (int i = 0; i < n ; i++)
	{
		if (i) d[0][i] = d[0][i-1];
		if (s[i] == phrase[0])
			d[0][i]++;
	}

	for (int i = 1; i < phrase_len ; i++)
	{
		for (int j = 1; j < n; j++)
		{
			d[i][j] = d[i][j-1];
			if (s[j] == phrase[i])
				d[i][j] += d[i-1][j];
			d[i][j] %= 1000;
		}
	}
	

	printf("Case #%d: %04d\n", test + 1, d[phrase_len - 2][n-1]);
}

}