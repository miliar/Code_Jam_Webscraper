#include <iostream>
#include <vector>

using namespace std;

const int is[4] = {1, 0, 0, -1};
const int js[4] = {0, -1, 1, 0};

int t;
int h, w;
int num = 0;
bool mem = false;
vector< vector<int> > data;
vector< vector<bool> > used;
vector< vector<char> > rez;

int Go(int e, int r)
{
	int min_cnt = data[e][r];
	int min_e = -1;
	int min_r = -1;

	for (int i = 0; i < 4; i++)
	{
		int new_e = e + is[i];
		int new_r = r + js[i];
		if (0 <= new_e && new_e < h
		&& 0 <= new_r && new_r < w)
		{
			if (data[new_e][new_r] < min_cnt) 
			{
				min_e = new_e;
				min_r = new_r;
				min_cnt = data[new_e][new_r];
			}
		}
	}

	if (min_cnt != data[e][r])
	{
		used[min_e][min_r] = true;
		int tmp = Go(min_e, min_r);
		rez[e][r] = 'a' + tmp;
		return tmp;
	}
	else
	{
		if (rez[e][r] == 0)
		{
			mem = true;
			rez[e][r] = 'a' + num;
			return num;
		}
		else
			return (rez[e][r] - 'a');
	}
}

void Solve()
{
	for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++)
		{
			if (!used[i][j])
			{
				used[i][j] = true;
				Go(i, j);
				if (mem)
				{
					mem = false;
					num++;
				}
			}
		}
}

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);

	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cin >> h >> w;
		data.clear();
		used.clear();
		rez.clear();
		num = 0;
		mem = false;
		data.resize(h);
		used.resize(h);
		rez.resize(h);
		for (int j = 0; j < h; j++)
		{
			data[j].resize(w);
			used[j].resize(w, false);
			rez[j].resize(w, 0);
			for (int u = 0; u < w; u++)
				cin >> data[j][u];
		}

		Solve();
		cout << "Case #" << i + 1 << ":" << endl;
		for (int j = 0; j < h; j++)
			for (int u = 0; u < w; u++)
			{
				cout << rez[j][u];
				if (u == w - 1)
					cout << endl;
				else
					cout << " ";
			}

	}

	return 0;
}