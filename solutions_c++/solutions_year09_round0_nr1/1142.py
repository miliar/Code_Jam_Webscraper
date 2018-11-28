#include <iostream>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <vector>
#include <set>
#include <string>
#define ldb long double
#define LL long long
#define sqr(a) (a) * (a)
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
const ldb LDINF = 9128739847123.00;
const ldb eps = 1e-9;
const int INF = 2147483647 / 2;
using namespace std;

int possible[30];
string s[5210], str;
int L, D, N;

void Load()
{
	cin >> L >> D >> N;
	int i;
	string str;
	int j, k;
	for (i = 1; i <= D; i++)
	{
		cin >> s[i];
	}
}

void Solve()
{
	int i;
	int j, k;
	LL result = 0, cur;
	for (i = 1; i <= N; i++)
	{
		cin >> str;
		k = 0;
		for (j = 0; j < str.size(); j++)
		{
			if (str[j] == '(')
			{
				k++;
				possible[k] = 0;
				j++;
				while (str[j] != ')')
				{
					possible[k] |= (1 << (str[j] - 'a'));
					j++;
				}
			}
			else
			{
				k++;
				possible[k] = 0;
				possible[k] |= 1 << (str[j] - 'a');
			}
		}
		result = 0;
		for (j = 1; j <= D; j++)
		{
			cur = 1;
			for (k = 1; k <= L; k++)
			{
				cur *= (possible[k] & (1 << (s[j][k - 1] - 'a'))) > 0;
			}
			result += cur;
		}
		cout << "Case #" << i << ": " << result << "\n";
	}
}


#define file "a"
int main()
{
	freopen(file".in", "rt", stdin);
	freopen(file".out", "wt", stdout);
	Load();
	Solve();
	return 0;
}