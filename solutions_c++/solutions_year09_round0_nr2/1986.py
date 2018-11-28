
#include<algorithm>
#include<bitset>
#include<iostream>
#include<string>
#include<cstdio>
#include<sstream>
#include<vector>
#include<stack>
#include<deque>
#include<map>
#include<iterator>
#include<cmath>
#include<complex>
#include<queue>
#include<cassert>
#include<set>
#include<cstring>
#include<list>
#include<numeric>
#include<cassert>

#define FOREACH(it ,c ) for( typeof((c).begin()) it= (c).begin();it!=(c).end();++it) 
#define debug(x) cerr<< #x << " = " << x << "\n";
#define debugv(x) cerr<< #x << " = " ; FOREACH(it,(x)) cerr << *it << "," ; cerr<< "\n" ;
#define MP make_pair
#define PB push_back
#define siz(w) (int)w.size()
#define fup(i,st,ko) for(int i=st;i<=ko;i++)
#define fdo(i,st,ko) for(int i=st;i>=ko;i--)
#define REP(i,w) for(int i=0;i<siz(w);i++)
#define inf 100000000

using namespace std;

typedef long long ll;
#define maxn 104
int attitude[maxn][maxn];
int num[maxn][maxn];
int H, W;
char letter[30];

bool good(int y, int x)
{
	if(y < 1 or y > H or x < 1 or x > W) return false;
	return true;
}

int tx[] = { 0, -1, 1, 0 };
int ty[] = { -1, 0, 0, 1 };

int main()
{
	int cas;
	cin >> cas;
	fup(xx, 1, cas)
	{
		memset(letter, 0, sizeof(letter));
		memset(attitude, 0, sizeof(attitude));
		vector<pair<int, pair<int, int> > > points;
		cin >> H >> W;
		fup(y, 1, H) fup(x, 1, W)
		{
			cin >> attitude[y][x];
			points.push_back(make_pair(attitude[y][x], make_pair(y, x)));
		}
		sort(points.begin(), points.end());
		int number = 0;
		REP(i, points)
		{
			int y, x, height;
			y = points[i].second.first;
			x = points[i].second.second;
			height = points[i].first;

			int minh = height;
			int kt = -1;
			fup(j, 0, 3)
			{
				int yy = y + ty[j];
				int xx = x + tx[j];
				if(good(yy, xx))
				{
					if(attitude[yy][xx] < minh)
					{
						minh = attitude[yy][xx];
						kt = j;
					}
				}
			}
			if(kt == -1)
			{
				number ++;
				num[y][x] = number;
			}
			else
			{
				num[y][x] = num[y + ty[kt]][x + tx[kt]];
			}	
		}
		char c = 'a';
		fup(y, 1, H) fup(x, 1, W)
		{
			int sink = num[y][x];
			if(letter[sink] == 0)
			{
				letter[sink] = c;
				c ++;
			}
		}
		cout << "Case #" << xx << ":" << endl;
		fup(y, 1, H)
		{
			fup(x, 1, W)
			{
				cout << letter[num[y][x]];
				if(x < W) cout << " ";
				else cout << endl;
			}
		}
	}

	return 0;
}



