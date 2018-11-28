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

using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define FOR(i,n) for (i = 0; i < (n); i++)
#define FORI(i,a,b) for (i = (a); i <= (b); i++)
#define FORD(i,a,b) for (i = (a); i >= (b); i--)
#define ZERO(a) memset(a, 0, sizeof(a))
#define MINUS(a) memset(a, -1, sizeof(a))
#define DBG(a) cerr << a << endl;
#define DEBUG 1
#define PB push_back

int tc, n;

int main()
{
	int i,j,k,t;
	vector<int> v;
	char c[100];

	scanf("%d", &tc);
	FOR(t, tc)
	{
		scanf("%s", c);
		v.clear();
		FOR(i, strlen(c)) v.PB(c[i] - '0');

/*		while (n > 0)
		{
			v.PB(n % 10);
			n /= 10;
		}*/
//		reverse(v.begin(), v.end());

		j = 0; 
		FORD (i, v.size() - 1, 0) 
		{
			if (j > v[i]) break;
			j = v[i];
		}
//		printf("break found at %d\n", i);
		if (i == -1) // need to add 0!
		{
			v.PB(0);
			sort(v.begin(), v.end());
			FOR(j, v.size()) if (v[j]) break;
			i = v[j]; v[j] = v[0]; v[0] = i;
		}
		else
		{
			vector<int> tmp;
			FORI(k, i + 1, v.size() - 1) if (v[i] >= v[k]) break;
			j = v[i]; v[i] = v[k - 1]; v[k - 1] = j;
			FORI(k, i + 1, v.size() - 1) tmp.PB(v[k]);
			sort(tmp.begin(), tmp.end());
			FORI(k, i + 1, v.size() - 1) v[k] = tmp[k - i - 1];
		}
		
		printf("Case #%d: ", t+1);
		FOR(i, v.size()) printf("%d", v[i]);
		printf("\n");
	}
	return 0;
}

