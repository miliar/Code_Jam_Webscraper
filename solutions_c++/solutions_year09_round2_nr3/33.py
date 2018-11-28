#include <iostream>
#include <cstdio>
#include <vector>
#include <set>

using namespace std;

struct PII
{
	int x, y, v;
	PII(int x, int y, int v) : x(x), y(y), v(v) {}
};

bool operator== (const PII &a, const PII &b)
{
	return a.x == b.x && a.y == b.y && a.v == b.v;
}

bool operator< (const PII &a, const PII &b)
{
	if (a.x != b.x)
		return a.x < b.x;
	if (a.y != b.y)
		return a.y < b.y;
	return a.v < b.v;
}

typedef vector<int> VI;
typedef vector<PII> VPII;

const int MAX = 1024;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};
char sq[32][32];
VI tab[20][20][MAX];
VI good[20][20][MAX];

int main()
{
	int kases;
	scanf("%d", &kases);
	for (int kase = 1; kase <= kases; kase++)
	{
		int w, q;
		scanf("%d%d", &w, &q);
		for (int i = 0; i < w; i++)
			scanf("%s", &sq[i]);
		cout << "Case #" << kase << ":" << endl;
		cout.flush();
		while (q--)
		{
			int val, length;
			bool done = false;
			string res;
			VPII poss;
			int best = 10;
			scanf("%d", &val);
			set<PII> vis;
			for (int i = 0; i < w; i++)
				for (int j = 0; j < w; j++)
				{
					good[i][j][0].clear();
					if (isdigit(sq[i][j]))
					{
						tab[i][j][0].assign(1, sq[i][j]-'0');
						if (sq[i][j] - '0' == val)
						{
							cout << val << endl;
							vis.insert(PII(i,j,val));
							cout.flush();
							goto end;
						}
					}
					else
					{
						tab[i][j][0].clear();
					}
				}
			for (int l = 1; true; l++)
			{
				for (int i = 0; i < w; i++)
					for (int j = 0; j < w; j++)
					{
						tab[i][j][l].clear();
						good[i][j][l].clear();
						sort(tab[i][j][l-1].begin(), tab[i][j][l-1].end());
						tab[i][j][l-1].erase(unique(tab[i][j][l-1].begin(), tab[i][j][l-1].end()), tab[i][j][l-1].end());
//						cout << tab[i][j][l-1].size() << " ";
//						cout << "(" << i << "," << j << "):";
//						for (VI::const_iterator it = tab[i][j][l-1].begin(); it != tab[i][j][l-1].end(); ++it)
//							cout << " " << *it;
//						cout << endl;
					}
				if (done)
					break;
				for (int i = 0; i < w; i++)
					for (int j = 0; j < w; j++)
						if (isdigit(sq[i][j]))
							for (int d1 = 0; d1 < 4; d1++)
								for (int d2 = 0; d2 < 4; d2++)
								{
									int nx1 = i + dx[d1], ny1 = j + dy[d1];
									int nx2 = nx1 + dx[d2], ny2 = ny1 + dy[d2];
									if (nx1 < 0 || nx1 >= w || ny1 < 0 || ny1 >= w ||
											nx2 < 0 || nx2 >= w || ny2 < 0 || ny2 >= w)
										continue;
									int diff = (sq[nx1][ny1] == '+' ? 1 : -1) * (sq[nx2][ny2] - '0');
									for (VI::const_iterator it = tab[i][j][l-1].begin(); it != tab[i][j][l-1].end(); ++it)
									{
										if (vis.find(PII(nx2,ny2,*it + diff)) != vis.end())
											continue;
										vis.insert(PII(nx2,ny2,*it + diff));
										tab[nx2][ny2][l].push_back(*it + diff);
										if (*it + diff == val)
										{
											done = true;
											length = l;
										}
									}
								}
			}
			for (int i = 0; i < w; i++)
				for (int j = 0; j < w; j++)
					if (binary_search(tab[i][j][length].begin(), tab[i][j][length].end(), val))
						good[i][j][length].assign(1, val);
			for (int l = length-1; l >= 0; l--)
				for (int i = 0; i < w; i++)
					for (int j = 0; j < w; j++)
						if (isdigit(sq[i][j]))
							for (int d1 = 0; d1 < 4; d1++)
								for (int d2 = 0; d2 < 4; d2++)
								{
									int nx1 = i + dx[d1], ny1 = j + dy[d1];
									int nx2 = nx1 + dx[d2], ny2 = ny1 + dy[d2];
									if (nx1 < 0 || nx1 >= w || ny1 < 0 || ny1 >= w ||
											nx2 < 0 || nx2 >= w || ny2 < 0 || ny2 >= w)
										continue;
									int diff = (sq[nx1][ny1] == '+' ? 1 : -1) * (sq[nx2][ny2] - '0');
									for (VI::const_iterator it = tab[i][j][l].begin(); it != tab[i][j][l].end(); ++it)
										if (binary_search(good[nx2][ny2][l+1].begin(), good[nx2][ny2][l+1].end(), *it + diff))
											good[i][j][l].push_back(*it);
									sort(good[i][j][l].begin(), good[i][j][l].end());
									good[i][j][l].erase(unique(good[i][j][l].begin(), good[i][j][l].end()), good[i][j][l].end());
								}

			for (int i = 0; i < w; i++)
				for (int j = 0; j < w; j++)
					if (!good[i][j][0].empty())
						best = min(best, good[i][j][0][0]);
			assert(best < 10);
			for (int i = 0; i < w; i++)
				for (int j = 0; j < w; j++)
					if (!good[i][j][0].empty() && good[i][j][0][0] == best)
						poss.push_back(PII(i,j,best));
			res.push_back(best + '0');
			for (int l = 1; l <= length; l++)
			{
//				for (int i = 0; i < poss.size(); i++)
//					cout << "(" << poss[i].x << "," << poss[i].y << "," << poss[i].v << ")";
//				cout << endl;
				sort(poss.begin(), poss.end());
				poss.erase(unique(poss.begin(), poss.end()), poss.end());
//				cout << poss.size() << endl;
				VPII nposs;
				char bestop = '-';
				char bestval = '9' + 1;
				assert(!poss.empty());
				for (VPII::const_iterator it = poss.begin(); it != poss.end(); ++it)
				{
					for (int d1 = 0; d1 < 4; d1++)
						for (int d2 = 0; d2 < 4; d2++)
						{
							int nx1 = it->x + dx[d1], ny1 = it->y + dy[d1];
							int nx2 = nx1 + dx[d2], ny2 = ny1 + dy[d2];
							if (nx1 < 0 || nx1 >= w || ny1 < 0 || ny1 >= w ||
									nx2 < 0 || nx2 >= w || ny2 < 0 || ny2 >= w)
								continue;
							int diff = (sq[nx1][ny1] == '+' ? 1 : -1) * (sq[nx2][ny2] - '0');
							if (binary_search(good[nx2][ny2][l].begin(), good[nx2][ny2][l].end(), it->v + diff))
							{
								if (bestop != sq[nx1][ny1])
								{
									if (bestop == '-')
									{
										bestop = '+';
										bestval = sq[nx2][ny2];
									}
								}
								else
								{
									bestval = min(bestval, sq[nx2][ny2]);
								}
							}
						}
				}
				res.push_back(bestop);
				res.push_back(bestval);
				for (VPII::const_iterator it = poss.begin(); it != poss.end(); ++it)
				{
					for (int d1 = 0; d1 < 4; d1++)
						for (int d2 = 0; d2 < 4; d2++)
						{
							int nx1 = it->x + dx[d1], ny1 = it->y + dy[d1];
							int nx2 = nx1 + dx[d2], ny2 = ny1 + dy[d2];
							if (nx1 < 0 || nx1 >= w || ny1 < 0 || ny1 >= w ||
									nx2 < 0 || nx2 >= w || ny2 < 0 || ny2 >= w)
								continue;
							int diff = (sq[nx1][ny1] == '+' ? 1 : -1) * (sq[nx2][ny2] - '0');
							if (binary_search(good[nx2][ny2][l].begin(), good[nx2][ny2][l].end(), it->v + diff) &&
									sq[nx1][ny1] == bestop && sq[nx2][ny2] == bestval)
								nposs.push_back(PII(nx2,ny2,it->v + diff));
						}
				}
				poss = nposs;
			}
			cout << res << endl;
			cout.flush();
			end:;
		}
	}
	return 0;
}
