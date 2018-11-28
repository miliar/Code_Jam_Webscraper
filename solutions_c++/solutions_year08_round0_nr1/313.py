#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <iostream>
#include <string>

using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define FOR(i,n) for (i = 0; i < (n); i++)
#define FORI(i,a,b) for (i = (a); i <= (b); i++)
#define FORD(i,a,b) for (i = (a); i >= (b); i--)
#define ZERO(a) memset(a, 0, sizeof(a))
#define MINUS(a) memset(a, -1, sizeof(a))

#define MAXN 128

int n, m, tc;
map<string, int> table;
int used[MAXN];

int main()
{
	int i,j,k,l,ans;
	string line, prev;
	char tmp[128];
	
	scanf("%d", &tc);
	FOR(i, tc)
	{
		scanf("%d\n", &n);
		FOR(j, n)
		{
			gets(tmp);
			line = string(tmp);
//			cerr << line << endl;
			table[line] = j;
		}
		l = ans = 0;
		scanf("%d\n", &m);
//		cerr << m << endl;
		ZERO(used);
		prev = "";
		
		FOR(j, m)
		{
			gets(tmp);
			if (i == 0) cerr << tmp << endl;
			line = string(tmp);
			k = table[line];
			if (!used[k] && (l != 0 || line != prev)) { used[k] = 1; l++; }
			if (l == n) { ans++; l = 1; ZERO(used); used[k] = 1; if (i == 0) fprintf(stderr, "change\n");}
			prev = line;
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}

