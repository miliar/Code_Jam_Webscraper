#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
using namespace std;

//============================================================
// Water
//============================================================
class Water
{
public:
	void AddRow(const vector<int> &row)
	{
		grid.push_back(row);
	}

	void Solve()
	{
		graph.assign(grid.size(),vector<int>(grid[0].size(), -1));
		next_char = 0;

		for(int y = 0;y < (int)grid.size();++y) {
			for(int x = 0;x < (int)grid[y].size();++x) {
				if(graph[y][x] < 0)
					FindSink(y,x);
				if(x != 0)
					cout << ' ';
				cout << (char)('a' + graph[y][x]);
			}
			cout << '\n';
		}
	}
private:
	vector<vector<int> > grid;
	vector<vector<int> > graph;
	int next_char;
	void FindSink(int y,int x)
	{
		vector<pair<int,int> >  passed;
		passed.push_back(make_pair(y,x));

		static const int dy[] = {-1,0,0,1};
		static const int dx[] = {0,-1,1,0};

		int use_char = next_char;
		int by=-1,bx=-1;
		while(true){
			by = passed.back().first;
			bx = passed.back().second;
			if(graph[by][bx] >= 0){
				use_char = graph[by][bx];
				break;
			}
			int small = grid[by][bx];
			for(int k = 0;k < 4;++k) {
				int ny = y + dy[k];
				int nx = x + dx[k];
				if(ny < 0 || ny >= (int)grid.size()) continue;
				if(nx < 0 || nx >= (int)grid[0].size()) continue;
				if(grid[ny][nx] < small){
					small = grid[ny][nx];
					by = ny; bx = nx;
				}
			}

			if(by == y && bx == x) break;
			passed.push_back(make_pair(by,bx));
			y = by; x = bx;
		}

		// Mark vertices with char.
		for(int k = 0;k < (int)passed.size();++k)
			graph[passed[k].first][passed[k].second] = use_char;

		if(use_char == next_char) ++next_char;
	}
};
//============================================================

int main()
{
	int T;
	cin >> T;
	for(int k = 0;k < T;++k) {
		int H,W;
		cin >> H >> W;
		Water problem;
		for(int h = 0;h < H;++h){
			vector<int> row;
			for(int w = 0;w < W;++w){
				int tmp;
				cin >> tmp;
				row.push_back(tmp);
			}
			problem.AddRow(row);
		}
		cout << "Case #" << k+1 << ":\n";
		problem.Solve();
	}
}
