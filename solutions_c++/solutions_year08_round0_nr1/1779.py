#include <fstream>
#include <string>
#include <sstream>
#include <cstring>

using namespace std;

ifstream cin("data.in");
ofstream cout("data.out");

int n, q, m;
string names[100];
string query[1000];
int qs[1000];
int opt[1000][100];


void init()
{
	cin >> n;
	string data;
	getline(cin, data);
	for (int i = 0; i < n; i++)
	{
		getline(cin, data);
		names[i] = data;
	}
	cin >> q;
	getline(cin, data);
	for (int i = 0; i < q; i++)
	{
		getline(cin, data);
		query[i] = data;
		for (int j = 0; j < n; j++)
			if (query[i] == names[j])
				qs[i] =j;
	}
	memset(opt, 0, sizeof opt);
	for (int i = 0; i < q; i++)
		for (int j = 0; j < n; j++)
			opt[i][j] = 100000;
		for (int j = 0; j < n; j++)
			if (qs[0] != j)
				opt[0][j] = 0;
}

int dp()
{
	for (int i = 1; i < q; i++)
		for (int j = 0; j < n; j++)
		if (qs[i-1] != j)
			for (int k = 0; k < n; k++)
			if (qs[i] != k)
			{
				if (k != j)
				if (opt[i][k] > opt[i-1][j] + 1)
					opt[i][k] = opt[i-1][j] + 1;
				if (k == j)
					if (opt[i][k] > opt[i-1][j])
						opt[i][k] = opt[i-1][j];
			}
	int tmp = 10000;
	for (int i = 0; i < n; i++)
		if (opt[q-1][i] < tmp)
			tmp = opt[q-1][i];
	return tmp;
}

int main()
{
	cin >> m;
	for (int i = 0; i < m; i++)
	{
		init();
		cout << "Case #" << i+1 << ": " << dp() << endl;
	}
}
