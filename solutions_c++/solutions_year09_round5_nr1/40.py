#include <ctime>
#include <queue>
#include <cassert>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <cassert>
#include <utility>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)

int n, m;
vector<string> f;

typedef pair<int,int> pt;
long long a, b;
int answer;
int size;

long long pos(vector<pt> p)
{
	size = p.size();
	long long result = 0;
	sort(p.begin(), p.end());
    forn(i, p.size())
    {
    	long long t = (p[i].first) | ((p[i].second) * 16);
        result |= (t << (8 * i));
    }
    return result;
}

vector<pt> pos(long long p)
{
	vector<pt> result;

	forn(i, size)
    {
    	int t = (p >> (i * 8)) & 255;
    	result.push_back(pt(t & 15, t >> 4));    
    }

    return result;
}

void readData()
{
	cin >> n >> m;
    f.resize(n);
    forn(i, n)
    {
    	string s;
        cin >> s;
        f[i] = s;
    }

    vector<pt> from;
    vector<pt> to;

    forn(i, n)
    	forn(j, m)
        {
        	if (f[i][j] == 'o')
            {
            	from.push_back(pt(i, j));
            }
        	if (f[i][j] == 'x')
            {
            	to.push_back(pt(i, j));
            }
        	if (f[i][j] == 'w')
            {
            	from.push_back(pt(i, j));
            	to.push_back(pt(i, j));
            }
            if (f[i][j] != '#')
            	f[i][j] = '.';
        }

    a = pos(from);
    b = pos(to);
}

char w[100][100];

bool ad(pt a, pt b)
{
	return abs(a.first - b.first) + abs(a.second - b.second) == 1;
}

int z[10][10];

bool isGood(vector<pt> p)
{
	forn(i, size)
    	forn(j, size)
        	z[i][j] = (i == j) || ad(p[i], p[j]);

    forn(t, size)
    	forn(i, size)
        	forn(j, size)
            	z[i][j] = z[i][j] | (z[i][t] & z[t][j]);

    forn(i, size)
    	forn(j, size)
        	if (!z[i][j])
            	return false;
                
    return true;
}

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0,  1, -1};

bool ok(int x, int y)
{
	return 0 <= x && x < n && 0 <= y && y < m;
}

void solve()
{
	map<long long, int> d;
    d[a] = 0;

    queue<pair<long long, bool> > q;
    q.push(make_pair(a, true));

    while (!q.empty())
    {
    	if (d.count(b))
        {
        	answer = d[b];
            return;
        }

        pair<long long, bool> c = q.front();
        q.pop();

        forn(i, n)
        	forn(j, m)
            	w[i][j] = '.';

        vector<pt> now = pos(c.first);

        forn(i, size)
        	w[now[i].first][now[i].second] = 'z';

        forn(i, size)
        {
        	forn(j, 4)
            {
            	int sx = now[i].first + dx[j];
            	int sy = now[i].second + dy[j];

            	int fx = now[i].first + dx[j ^ 1];
            	int fy = now[i].second + dy[j ^ 1];

                if (ok(sx, sy) && ok(fx, fy) && w[sx][sy] == '.' && w[fx][fy] == '.' && f[sx][sy] == '.' && f[fx][fy] == '.')
                {
                	now[i].first += dx[j];
                	now[i].second += dy[j];

                    if (!c.second && isGood(now))
                    {
                    	long long res = pos(now);
                        if (d.count(res) == 0)
                        {
                        	d[res] = d[c.first] + 1;
                            q.push(make_pair(res, true));
                        }
                    }

                    if (c.second)
                    {
                    	long long res = pos(now);
                        if (d.count(res) == 0)
                        {
                        	d[res] = d[c.first] + 1;
                            q.push(make_pair(res, isGood(now)));
                        }
                    }

                	now[i].first -= dx[j];
                	now[i].second -= dy[j];
                }
            }
        }
    }

    answer = -1;
}

int main(int argc, char* argv[])
{
	freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);

	int beginIndex = atoi(argv[1]);
	int endIndex = atoi(argv[2]);

	int testCount;

	string s;
	getline(cin, s);
	sscanf(s.c_str(), "%d", &testCount);
	
	for (int tt = 1; tt <= testCount; tt++)
	{
		readData();

		if (beginIndex <= tt && tt <= endIndex)
		{
            cerr << "[" << clock() << "]\tRunning test " << tt << " (" << tt - beginIndex + 1
                << " out of " << endIndex - beginIndex + 1 << ")..." << endl;
            int from = clock();

            solve();

            cerr << "\tCompleted in " << clock() - from << " ms." << endl;

			printf("Case #%d: %d", tt, answer);
            printf("\n");
		}
	}

	fclose(stdin);
    fclose(stdout);
	
    return 0;
}
