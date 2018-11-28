#include<iostream>
#include<limits.h>
#include<queue>

using namespace std;

struct data
{
	int cost;
	int con;
	char c;
	bool flag;
};

struct data1
{
	int x, y;
};

int conv[][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int main()
{
	int t, k;
	cin >> t;
	k = 1;
	while (t--)
	{
		int m, n;
		cin >> m >> n;
		struct data **ar;
		ar = new data*[m];
		for (int i = 0; i < m; i++) ar[i] = new data[n];
		for (int i = 0; i < m; i++) 
		{
			for (int j = 0; j < n; j++)
			{
				cin >> ar[i][j].cost;
				ar[i][j].con = 0;
				ar[i][j].c = 0;
				ar[i][j].flag = false;
			}
		}
		int di, min;
		for (int i = 0; i < m; i++) 
		{
			for (int j = 0; j < n; j++)
			{
				min = INT_MAX;
				di = 0;
				if (i > 0 && ar[i - 1][j].cost < ar[i][j].cost)
				{
					if (ar[i - 1][j].cost < min)
					{
						min = ar[i - 1][j].cost;
						di = 1;
					}
				}
				if (j > 0 && ar[i][j - 1].cost < ar[i][j].cost)
				{
					if (ar[i][j - 1].cost < min)
					{
						min = ar[i][j - 1].cost;
						di = 2;
					}
				}
				if (j < n - 1 && ar[i][j + 1].cost < ar[i][j].cost)
				{
					if (ar[i][j + 1].cost < min)
					{
						min = ar[i][j + 1].cost;
						di = 3;
					}
				}
				if (i < m - 1 && ar[i + 1][j].cost < ar[i][j].cost)
				{
					if (ar[i + 1][j].cost < min)
					{
						min = ar[i + 1][j].cost;
						di = 4;
					}
				}
				if (di != 0) 
				{
					ar[i][j].con = di;
				}
			}
		}
		struct data1 d, d1;
		char cc = 'a' - 1;
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (ar[i][j].c == 0) 
				{
					queue<data1> q;
					cc++;
					d.x = i;
					d.y = j;
					q.push(d);
					ar[d.x][d.y].flag = true;
					while (!q.empty())
					{
						d = q.front();
						q.pop();
						ar[d.x][d.y].c = cc;
						if (ar[d.x][d.y].con != 0) 
						{
							d1.x = d.x + conv[ar[d.x][d.y].con - 1][0];
							d1.y = d.y + conv[ar[d.x][d.y].con - 1][1];
							if (!ar[d1.x][d1.y].flag) 
							{
								q.push(d1);
								ar[d1.x][d1.y].flag = true;
							}
						}
						if (d.x > 0 && ar[d.x - 1][d.y].con == 4)
						{
							d1.x = d.x - 1;
							d1.y = d.y;
							if (!ar[d1.x][d1.y].flag) 
							{
								q.push(d1);
								ar[d1.x][d1.y].flag = true;
							}
						}
						if (d.x < m - 1 && ar[d.x + 1][d.y].con == 1)
						{
							d1.x = d.x + 1;
							d1.y = d.y;
							if (!ar[d1.x][d1.y].flag) 
							{
								q.push(d1);
								ar[d1.x][d1.y].flag = true;
							}
						}
						if (d.y > 0 && ar[d.x][d.y - 1].con == 3)
						{
							d1.x = d.x;
							d1.y = d.y - 1;
							if (!ar[d1.x][d1.y].flag) 
							{
								q.push(d1);
								ar[d1.x][d1.y].flag = true;
							}
						}
						if (d.y < n - 1 && ar[d.x][d.y + 1].con == 2)
						{
							d1.x = d.x;
							d1.y = d.y + 1;
							if (!ar[d1.x][d1.y].flag) 
							{
								q.push(d1);
								ar[d1.x][d1.y].flag = true;
							}
						}
					}

				}
			}
		}
		cout << "Case #" << k << ":\n";
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cout << ar[i][j].c << " ";
			}
			cout << endl;
		}
		k++;
	}
}
