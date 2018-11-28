#include <iostream>
#include <string>
#include <vector>
#include <memory.h>
using namespace std;

int mat[101][101];
int dyn[101][101];
int ind = 0;
int h,w,N;

int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int isValid(int x, int y)
{
	return x >= 0 && x < h && y >= 0 && y < w;
}

int dynamic(int x, int y)
{
//	cout<<x<<' '<<y<<endl;
	if(dyn[x][y] != -1)
		return dyn[x][y];
	int mn = 100000;
	for(int i = 0; i < 4; i++)
	{
		int nx = x + dir[i][0];
		int ny = y + dir[i][1];
		if(isValid(nx, ny))
		{
			if(mat[nx][ny] < mn)
				mn = mat[nx][ny];
		}
	}
	if(mn < mat[x][y])
	{
	for(int i = 0; i < 4; i++)
	{
		int nx = x + dir[i][0];
		int ny = y + dir[i][1];
		if(isValid(nx, ny))
		{
			if(mat[nx][ny] == mn){
				dyn[x][y] = dynamic(nx, ny);
				return dyn[x][y];
			}
		}

	}
	}else return dyn[x][y] = ind++;
}

int main()
{
	cin>>N;
	for(int c = 1; c <= N; c++)
	{
		ind = 0;
		cin>>h>>w;
		for(int i = 0; i < h; i++)
			for(int j = 0; j < w; j++)
				cin>>mat[i][j];
		memset(dyn, -1, sizeof dyn);
		for(int i = 0; i < h; i++)
			for(int j = 0; j < w; j++)
			{
//				cout<<"Hey: "<<i<<' '<<j<<endl;
				dyn[i][j] = dynamic(i, j);
			}
		cout<<"Case #"<<c<<":"<<endl;
		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)
			{
				if(j)cout<<' ';
				cout<<(char)(dyn[i][j] + 'a');
			}
			cout<<endl;
		}
	}
	return 0;
}
