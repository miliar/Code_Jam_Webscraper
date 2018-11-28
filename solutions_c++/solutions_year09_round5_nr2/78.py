#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <assert.h>
using namespace std;

typedef long long LL;
typedef vector <string> vs;
typedef vector <int> vi;
typedef vector <LL> vll;
typedef vector <double> vd;
typedef pair <int,int> pii;


vs token(string s, string d)
{
	string t;
	vs res;
	int pos;
	while (true)
	{
		pos = s.find(d);
		if (pos == -1) break;
		t = s.substr(0, pos);
		s = s.substr(pos+d.length());
		if (t != "") res.push_back( t );
	}
	if (s != "") res.push_back( s );
	return res;
}

vs token(string s)
{
	return token(s, " ");
}

vi s2vi(string s, string d)
{
	vs tvs = token(s, d);
	vi res;
	int i;
	for (i=0; i<tvs.size(); i++) res.push_back( atoi(tvs[i].c_str()) );
	return res;
}

vi s2vi(string s)
{
	return s2vi(s, " ");
}

///////////////////////////

int tc, ntc;
char buf[10000];
int K;

#define MOD 10009

vs terms;
vs ar;
int n;
int val[100];
int vres[100];

int cnt1[100][26];
int cnt[100];

int xid[26];
int imp[26];
int nimp;

void proc1(int x)
{
	int i, j;
	int res = 0;
	for (i=0; i<terms.size(); i++)
	{
		int x = 1;
		for (j=0; j<terms[i].length(); j++)
			x = x * cnt[ terms[i][j]-'a' ] % MOD;
		res = (res + x) % MOD;
	}
	vres[x] += res;
	vres[x] %= MOD;
}

inline void add_word(int id)
{
	int i;
	for (i=0; i<nimp; i++)
		cnt[imp[i]]+=cnt1[id][imp[i]];
}

inline void rem_word(int id)
{
	int i;
	for (i=0; i<nimp; i++)
		cnt[imp[i]]-=cnt1[id][imp[i]];
}

void dfs(int num)
{
	if (num > K) return;
	if (num != 0)
	{
		proc1( num );
	}

	int i, j;
	for (i=0; i<n; i++)
	{
		add_word( i );
		dfs(num+1);
		rem_word( i );
	}
}

int main()
{
	FILE* fi = fopen("B-small1.in", "r");
	FILE* fo = fopen("B.out", "w");

	fscanf(fi, "%d", &ntc);
	int i, j;
	for (tc = 1; tc <= ntc; tc++)
	{
		fscanf(fi, "%s %d", buf, &K);
		terms = token(buf, "+");

		fscanf(fi, "%d", &n);
		ar.clear();
		
		nimp = 0;
		memset(xid, -1, sizeof(xid));
		for (i=0; i<terms.size(); i++)
		{
			for (j=0; j<terms[i].length(); j++)
			{
				int c = terms[i][j] - 'a';
				if (xid[c] != -1) continue;
				imp[nimp] = c;
				xid[c] = nimp++;
			}
		}


		memset(cnt1, 0, sizeof(cnt1));
		for (i=0; i<n; i++)
		{
			fscanf(fi, "%s", buf);
			ar.push_back( buf );
			for (j=0; j<ar[i].length(); j++)
				cnt1[i][ ar[i][j]-'a' ]++;
		}

		

		memset(vres, 0, sizeof(vres));
		memset(cnt, 0, sizeof(cnt));
		dfs( 0 );

		printf("Case #%d:", tc);
		for (i=1; i<=K; i++) printf(" %d", vres[i]);
		printf("\n");

		fprintf(fo, "Case #%d:", tc);
		for (i=1; i<=K; i++) fprintf(fo, " %d", vres[i]);
		fprintf(fo, "\n");
	}



	fclose(fi); fclose(fo);
}