#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <cmath>
#include <cassert>
using namespace std;

const int INF = 1 << 30;
const double EPS = 1e-9; 
const double PI = acos(-1.0);

const int M = 10000;

string S, T;

int mem[1024][1024];

int Go(int a, int b)
{
	if (a < 0 || b < 0)
		return 0;
	int& r = mem[a][b];
	if (r == -1)
	{
		if (S[a] == T[b])
		{
			r = (Go(a - 1, b - 1) + Go(a, b - 1)) % M;
			if (a == 0)
			{
				r = (r + 1) % M;
			}
		}
		else
		{
			r = Go(a, b - 1);
		}
	}
	return r;
}

void main()
{
#ifndef _DEBUG
	const string file_name = "C-large";
	freopen((file_name + ".in").c_str(), "r", stdin);
	freopen((file_name + ".out").c_str(), "w", stdout);
#endif

	//memset(mem, -1, sizeof(mem));
	//getline(cin, S);
	//getline(cin, T);
	//cout << Go(S.size() - 1, T.size() - 1) << endl;
	S = "welcome to code jam";
	int nn;
	cin >> nn;
	getline(cin, T);
	for (int jj = 1; jj <= nn; jj++)
	{
		memset(mem, -1, sizeof(mem));
		getline(cin, T);
		cout << "Case #" << jj << ": ";
		cout.width(4);
		cout.fill('0');
		cout << Go(S.size() - 1, T.size() - 1);
		cout << '\n';
	}

}
