#include <fstream>
#define N 4
using namespace std;
char map[N][N];
bool test(char ch)
{
	int flag[2];
	int T[2];
	int f[2];
	int ft[2];
	for(int x=0;x<N;x++)
	{
		for(int y=0;y<2;y++)
		{
			flag[y]=0;
			T[y]=0;
			f[y]=0;
			ft[y]=0;
		}
		for(int y=0;y<N;y++)
		{
			if(map[x][y]==ch) flag[0]++;
			if(map[x][y]=='T') T[0]++;
			if(map[y][x]==ch) flag[1]++;
			if(map[y][x]=='T') T[1]++;
			if(map[y][y]==ch) f[0]++;
			if(map[y][y]=='T') ft[0]++;
			if(map[y][N-y-1]==ch) f[1]++;
			if(map[y][N-y-1]=='T') ft[1]++;
		}
		if(flag[0]==N || flag[1]==N) return true;
		if(flag[0]==N-1 && T[0]==1) return true;
		if(flag[1]==N-1 && T[1]==1) return true;
		if(f[0]==N || f[1]==N) return true;
		if(f[0]==N-1 && ft[0]==1) return true;
		if(f[1]==N-1 && ft[1]==1) return true;
	}
	return false;
}
int main()
{
	ifstream fin("in.in");
	ofstream fout("out.out");

	int T;
	fin >> T;
	for(int i=0;i<T;i++)
	{
		for(int x=0;x<N;x++)
			for(int y=0;y<N;y++)
				fin >> map[x][y];
		if(test('X')) fout << "Case #" << i+1 << ": X won";
		else if(test('O')) fout << "Case #" << i+1 << ": O won";
		else 
		{
			bool flag=false;
			for(int x=0;x<N;x++)
			{
				for(int y=0;y<N;y++)
				{
					if(map[x][y]=='.')
					{
						flag=true;
						break;
					}
				}
				if(flag) break;
			}
			if(flag) fout << "Case #" << i+1 << ": Game has not completed";
			else fout << "Case #" << i+1 << ": Draw";
		}
		fout << endl;
	}
	fin.close();
	fout.close();
}