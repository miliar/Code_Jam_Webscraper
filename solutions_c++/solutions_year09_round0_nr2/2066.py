#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
using namespace std;

ifstream fin("Watersheds.txt");
#define cin fin

ofstream fout("Watersheds out.txt");
#define cout fout

int R, C;
int grid[110][110];
char rain[110][110];
char ch;
bool visited[110][110];

void Solve(int r, int c, vector<pair<int, int> >vec)
{
	visited[r][c] = 1;
	//North, West, East, South.
	int x[] = {-1, 0, 0, 1};
	int y[] = {0, -1, 1, 0};

	int to = -1, i, mn = grid[r][c];
	for(i=0; i<4; i++)
	{
		int nwr, nwc;
		nwr = r + x[i];
		nwc = c + y[i];
		if(nwr >= 0 && nwr < R && nwc >=0 && nwc < C)
		{
			if(grid[nwr][nwc] < mn)
			{
				if(!visited[nwr][nwc] || (visited[nwr][nwc] && rain[nwr][nwc] != '.'))
				{
					mn = grid[nwr][nwc];
					to = i;
				}
			}
		}
	}
	if(to == -1)
	{
		char cc = ch;
		if(rain[r][c] == '.')
			cc = ++ch;
		else
			cc = rain[r][c];
		for(i=0; i<vec.size(); i++)
		{
			rain[vec[i].first][vec[i].second] = cc;
		}
	}
	else
	{
		vec.push_back(make_pair(r+x[to], c+y[to]));
		Solve(r + x[to], c + y[to], vec);
	}
}


int main()
{
	int t, k;
	cin>>t;
	for(k=0; k<t; k++)
	{
		cin>>R>>C;
		int i, j;
		for(i=0; i<R; i++)
		{
			for(j=0; j<C; j++)
			{
				cin>>grid[i][j];
				rain[i][j] = '.';
				visited[i][j] = 0;
			}
		}
		ch = 'a' - 1;
		for(i=0; i<R; i++)
		{
			for(j=0; j<C; j++)
			{
				if(rain[i][j] == '.')
				{
					visited[i][j] = 1;
					vector<pair<int, int> >vec(1, make_pair(i, j));
					Solve(i, j, vec);
				}
			}
		}
		cout<<"Case #"<<k+1<<":"<<endl;
		for(i=0; i<R; i++)
		{
			for(j=0; j<C; j++)
			{
				cout<<rain[i][j]<<" ";
			}
			cout<<endl;
		}
	}
	return 0;
}