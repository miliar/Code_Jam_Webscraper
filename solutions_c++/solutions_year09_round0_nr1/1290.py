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
//#define err(...) fprintf(stderr, __VA_ARGS__)

#define maxn 5010

int L, D;
char a[maxn][17];
char w[28*17];
bool v[17][27];

void test()
{
	fore(i,L) fore(j,26) v[i][j] = 0;
	scanf(" %s", w);
	int q = 0;
	for(int i = 0; w[i]; i++)
	{
		if(w[i] != '(') v[q++][w[i]-'a'] = 1;
		else
		{
			i++;
			while(w[i] != ')')
			{
				v[q][w[i]-'a'] = 1;
				i++;
			}
			q++;
		}
	}
	err("\n");
	fore(i,q)
	{
		err("%d : ", i);
		fore(j,26) if(v[i][j]) err("%c", 'a'+j);
		err("\n");
	}
	int res = 0;
	fore(j,D)
	{
		bool good = 1;
		fore(i,L) if(v[i][a[j][i]-'a'] == 0) good = 0;
		res += good;
	}
	printf("%d\n", res);
}

int main()
{
	int T;
	scanf("%d%d%d", &L, &D, &T);
	fore(i,D) scanf(" %s", a[i]);
	for(int tt = 1; tt <= T; tt++)
	{
		printf("Case #%d: ", tt); fflush(stdout);
		test();
	}
}
