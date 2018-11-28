#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define sz 
#define GI(t) (scanf("%d", &(t)))

vector <string> board; 
vector < pair <int, int> > pos; 
vector < pair <int, int> > temp;
vector < pair <int, int> > result;
map <long long, int> m;
queue < pair <long long, bool> > que; 
int r, c, n;
bool boolean;
int dx[4]; 
int dy[4]; 

long long encode(vector < pair <int, int> > &p)
{
	long long ret = 0;
	for (int i = 0; i < n; i++)
		ret = (ret*144LL)+p[i].first*12LL+p[i].second;
	return ret;
}

void decode(long long val, vector < pair <int, int> > &p)
{
	for (int i = n-1; i >= 0; i--)
	{
		p[i].second = val%12LL; val /= 12LL;
		p[i].first = val%12LL; val /= 12LL;
	}
}

bool check (vector < pair <int, int> > &p)
{
	bool ret;
	if (n==1) return true;
	for (int i = 0; i < n; i++)
	{
		ret = false;	
		for (int j = 0; j < n; j++)
			if (abs(p[i].first-p[j].first) + abs(p[i].second-p[j].second) == 1)
				ret  = true;
		if (!ret) return false;
	}
	return true;
}

bool valid(int index,int dir, vector < pair <int, int> > &p, bool stat, bool &end_stat)
{
//			cout << "valid" << endl;
	if (p[index].first + dx[dir] < r && p[index].first + dx[dir] >= 0)
		if (p[index].second + dy[dir] < c && p[index].second + dy[dir] >= 0)
			if (board[p[index].first + dx[dir]][p[index].second + dy[dir]]=='.'||board[p[index].first + dx[dir]][p[index].second + dy[dir]]=='x')
				if (p[index].first - dx[dir] < r && p[index].first - dx[dir] >= 0)
					if (p[index].second - dy[dir] < c && p[index].second - dy[dir] >= 0)
						if (board[p[index].first - dx[dir]][p[index].second - dy[dir]]=='.'||board[p[index].first - dx[dir]][p[index].second - dy[dir]]=='x')
						{
							p[index].first += dx[dir];
							p[index].second += dy[dir];
							bool tr = true;
							for (int i = 0; i < n; i++)
								if (i != index)
									if (p[i]==p[index] || (p[index].first - 2*dx[dir]==p[i].first && p[index].second - 2*dy[dir] == p[i].second))
										tr = false;
							if (tr)
							{
								if (stat)
								{
									if (check(p))
									{
										end_stat = false;
										return true;
									}
									else
									{
										p[index].first -= dx[dir];
										p[index].second -= dy[dir];
									}
								}
								else
								{
									end_stat = !check(p);
									return true;
								}
							}
							else
							{
								p[index].first -= dx[dir];
								p[index].second -= dy[dir];
							}
						}
	return false;
}

int main ()
{
//    freopen("input.txt", "r", stdin);
	freopen("A-small-attempt2.in", "r", stdin);
    freopen("Asmall.txt", "w", stdout);
	dx[0] = 1; dx[2] = -1; 
	dy[1] = 1; dy[3] = -1; 
    int test_cases;
	cin >> test_cases;
    for (int numb = 0; numb < test_cases; numb++)
    {
		cin >> r >> c;
		board.resize(r);
		result.resize(0);
		n = 0;
		m.clear();
		for (int i = 0; i < r; i++)
			cin >> board[i];
		pos.resize(0);
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
			{
				if (board[i][j]=='o')
				{
					board[i][j] = '.';
					pos.push_back(make_pair(i,j)); n++; 
				}
				else if (board[i][j] == 'w')
				{
					board[i][j] = 'x';
					pos.push_back(make_pair(i,j)); n++; 
					result.push_back(make_pair(i,j));
				}
				else if (board[i][j]=='x')
				{
					result.push_back(make_pair(i,j));
				}
			}
		sort(result.begin(), result.end());
		sort(pos.begin(), pos.end());

//		for (int i = 0; i < n; i++)
//			cout << pos[i].first << ' ' << pos[i].second << ' ';
//		cout << endl;
//		for (int i = 0; i < n; i++)
//			cout << result[i].first << ' ' << result[i].second << ' ';
//		cout << endl;
//		for (int i = 0; i < r; i++)
//			cout << board[i] << endl;

		que.push(make_pair(encode(pos),false));
		m[encode(pos)] = 0;
		pair <long long, bool> req; 
		while (!que.empty())
		{
//			cout << "loop" << endl;

			req = que.front();
			que.pop(); 
			decode(req.first, pos);

//			for (int arbit = 0; arbit < n; arbit++)
//				cout << pos[arbit].first << ' ' << pos[arbit].second << ' ';
//			cout << endl;

			for (int i = 0; i < n; i++)
				for (int j = 0; j < 4; j++)
					if (valid(i,j,pos,req.second,boolean))
					{
//						cout << "True" << endl;
//						for (int arbit = 0; arbit < n; arbit++)
//							cout << pos[arbit].first << ' ' << pos[arbit].second << ' ';
//						cout << endl;
//						cout << i << ' ' << j << endl;

						temp = pos; 
						pos[i].first -= dx[j];
						pos[i].second -= dy[j];
						sort(temp.begin(), temp.end());
						if (m.find(encode(temp))==m.end())
						{
							m[encode(temp)] = m[req.first]+1;
							que.push(make_pair(encode(temp),boolean));
						}
					}
//			cout << endl;
		}
		if (m.find(encode(result))!=m.end())
			cout << "Case #" << numb+1 << ": " << m[encode(result)] << endl;
		else
			cout << "Case #" << numb+1 << ": -1\n";
    }
    return 0;
}
/*
    *  '.' is an empty spot
    * '#' is a wall
    * 'x' is a goal (where a box should be at the end)
    * 'o' is a box
    * 'w' is a both a box and a goal
*/