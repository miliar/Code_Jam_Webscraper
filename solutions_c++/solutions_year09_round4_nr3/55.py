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

////////////////////////////////////////////

int tc, ntc;
int n, m;

bool conf[100][100];
vi ar[100];

bool check_conf(const vi& a, const vi& b)
{
	int i;
	for (i=0; i<m-1; i++)
	{
		if (a[i] >= b[i] && a[i+1] <= b[i+1]) return true;
		if (a[i] <= b[i] && a[i+1] >= b[i+1]) return true;
	}
	return false;
}

bool con[100][100];
void create_graph()
{
	memset(con, 0, sizeof(con));
	int i, j, k;
	for (i=0; i<n; i++) for (j=i+1; j<n; j++) if (!conf[i][j])
	{
		con[i][j] = true;
/*
		for (k=i+1; k<j; k++) if (!conf[i][k] && !conf[k][j]) break;
		if (k == j) 
		{
			con[i][j] = true;
			printf("%d %d\n", i, j);
		}
*/
	}
}

int matched[100];
bool used[100];

bool match(int x)
{
	int i;
	for (i=0; i<n; i++) if (con[x][i] && !used[i])
	{
		used[i] = true;
		if (matched[i] == -1 || match(matched[i]))
		{
			matched[i] = x;
			return true;
		}
	}
	return false;
}

int proc()
{
	memset(matched, -1, sizeof(matched));

	int i;
	int m = 0;
	for (i=0; i<n; i++)
	{
		memset(used, 0, sizeof(used));
		m += match( i );
	}

	int res = n - m;
	return res;
}

int main()
{
	FILE* fi = fopen("C-large.in", "r");
	FILE* fo = fopen("C-large.out", "w");

	fscanf(fi, "%d", &ntc);
	for (tc=1; tc<=ntc; tc++)
	{
		fscanf(fi, "%d %d", &n, &m);
		int i, j;
		for (i=0; i<n; i++)
		{
			ar[i].clear();
			int a;
			for (j=0; j<m; j++) 
			{				
				fscanf(fi, "%d", &a);
				ar[i].push_back( a );
			}
		}
		sort(ar, ar+n);

		memset(conf, 1, sizeof(conf));
		for (i=0; i<n; i++) for (j=i+1; j<n; j++)
		{
			conf[i][j] = conf[j][i] = check_conf(ar[i], ar[j]);
			//printf("%d %d : %d\n", i, j, conf[i][j]);
		}

		create_graph();
		int res = proc();
		printf("Case #%d: %d\n", tc, res);
		fprintf(fo, "Case #%d: %d\n", tc, res);
	}

	fclose(fi); fclose(fo);
}