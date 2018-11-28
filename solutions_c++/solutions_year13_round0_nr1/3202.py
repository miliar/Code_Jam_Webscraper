#include <fstream>

using namespace std;

main()
{
	int T;
	char map[4][4];
	ifstream fin ("input.in");
	ofstream fout ("output.out");
	fin >> T;
	for (int z=1;z<=T;z++)
	{
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++)
				fin >> map[i][j];
		bool iC=true;
		for (int i=0;i<4;i++)
		{
			int X=0,O=0;
			for (int j=0;j<4;j++)
			{
				if (map[i][j]=='O') O++;
				if (map[i][j]=='X') X++;
				if (map[i][j]=='T') {O++;X++;}
				if (map[i][j]=='.') iC=false;
			}
			if (O==4)
			{
				fout << "Case #" << z << ": O won";
				goto mend;
			}
			if (X==4)
			{
				fout << "Case #" << z << ": X won";
				goto mend;
			}
		}
		for (int j=0;j<4;j++)
		{
			int X=0,O=0;
			for (int i=0;i<4;i++)
			{
				if (map[i][j]=='O') O++;
				if (map[i][j]=='X') X++;
				if (map[i][j]=='T') {O++;X++;}
				if (map[i][j]=='.') iC=false;
			}
			if (O==4)
			{
				fout << "Case #" << z << ": O won";
				goto mend;
			}
			if (X==4)
			{
				fout << "Case #" << z << ": X won";
				goto mend;
			}
		}
		{
			int X=0,O=0;
			for (int i=0;i<4;i++)
			{
				if (map[i][i]=='O') O++;
				if (map[i][i]=='X') X++;
				if (map[i][i]=='T') {O++;X++;}
				if (map[i][i]=='.') iC=false;
			}
			if (O==4)
			{
				fout << "Case #" << z << ": O won";
				goto mend;
			}
			if (X==4)
			{
				fout << "Case #" << z << ": X won";
				goto mend;
			}
			X=O=0;
			for (int i=0;i<4;i++)
			{
				if (map[i][3-i]=='O') O++;
				if (map[i][3-i]=='X') X++;
				if (map[i][3-i]=='T') {O++;X++;}
				if (map[i][3-i]=='.') iC=false;
			}
			if (O==4)
			{
				fout << "Case #" << z << ": O won";
				goto mend;
			}
			if (X==4)
			{
				fout << "Case #" << z << ": X won";
				goto mend;
			}
		}
		if (iC)
			fout << "Case #" << z << ": Draw";
		else
			fout << "Case #" << z << ": Game has not completed";
		mend:
			fout << endl;
	}
}
