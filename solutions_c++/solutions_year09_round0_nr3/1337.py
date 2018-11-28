#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>

using namespace std;

#define fore(i,a) for(int i = 0; i < (a); i++)
#define fort(i,a) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define x first
#define y second

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef long long ll;

#define err(...)
#define err(...) fprintf(stderr, __VA_ARGS__)

char s[505];
char t[21] = "#welcome to code jam";
int d[505][22];

void test()
{
	int n,m=20;
	s[0] = '*';
	scanf(" %[^\n]", &s[1]);
	for(n=0;s[n];n++) ;
	fore(i,n) fore(j,m) d[i][j] = 0;
	fore(i,n) d[i][0] = 1;
	for(int j = 1; j < m; j++)
	{
		for(int i = 1; i < n; i++)
		{
			d[i][j] = d[i-1][j];
			if(t[j] == s[i]) d[i][j] += d[i-1][j-1];
			if(d[i][j] >= 10000) d[i][j] -= 10000;
		}
	}
	printf("%04d\n", d[n-1][m-1]);
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++)
	{
		printf("Case #%d: ", tt);
		test();
	}
}
