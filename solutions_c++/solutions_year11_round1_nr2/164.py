#include <iostream>
#include <string>

using namespace std;

string D[10000];
int N;
string list;
bool F[10000];

int guess(string s)
{
	char x[10];
	int M = s.length();
	for (int i = 0; i < M; i++)
		x[i] = '_';
	int m = 0;
	for (int i = 0; i < N; i++)
		if (D[i].length() == M)
		{
			m++;
			F[i] = true;
		}
		else F[i] = false;
	int K = 0;
	int J = 0;
	while (m > 1)
	{
		bool f = false;
		int o = 0;
		for (int i = 0; i < N; i++)
			if (F[i])
			{
				for (int j = 0; j < D[i].length(); j++)
					if (D[i][j] == list[J]) 
					{
						o++;
						f = true;
						break;
					}
				if (f) break;
			}
		if (o == m) f = false;
		if (f)
		{
			K++;
			bool f = false;
			for (int i = 0; i < M; i++)				
				if (list[J] == s[i])
				{
					x[i] = s[i];
					f = true;
				}
			if (f) K--;
			for (int i = 0; i < N; i++)
				if (F[i])
				{
					for (int j = 0; j < M; j++)
						if ((D[i][j] == list[J] || x[j] == list[J]) && D[i][j] != x[j])
						{
							m--;
							F[i] = false;
							break;
						}
				}
		}
		J++;
	}
	return K;
}

string best()
{
	int K = -1;
	string S = "";
	for (int i = 0; i < N; i++)
	{
		int z = guess(D[i]);
		if (K < 0 || z > K)
		{
			S = D[i];
			K = z;
		}
	}
	return S;
}

void solve()
{
	int n, m;
	cin >> n >> m;
	N = n;
	for (int i = 0; i < n; i++)
		cin >> D[i];
	for (int i = 0; i < m; i++)
	{
		cin >> list;
		cout << best() << " ";
	}
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	int I = 0;
	cin >> t;
	while (t--)
	{
		I++;
		cout << "Case #" << I << ": ";
		solve();
		cout << endl;
	}
	return 0;
}