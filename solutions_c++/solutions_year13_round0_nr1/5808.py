#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char** argv)
{
	int cases;
	int i,j,k,l,c;
	string map[4];
	int dotcount = 0;
	string t;
	char startchar;
	char winchar;
	ofstream ofs("result.txt");
	string filename = argv[1];
	ifstream ifs(filename.c_str());
	ifs >> cases;

	for (c=0;c<cases;c++)
	{
		winchar = '?';
		dotcount = 0;
		for(i=0;i<4;i++)
		{
			ifs >> map[i];
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++) if (map[i][j] == '.') dotcount++;
		}
		for(i=0;i<4;i++)
		{
			startchar = map[i][0];
			for (j=0;j<4;j++)
			{
				if (map[i][j] == 'O' || map[i][j] == 'X') startchar = map[i][j];
			}
			if (startchar != 'O' && startchar != 'X') continue;
			for(j=0;j<4;j++)
			{
				if (map[i][j] != startchar && map[i][j] != 'T')
				{
					break;
				}
			}
			if (j == 4) winchar = startchar;
		}
		for(i=0;i<4;i++)
		{
			startchar = map[0][i];
			for (j=0;j<4;j++)
			{
				if (map[j][i] == 'O' || map[j][i] == 'X') startchar = map[j][i];
			}
			if (startchar != 'O' && startchar != 'X') continue;
			for(j=0;j<4;j++)
			{
				if (map[j][i] != startchar && map[j][i] != 'T')
				{
					break;
				}
			}
			if (j == 4) winchar = startchar;
		}
		startchar = map[0][0];
		for (j=0;j<4;j++)
		{
			if (map[j][j] == 'O' || map[j][j] == 'X') startchar = map[j][j];
		}
		if (startchar == 'O' || startchar == 'X')
		{
			for (i=0;i<4;i++)
			{
				if (map[i][i] != startchar && map[i][i] != 'T') { break; }	
			}
			if (i == 4) winchar = startchar;
		}
		startchar = map[0][3];
		for (j=0;j<4;j++)
		{
			if (map[j][3-j] == 'O' || map[j][3-j] == 'X') startchar = map[j][3-j];
		}
		if (startchar == 'O' || startchar == 'X')
		{
			for (i=0;i<4;i++)
			{
				if (map[i][3-i] != startchar && map[i][3-i] != 'T') { break; }
			}
		}	
		if (i == 4) winchar = startchar;

		ofs << "Case #" << c+1 << ": ";

		if (winchar == 'O')
		{
			ofs << "O won";
		}
		else if (winchar == 'X')
		{
			ofs << "X won";
		}
		else if (dotcount != 0)
		{
			ofs << "Game has not completed";
		}
		else
		{
			ofs << "Draw";
		}

		ofs << endl;
	}

	return 0;
}
