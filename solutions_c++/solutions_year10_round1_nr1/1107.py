#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;
const int dir[8][2] = {{0,1},{1,0},{0,-1},{-1,0},{-1,1},{1,1},{1,-1},{-1,-1}};
int N,K;
vector<string> G;
vector<string> R;
vector<int> H;
int maxH = 0;
int maxJ = 0;

void Rotate()
{
	string str(N,'.');
	R.assign(N,str);
	for(int i = 0; i < N; i++)
	{
		if(H[i])
		{
			for(int j = N-1; j >= N-H[i]; j--)
			{
				R[i][N-1-j] = G[j][i];
			}
		}
	}
	
	int k;
	for(int j = 0; j < maxH; j++)
	{
		for(int i = N - 1; i >= 0; i--)
		{
			for(k = i; k >= 0 && R[k][j] == '.'; k--);
			if(k >= 0)
				swap(R[i][j],R[k][j]);
		}
	}
}
bool check(char w)
{
	int x,y;
	for(int i = 0; i < N; i++)
	{
		for(int j = 0; j < N; j++)
		{
			if(R[i][j] == w)
			{
				for(int d = 0; d < 8; d++)
				{
					int k = 0;
					x = i;
					y = j;
					while(x >= 0 && x < N && y >= 0 && y < N && R[x][y] == w)
					{
						x = x + dir[d][0];
						y = y + dir[d][1];
						k++;
					}
					if(k >= K)
						return true;					
				}
			}
		}
	}
	return false;
}
int main()
{
	ifstream input("A-large.in");
	ofstream out("test.out");
	int T;
	bool red = false;
	bool blue = false;
	input >> T;
	for(int i = 1; i <= T; i++)
	{
		string str;
		input >> N >> K;
		H.assign(N,0);
		G.clear();
		for(int j = 0; j < N; j++)
		{
			input >> str;
			G.push_back(str);
			for(string::size_type k = 0; k < N; k++)
			{
				if(!H[k] && str[k] != '.')
				{
					if(k > maxJ)
						maxJ = k;
					H[k] = N - j;
					if(H[k] > maxH)
						maxH = H[k];
				}
			}
		}
		Rotate();
		red = check('R');
		blue = check('B');
		if(red && blue)
		{
			out << "Case #" << i << ": " << "Both" << endl;
		}
		else if(red)
		{
			out << "Case #" << i << ": " << "Red" << endl;
		}
		else if(blue)
		{
			out << "Case #" << i << ": " << "Blue" << endl;
		}
		else
		{
			out << "Case #" << i << ": " << "Neither" << endl;
		}
	}
	return 0;
}