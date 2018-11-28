#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <list>
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
int n, m;
char mm[20][20];

LL enc(const vector<pii>& v)
{
	LL res = 0;
	int i;
	for (i=0; i<v.size(); i++)
	{
		res = res * n + v[i].first;
		res = res * m + v[i].second;
	}
	return res;
}

int nb;
void dec(LL x, vector<pii>& v)
{
	int i;
	for (i=nb-1; i>=0; i--)
	{
		v[i].second = x % m; x /= m;
		v[i].first = x % n; x /= n;
	}
}

LL target, start;

list<LL> q;
map<LL, int> val;

void add(LL st, int v)
{
	if (val.count(st)) return;
	val[st] = v;
	q.push_back(st);
}

int dy[] = {-1,0,1,0};
int dx[] = {0,1,0,-1};

bool isfree(const vector<pii>& cur, int id, int dir)
{
	int ny = cur[id].first + dy[dir];
	int nx = cur[id].second + dx[dir];
	if (ny < 0 || ny >= n || nx < 0 || nx >= m) return false;
	if (mm[ny][nx] == '#') return false;
	int i;
	for (i=0; i<nb; i++) if (cur[i].first == ny && cur[i].second == nx) return false;
	return true;
}

vector <pii> do_move(const vector<pii>& cur, int id, int dir)
{
	if (!isfree(cur, id, dir) || !isfree(cur, id, (dir+2)%4)) return vector<pii>();
	vector <pii> res = cur;
	res[id].first += dy[dir];
	res[id].second += dx[dir];
	sort(res.begin(), res.end());
	return res;
}

bool used[10];
int ff(const vector<pii>& cur, int id)
{
	int res = 1;
	used[id] = true;

	int i;
	for (i=0; i<nb; i++) if (!used[i])
	{
		int dist = abs(cur[i].first - cur[id].first) + abs(cur[i].second - cur[id].second);
		if (dist == 1) res += ff(cur, i);
	}
	return res;
}
bool calc_safe(const vector<pii>& cur)
{
	memset(used, 0, sizeof(used));
	if (ff(cur, 0) != nb) return false;
	return true;
}

int bfs()
{
	val.clear();
	q.clear();
	add(start, 0);
	
	int cval;

	vector<pii> pos(nb);
	vector <pii> npos;
	while (!q.empty())
	{
		LL cur = q.front(); q.pop_front();
		cval = val[cur];

		if (cur == target) return cval;

		dec(cur, pos);
		bool safe = calc_safe( pos );

		int i, j;
		for (i=0; i<nb; i++) for (j=0; j<4; j++)
		{
			npos = do_move(pos, i, j);
			if (!npos.empty())
			{
				if (safe || calc_safe(npos)) add(enc(npos), cval+1);
			}
		}
	}

	return -1;
}

int main()
{
	FILE* fi = fopen("A-large.in", "r");
	FILE* fo = fopen("A-large.out", "w");

	fscanf(fi, "%d", &ntc);
	int i, j;
	for (tc = 1; tc <= ntc; tc++)
	{
		fscanf(fi, "%d %d", &n, &m);
		for (i=0; i<n; i++)
			fscanf(fi, "%s", mm[i]);

		vector <pii> pos;
		target = 0;
		for (i=0; i<n; i++) for (j=0; j<m; j++) if (mm[i][j] == 'x' || mm[i][j] == 'w')
			{
				pos.push_back( pii(i,j) );
			}
		target = enc( pos );

		pos.clear();
		for (i=0; i<n; i++) for (j=0; j<m; j++) if (mm[i][j] == 'o' || mm[i][j] == 'w')
		{
			pos.push_back( pii(i,j) );
		}
		nb = pos.size();
		start = enc( pos );

		int res = bfs();
		printf("Case #%d: %d\n", tc, res);
		fprintf(fo, "Case #%d: %d\n", tc, res);
	}	

	fclose(fi); fclose(fo);
}