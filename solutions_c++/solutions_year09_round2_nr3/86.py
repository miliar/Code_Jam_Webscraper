#include <string>
#include <vector>
#include <queue>
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

map<int,string> z[20][20];
map<int,int> w[20][20];

struct state
{
	int row, col, v;
    string s;
};

int dx[] = {1, -1, 0,  0};
int dy[] = {0,  0, 1, -1};

#define MAX 155

int main()
{
	freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);

    int T;
    cin >> T;
    string s;

    forn(tt, T)
    {
    	cerr << tt << endl;
    	int n, m;
    	cin >> n >> m;
        getline(cin, s);
        vector<string> f;

        forn(i, n)
        {
        	getline(cin, s);
            f.push_back(s);
        }

        forn(i, 20)
        	forn(j, 20)
            	z[i][j].clear(),
                w[i][j].clear();

        forn(i, n)
        	forn(j, n)
            	if (isdigit(f[i][j]))
                	z[i][j][f[i][j] - '0'] = string(1, f[i][j]), w[i][j][f[i][j] - '0'] = 1;

        while (true)
        {
        	queue<state> q;

            forn(i, n)
            	forn(j, n)
                	for (map<int,string>::iterator it = z[i][j].begin(); it != z[i][j].end(); it++)
                    {
                    	state root;
                        root.row = i;
                        root.col = j;
                        root.v = it->first;
                        root.s = it->second;
                    	q.push(root);
                    }

            bool update = false;
            
            while (!q.empty())
            {
            	state c = q.front();
                s = c.s;
                q.pop();

                forn(i, 4)
                {
                	int mx = c.row + dx[i];
                    int my = c.col + dy[i];
                    if (mx >= 0 && mx < n && my >= 0 && my < n)
                		forn(j, 4)
                        {
                 			int nx = mx + dx[j];
                            int ny = my + dy[j];

                            if (nx >= 0 && nx < n && ny >= 0 && ny < n)
                            {
                            	int d = f[nx][ny] - '0';
                                int nv = c.v + (f[mx][my] == '+' ? d : -d);
                                string ns = s + f[mx][my] + f[nx][ny];

                                bool ok = false;

                                if (nv >= -MAX && nv <= MAX)
                                {
                                	if (z[nx][ny].count(nv) == 0)
                                    {
                                    	z[nx][ny][nv] = ns;
                                        w[nx][ny][nv] = ns.length();
                                        update = true;
                                        ok = true;
                                    }
                                    else
                                    {
                                    	if (w[nx][ny][nv] >= ns.length())
                                        {
                                        	string p = z[nx][ny][nv];
                                            if (((p.length() > ns.length()) || (p.length() == ns.length() && p > ns)))
                                            {
                                            	z[nx][ny][nv] = ns;
                                                w[nx][ny][nv] = ns.length();

                                                update = true;
                                                ok = true;
                                            }
                                        }
                                    }
                                }

                                if (ok)
                                {
                                	state nc;
                                    nc.row = nx;
                                    nc.col = ny;
                                    nc.v = nv;
                                    nc.s = s + f[mx][my] + f[nx][ny];
                                    q.push(nc);
                                }
                            }
                        }
                }
            }

            if (!update)
            	break;
        }

        cout << "Case #" << tt + 1 << ":" << endl;

        forn(i, m)
        {
        	int el;
        	cin >> el;

            string result;

            forn(i, n)
            	forn(j, n)
                {
                	string s = z[i][j][el];
                    if (s.length() > 0)
                    {
                    	if (result.length() == 0)
                        	result = s;
                        else
                        {
                        	if ((result.length() > s.length()) || (result.length() == s.length() && result > s))
                            {
                            	result = s;
                            }
                        }
                    }
                }

            cout << result << endl;
            result = "+" + result;

            int sum = 0;
            forn(i, result.length())
            {
            	if (result[i] == '+')
                	sum += (result[i + 1] - '0');
                else
                	sum -= (result[i + 1] - '0');
                i++;
            }

            assert(sum == el);
        }
    }

    fclose(stdin);
    fclose(stdout);
	return 0;
}


