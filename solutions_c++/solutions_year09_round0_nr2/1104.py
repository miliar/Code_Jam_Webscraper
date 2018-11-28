#include <iostream>
#include <fstream>

using namespace std;

struct node{int h; char ch; };


int row = 0, col = 0;

char flood_new(node arry[][101], int i ,int j,char ch)
{
	int min = arry[i][j].h;
	int x,y;
	if(arry[i][j].ch == 0)
	{
		arry[i][j].ch = ch;
		
		if( i!= 0 && arry[i-1][j].h < min)
		{
			min = arry[i-1][j].h;
			x = i-1;
			y = j;
		}

		if( j!= 0 && arry[i][j-1].h < min)
		{
			min = arry[i][j - 1].h;
			x = i;
			y = j-1;
		}

		if( j!=col-1  && arry[i][j+1].h < min)
		{
			min = arry[i][j + 1].h;
			x = i;
			y = j+1;
		}

		if( i!= row-1 && arry[i+1][j].h < min)
		{
			min = arry[i+1][j].h;
			x = i+1;
			y = j;
		}

		if(min == arry[i][j].h)
		{
			return 0;
		}
		else
		{
			char t =  flood_new( arry,x ,y ,ch);
			if (t != 0)
			{
				arry[i][j].ch = t;
				return t;
			}
			return 0;
		}
	}
	else
	{
		return arry[i][j].ch;//×²³µ
	}

}

void flood(node arry[][101])
{
	char ch = 'a';
	for(int i = 0 ; i < row; ++i)
	{
		for(int j = 0 ; j < col; ++j)
		{
			if(arry[i][j].ch == 0)
			{

				if (flood_new(arry, i ,j,ch) == 0)
				{
					ch ++;
				}
			}
		}
	}


}
int main()
{
	int T = 0;
	ifstream fin("B-large.in");
//	ifstream fin("B-small-attempt0.in");
	
	ofstream fout("B.out");

	node arry[101][101];

	fin >> T;
	for(int i = 0; i < T;++i)
	{
		fin >> row>> col;
		for(int j = 0 ; j < row ;++j)
			for(int k = 0 ; k < col ;++k)
			{
				fin >> arry[j][k].h;
				arry[j][k].ch=0;
			}

		flood(arry);

		fout <<"Case #"<< (i+1) <<":"<<endl;

		for(int m = 0 ; m < row ;++m)
		{
			for(int n = 0 ; n < col ;++n)
			{
				fout << arry[m][n].ch<<" ";
			}
			fout << endl;
		}

	}
	
	return 0;
}