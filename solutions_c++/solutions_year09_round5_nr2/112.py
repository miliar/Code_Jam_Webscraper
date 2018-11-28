#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int n, t;
string P;
vector< string > word;
vector< int > c[105];
int sol[105];

int calc(string A, string B)
{
	cout << A << " : " << B << endl;
	vector<int> c(26, 0);
	for (int i = 0; i < A.size(); ++i)
		c[ A[i] - 'a' ]++;
	int ret = 0;
	int add = 1;
	
	B += "+";
	for (int i = 0; i < B.size(); ++i)
	{
		if (B[i] == '+')
		{
			ret = (ret + add) % 10009;
			add = 1;
		}
		else
		{
			add = add * c[ B[i] - 'a' ];
			add %= 10009;
		}
	}
	return ret;
}

void go(int dpt, vector<int> cc)
{
	int ret = 0;
	int add = 1;
	for (int i = 0; i < P.size(); ++i)
	{
		if (P[i] == '+')
		{
			ret = (ret + add) % 10009;
			add = 1;
		}
		else
		{
			add = add * cc[ P[i] - 'a' ];
			add %= 10009;
		}
	}

	sol[dpt] = (sol[dpt] + ret) % 10009;

	if (dpt == t) return;

	vector<int> newb(26, 0);
	for (int i = 0; i < n; ++i)
	{
		newb = cc;
		for (int j = 0; j < 26; ++j)
			newb[j] += c[i][j];
		go(dpt + 1, newb);
	}
}

int main()
{
	int T;
	scanf("%d", &T);

	char tmp[1000];

	for (int cn = 1; cn <= T; ++cn)
	{
		word.clear();
		printf("Case #%d:", cn);
		scanf("%s %d", tmp, &t);
		P = tmp;
		P += "+";

		scanf("%d", &n);

		memset(sol, 0, sizeof(sol));
		for (int i = 0; i < n; ++i)
		{
			scanf("%s", tmp);
			word.push_back(tmp);

			c[i].assign(26, 0);
			for (int j = 0; j < word[i].size(); ++j)
				c[i][ word[i][j] - 'a' ]++;
//			cout << calc(tmp, P) << ' ';
		}

		go( 0, vector<int> (26, 0) );

		for (int i = 1; i <= t; ++i)
			printf(" %d", sol[i]);
		printf("\n");
	}
}

