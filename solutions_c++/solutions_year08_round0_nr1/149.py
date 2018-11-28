#include<iostream>
#include<string>
#include<string.h>
#include<map>

using namespace std;

typedef map<string, int> MAP;

int s,q;

string engine[110];
int dp[1100][110];

char buf[2000];

int solve()
{
	int i,j,k;
	MAP hash;
	memset(dp, 0, sizeof(dp));
	cin >> s;
	cin.getline(buf, 200);
	
	for (i=0; i<s; i++) {
		cin.getline(buf, 200);
		engine[i] = buf;
		hash.insert(MAP::value_type(engine[i], i));
	}
	
	cin >> q;
	cin.getline(buf, 200);
	
	string query;
	
	for (i=0; i<q; i++) {
		cin.getline(buf, 200);
		query = buf;
		if (hash.find(query)!=hash.end()) {
			k = hash[query];
			int a=100000;
			for (j=0; j<s; j++) if (a>dp[i][j]) a=dp[i][j];
			for (j=0; j<s; j++)	{
				if (j==k) dp[i+1][j] = 100000;
				else dp[i+1][j] = min(dp[i][j], a+1);
			}
		}
		else memmove(dp[i+1], dp[i], sizeof(int)*s);
	}
	
	int a = 100000;
	for (i=0; i<s; i++) if (a>dp[q][i]) a=dp[q][i];
	
	cout << a << endl;
	
	return 0;
}

int main()
{
	int c, cc=0;
	cin >> c;
	while (c--) {
		cout << "Case #" << ++cc << ": ";
		solve();
	}
	
	return 0;
}
