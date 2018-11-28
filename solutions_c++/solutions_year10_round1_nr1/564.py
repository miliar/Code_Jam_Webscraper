#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

char b[50][50];
char bi[50][51];

int N, L;

void rotate(int x)
{
	int y=N-1;
	for (int i=N-1;i>=0;i--)
		if (b[x][i]!='.')
			bi[y--][N-1-x] = b[x][i];
	while (y>=0)
		bi[y--][N-1-x]='.';
}

bool chec(int i, int j, int c)
{
	if (bi[i][j] != c) return false;
	//hor
	int jj=j;
	while (jj<N && bi[i][jj]==c)
	{
		if (jj-j+1 == L) return true;
		jj++;
	}

	//ver
	int ii=i;
	while (ii<N && bi[ii][j]==c)
	{
		if (ii-i+1 == L) return true;
		ii++;
	}

	//diag 1
	ii=i;jj=j;
	while (ii<N && jj<N && bi[ii][jj]==c)
	{
		if (ii-i+1 == L) return true;
		ii++;
		jj++;
	}

	//diag 2
	ii=i;jj=j;
	while (ii<N && jj>=0 && bi[ii][jj]==c)
	{
		if (ii-i+1 == L) return true;
		ii++;
		jj--;
	}

	return false;
}
bool win(char c)
{
	for (int i=0;i<N;i++)
		for (int j=0;j<N;j++)
			if (chec(i,j, c))
				return true;
	return false;
}

int main()
{
    ifstream ifs("A-small-attempt0.in");
    ofstream ofs("A-small-attempt0.out");

    int T;

	//ofs.setf(ios::fixed, ios::floatfield);
	//ofs.precision(7);

    ifs >> T;
    for (int i=0;i<T;i++)
    {
		ifs >> N >> L;
		char temp[50];
		ifs.getline(temp, 50);
		for (int i=0;i<N;i++)
		{
			ifs.getline(b[i], 50);
			rotate(i);
		}

		bool wr = win('R');
		bool wb = win('B');
		
		if (wr && wb)
			ofs << "Case #" << i+1 << ": Both" << endl;
		else if (wr)
			ofs << "Case #" << i+1 << ": Red" << endl;
		else if (wb)
			ofs << "Case #" << i+1 << ": Blue" << endl;
		else
			ofs << "Case #" << i+1 << ": Neither" << endl;
		
		
    }
    ifs.close();
    ofs.close();
    return 0;
}
