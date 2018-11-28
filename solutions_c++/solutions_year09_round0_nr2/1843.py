#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

vector <vector <vector <pair<int,int> > > > gr;
vector <vector <int> > arr;
vector <vector <char> > color;
int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};

void DFS(pair<int,int> p , char c)
{
	if (color[p.first][p.second] != 0)
		return;
	color[p.first][p.second] = c;
	for (int i =0 ;i < gr[p.first][p.second].size(); i ++)
		DFS(gr[p.first][p.second][i],c);
}

int main()
{
	freopen("f.in", "r", stdin);
	freopen("f.out", "w", stdout);
	int t;
	cin >> t;
	int h,w;	
	for (int test = 1; test <= t; test ++)
	{
		arr.clear();
		cin >> h >> w;
		arr.assign(h,vector<int>(w));
		color.assign(h,vector<char>(w,0));
		gr.assign(h,vector<vector <pair<int,int> > >(w));
		for (int i = 0 ;i < h; i ++)
			for (int j =0; j < w ;j ++)
			{
				cin >> arr[i][j];
			}
		for (int i =0;i < h; i ++)
			for (int j =0 ;j < w; j ++)
			{
				int m = arr[i][j];
				int mx,my;
				for (int k = 0; k < 4; k ++)
				{
					int x = i+dx[k];
					int y = j+dy[k];
					if (x < 0 || y < 0 || x >= h || y >= w)
						continue;
					if (arr[x][y] < m)
					{
						mx = x;
						my = y;
						m = arr[x][y];
					}
				}
				if (m != arr[i][j])
				{
					gr[i][j].push_back(make_pair(mx,my));
					gr[mx][my].push_back(make_pair(i,j));
				}
			}
		int c = 'a';
		for (int i =0;i < h; i ++)
			for (int j =0 ;j < w; j ++)
				if (color[i][j] == 0)
					DFS(make_pair(i,j),c++);
		cout << "Case #" << test << ":" << endl;
		for (int i =0;i < h; i ++)
		{
			for (int j =0 ;j < w; j ++)
	//		if (color[i][j] == 'c')
	//			cout << "F";
	//		else
			{
				//if (gr[i][j].size() > 1)
				//	cout << "F";
				cout << color[i][j] << " ";
			}
			cout << endl;
		}
	}
	return 0;
}