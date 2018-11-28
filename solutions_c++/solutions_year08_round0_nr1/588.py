#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

const int MAXS = 110;
const int MAXQ = 1010;
const int INF = 10000;

string in[MAXS];

int s, q;

void input()
{
	cin >> s;
	getchar();
	for (int i=1; i<=s; i++)
		getline(cin, in[i]);
}

int ans[MAXQ][MAXS];

void solve()
{
	cin >> q;
	getchar();
	for (int i=1; i<=q; i++)
	{
		string str;
		getline(cin, str);
		if (i == 1)
		{
			for (int j=1; j<=s; j++)
			{
				if (str == in[j])
					ans[i][j] = INF;
				else
					ans[i][j] = 0;	
			}	
		}
		else{
			for (int j=1; j<=s; j++)
			{
				if (str == in[j])
					ans[i][j] = INF;
				else{
					int tmp = ans[i-1][j];
					for (int k=1; k<=s; k++)
						if (k != j)
							tmp = min(tmp, ans[i-1][k]+1);
					ans[i][j] = tmp;	
				}	
			}
		}	
	}	
	int res = INF;
	for (int i=1; i<=s; i++)
		res = min(res, ans[q][i]);
	cout << res << endl;
}

int main()
{
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	int n;
	cin >> n;
	for (int kth=1; kth<=n; kth++)
	{
		input();
		cout << "Case #" << kth << ": ";
		solve();
	}	
	return 0;
}
