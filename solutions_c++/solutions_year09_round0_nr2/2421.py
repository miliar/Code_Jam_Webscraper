#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <stack>
using namespace std;

class TaskB
{
	int H, W;
	vector<vector<int> > map;
	struct Pt { int r, c; };
public:
	void ReadData()
	{
		cin >> H >> W;
		map.assign(H, vector<int>(W));
		for (int i=0; i<H; ++i)  for (int j=0; j<W; ++j)  cin >> map[i][j];
	}
	void Solve(int nCase)
	{
		ReadData();

		vector<vector<char> > res(H, vector<char>(W, ' '));
		char c = 'a';

		for (int i=0; i<H; ++i)
		for (int j=0; j<W; ++j)
		{
			stack<Pt> trace;
			Pt cur;  cur.r = i;  cur.c = j;

			char mark;

			while (res[cur.r][cur.c]==' ')
			{
				trace.push(cur);
				Pt nxt = cur;
				if (cur.r>0   && map[cur.r-1][cur.c] < map[nxt.r][nxt.c])  nxt.r = cur.r-1, nxt.c = cur.c;
				if (cur.c>0   && map[cur.r][cur.c-1] < map[nxt.r][nxt.c])  nxt.r = cur.r, nxt.c = cur.c-1;
				if (cur.c<W-1 && map[cur.r][cur.c+1] < map[nxt.r][nxt.c])  nxt.r = cur.r, nxt.c = cur.c+1;
				if (cur.r<H-1 && map[cur.r+1][cur.c] < map[nxt.r][nxt.c])  nxt.r = cur.r+1, nxt.c = cur.c;

				if (cur.c==nxt.c && cur.r==nxt.r)
				{
					mark = c++;			// next character
					break;
				}
				else if (res[nxt.r][nxt.c]!=' ')
				{
					mark = res[nxt.r][nxt.c];
					break;
				}
				cur = nxt;
			}

			while (!trace.empty())
			{
				Pt cur = trace.top();  trace.pop();
				res[cur.r][cur.c] = mark;
			}
		}

		cout << "Case #" << nCase << ": " << endl;
		for (int i=0; i<H; ++i)
		{
			for (int j=0; j<W; ++j)  cout << res[i][j] << ' ';
			cout << endl; cout.flush();
		}
	}
};

int main()
{
	//int N;  string s;  getline(cin, s);  istringstream(s) >> N;
	int N;  cin >> N;
	TaskB sol;	for (int i=1; i<=N; ++i)  sol.Solve(i);
	return 0;
}