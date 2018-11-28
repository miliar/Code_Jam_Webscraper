#include<fstream>
using namespace std;
int T;
char mat[5][5];

inline bool Castiga(char c)
{
	int i,j,nr;
	for(i=1;i<=4;i++)
	{
		nr=0;
		for(j=1;j<=4;j++)
			if(mat[i][j]==c || mat[i][j]=='T')
				nr++;
		if(nr==4)
			return true;
		nr=0;
		for(j=1;j<=4;j++)
			if(mat[j][i]==c || mat[j][i]=='T')
				nr++;
		if(nr==4)
			return true;
	}
	nr=0;
	for(i=1;i<=4;i++)
		if(mat[i][i]==c || mat[i][i]=='T')
			nr++;
	if(nr==4)
		return true;
	nr=0;
	for(i=1,j=4;i<=4;i++,j--)
		if(mat[i][j]==c || mat[i][j]=='T')
			nr++;
	if(nr==4)
		return true;
	return false;
}

int main()
{
	int i,j,t;
	bool gol;
	ifstream fin("A.in");
	ofstream fout("A.out");
	fin>>T;
	for(t=1;t<=T;t++)
	{
		gol=false;
		for(i=1;i<=4;i++)
		{
			fin>>(mat[i]+1);
			for(j=1;j<=4;j++)
				if(mat[i][j]=='.')
					gol=true;
		}
		fin.get();
		if(Castiga('X'))
			fout<<"Case #"<<t<<": X won\n";
		else
		{
			if(Castiga('O'))
				fout<<"Case #"<<t<<": O won\n";
			else
			{
				if(gol)
					fout<<"Case #"<<t<<": Game has not completed\n";
				else
					fout<<"Case #"<<t<<": Draw\n";
			}
		}
	}
	fin.close();
	fout.close();
	return 0;
}
