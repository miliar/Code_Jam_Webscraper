#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

int c, d, n, k;
char mod[300][300], st[200];
bool def[300][300], op[300][300];

void solve()
{
	for(int i = 'A'; i <= 'Z'; i++)
		for(int j = 'A'; j <= 'Z'; j++)
		{
			def[i][j] = false;
			op[i][j] = false;
		}
	k = 0;
	cin >> c;	
	for(int i = 0; i < c; i++)
	{
		char a, b, c;
		cin >> a >> b >> c;
		def[a][b] = def[b][a] = true;
		mod[a][b] = mod[b][a] = c;
	}
	cin >> d;
	for(int i = 0; i < d; i++)
	{
		char a, b;
		cin >> a >> b;
		op[a][b] = op[b][a] = true;
	}
	cin >> n;
	for(int i = 0; i < n; i++)
	{
		char x;
		cin >> x;
		if (k > 0 && def[x][st[k - 1]])
			st[k - 1] = mod[x][st[k-1]];
		else
			st[k++] = x;
		for(int j = 0; j < k - 1; j++)
			if (op[st[j]][st[k - 1]])
			{
				k = 0;
				break;
			}
	}
	cout << "[";
	if (k > 0)
		cout << st[0];
	for(int i = 1; i < k; i++)
		cout << ", " << st[i];
	cout << "]";
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}