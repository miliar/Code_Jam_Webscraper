#include <vector>
#include <string>
#include <fstream>

using namespace std;

int dr[] = {-1,0,0,1};
int dc[] = {0,-1,1,0};

char flow(const vector<vector<int> > &m, vector<string> &res, int r, int c, char &b)
{
	if(res[r][c] != '.')
		return res[r][c];
	int newr = r, newc = c;
	int mn = m[r][c];
	for(int i = 0; i < 4; i++)
	{
		if(r + dr[i] >= 0 && r + dr[i] < m.size() &&
			c + dc[i] >= 0 && c + dc[i] < m[r].size() &&
			m[r + dr[i]][c + dc[i]] < mn)
		{
			mn = m[r + dr[i]][c + dc[i]];
			newr = r + dr[i];
			newc = c + dc[i];
		}
	}
	if(mn < m[r][c])
	{
		res[r][c] = flow(m, res, newr, newc, b);
		return res[r][c];
	}
	else
	{
		res[r][c] = b;
		b++;
		return res[r][c];
	}
}

int main()
{
	ifstream f;
	f.open("Blarge.txt");
	int T;
	f >> T;
	ofstream o;
	o.open("Boutlarge.txt");
	for(int i = 0; i < T; i++)
	{
		int H, W;
		f >> H >> W;
		vector<vector<int> > m;
		int t;
		for(int r = 0; r < H; r++)
		{
			m.push_back(vector<int>());
			for(int c = 0; c < W; c++)
			{
				f >> t;
				m[r].push_back(t);
			}
		}
		vector<string> res(H, string(W, '.'));
		o << "Case #" << (i+1) << ":" << endl;
		char b = 'a';
		for(int r = 0; r < H; r++)
			for(int c = 0; c < W; c++)
				if(res[r][c] == '.')
					flow(m, res, r, c, b);
		for(int r = 0; r < H; r++)
		{
			for(int c = 0; c < W - 1; c++)
			{
				o << res[r][c] << " ";
			}
			o << res[r][W - 1] << endl;
		}
	}
	o.close();
	f.close();
}