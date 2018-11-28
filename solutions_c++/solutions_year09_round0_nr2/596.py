#include <iostream>
#include <string>
#include <vector>

using namespace std;

int alt[200][200];
int labels[200][200];
int H, W;

int SetLabel(int i, int j, int l)
{
	if(labels[i][j] != 0)
	{
		return labels[i][j];
	}
	labels[i][j] = l;
	int i1 = i, j1 = j, minHeight = alt[i][j];
	if(i > 0 && alt[i-1][j] < minHeight)
	{
		minHeight = alt[i-1][j];
		i1 = i-1;
		j1 = j;
	}
	if(j > 0 && alt[i][j-1] < minHeight)
	{
		minHeight = alt[i][j-1];
		i1 = i;
		j1 = j-1;
	}
	if(j < (W-1) && alt[i][j+1] < minHeight)
	{
		minHeight = alt[i][j+1];
		i1 = i;
		j1 = j+1;
	}
	if(i < (H-1) && alt[i+1][j] < minHeight)
	{
		minHeight = alt[i+1][j];
		i1 = i+1;
		j1 = j;
	}
	if(i1 != i || j1 != j)
	{
		labels[i][j] = SetLabel(i1, j1, l);
	}
	return labels[i][j];
}

int main()
{
	int T;
	cin >> T;
	for(int N = 1; N <= T; N++)
	{
		cin >> H >> W;
		for(int i = 0; i < H; i++)
		{
			for(int j = 0; j < W;j++)
			{
				cin >> alt[i][j];
			}
		}
		int label = 'a';
		memset(labels, 0, 200 * 200 * sizeof(labels[0][0]));
		for(int i = 0; i < H; i++)
		{
			for(int j = 0; j < W; j++)
			{
				int newLabel = SetLabel(i, j, label);
				if(newLabel == label)
				{
					label ++;
				}
			}
		}
		cout << "Case #" << N << ":" << endl;
		for(int i = 0; i < H; i++)
		{
			cout << (char)labels[i][0] << ' ';
			for(int j = 1; j < W; j++)
			{
				cout << (char)labels[i][j] << ' ';
			}
			cout << endl;
		}
	}
	return 0;
}
