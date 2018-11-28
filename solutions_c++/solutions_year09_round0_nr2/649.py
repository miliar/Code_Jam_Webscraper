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

#define NMAX 1000

int h[NMAX][NMAX];

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

map<pair<int,int>, vector<pair<int,int> > > in;
set<pair<int,int> > used;

char r[NMAX][NMAX];

void dfs(const pair<int,int>& v, set<pair<int,int> >& cp)
{
	if (used.count(v) == 0)
    {
    	used.insert(v);
        cp.insert(v);

        forn(i, in[v].size())
        {
        	pair<int,int> w = in[v][i];
            dfs(w, cp);
        }
    }
}

int main()
{
	freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);

    int tt;

    cin >> tt;

    forn(t, tt)
    {
    	int n, m;
        cin >> n >> m;

        forn(i, n)
        	forn(j, m)
            	cin >> h[i][j];

        in.clear();
        used.clear();

        set<pair<int,int> > from;

        forn(i, n)
        {
        	forn(j, m)
            {
            	int nx = -1;
                int ny = -1;

                int nh = INT_MAX;

                forn(d, 4)
                {
                	int wx = i + dx[d];
                	int wy = j + dy[d];

                    if (wx >= 0 && wx < n && wy >= 0 && wy < m)
                    {
                    	if (h[i][j] > h[wx][wy] && h[wx][wy] < nh)
                        {
                        	nx = wx;
                            ny = wy;
                            nh = h[wx][wy];
                        }
                    }
                }

                if (nx != -1)
                {
                	//cerr << "(" << nx << "," << ny << ") -> (" << i << "," << j << ")" << endl;
                	in[make_pair(nx, ny)].push_back(make_pair(i, j));
                }
                else
                {
                	from.insert(make_pair(i, j));
                }
            }
        }

        //cerr << from.size() << endl;

        vector<set<pair<int,int> > > cps;

        forn(i, n)
        	forn(j, m)
            	if (from.count(make_pair(i, j)))
                {
                	set<pair<int,int> > s;
                	dfs(make_pair(i, j), s);
                    cps.push_back(s);
                }

        sort(cps.begin(), cps.end());

        vector<string> result;

        assert(cps.size() <= 26);

        forn(i, cps.size())
        {
        	set<pair<int,int> >& s = cps[i];

            for (set<pair<int,int> > :: iterator it = s.begin(); it != s.end(); it++)
            {
            	r[it->first][it->second] = 'a' + i;
            }
        }

        cout << "Case #" << t + 1 << ":" << endl;

        forn(i, n)
        {
        	forn(j, m)
            {
            	cout << r[i][j] << " ";
            }
            cout << endl;
        }
    }

    fclose(stdin);
    fclose(stdout);
	return 0;
}
