#include <fstream>
using namespace std;

ifstream fin("xo.in");
ofstream fout("xo.out");

char a[4][4];

bool wonRow(int i, char ch)
{
		int j;
	for(j=0; j<4; ++j)
		if(a[i][j] != ch && a[i][j]!='T')
			return false;
	return true;
}

bool wonColl(int i, char ch)
{
		int j;
	for(j=0; j<4; ++j)
		if(a[j][i] != ch && a[j][i]!='T')
			return false;
	return true;
}

bool wonAnk1(char ch)
{
		int i,j;
	for(i=0,j=0; i<4; ++i,++j)
		if(a[i][j] != ch && a[i][j]!='T')
			return false;
	return true;
}

bool wonAnk2(char ch)
{
		int i,j;
	for(i=0,j=0; i<4; ++i,++j)
		if(a[i][3-j] != ch && a[i][3-j]!='T')
			return false;
	return true;
}

bool win(char ch)
{
		int i;
	if(wonAnk1(ch) || wonAnk2(ch))
		return true;
	for(i=0;i<4;++i)
		if(wonRow(i,ch) || wonColl(i,ch))
			return true;
	return false;
}

bool hasDot()
{
	int i,j;
	for(i=0;i<4;++i)
		for(j=0;j<4;++j)
			if(a[i][j]=='.')
				return true;
	return false;
}

int main()
{
	int i, j, tt;
	fin>>tt;
	for(int t = 1; t<=tt; ++t)
	{
		for(i=0;i<4;++i)
			for(j=0;j<4;++j)
				fin>>a[i][j];

		fout<<"Case #"<<t<<": ";
		if(win('X'))
			fout<<"X won";
		else if(win('O'))
			fout<<"O won";
		else if(hasDot())
			fout<<"Game has not completed";
		else
			fout<<"Draw";

		fout<<endl;
	}
	return 0;
}