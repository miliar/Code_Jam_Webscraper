#include <fstream>
using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("out.txt");
	char map[4][5];
	int chk;
	int i, j, k;
	int cntO, cntX, cntT, cnt;
	int T;
	fin >> T;
	for(i=1;i<=T;i++)
	{
		fout << "Case #" << i << ": ";
		for(j=0;j<4;j++)
		{
			fin >> map[j];
		}
		cnt = chk = 0;
		for(j=0;j<4;j++)
		{
			cntO = cntX = cntT = 0;
			for(k=0;k<4;k++)
			{
				cnt += (map[j][k]=='.');
				if(map[j][k] == 'O') cntO++;
				else if(map[j][k] == 'X') cntX++;
				else if(map[j][k] == 'T') cntT++;

			}
			if(cntO + cntT == 4) 
			{
				fout << "O won" << endl;
				chk = 1;
				j=10;
				continue;
			}
			else if(cntX + cntT == 4)
			{
				fout << "X won" << endl;
				chk = 1;
				j=10;
				continue;
			}
			cntO = cntX = cntT = 0;
			for(k=0;k<4;k++)
			{
				if(map[k][j] == 'O') cntO++;
				else if(map[k][j] == 'X') cntX++;
				else if(map[k][j] == 'T') cntT++;
			}
			if(cntO + cntT == 4) 
			{
				fout << "O won" << endl;
				chk = 1;
				j=10;
				continue;
			}
			else if(cntX + cntT == 4)
			{
				fout << "X won" << endl;
				chk = 1;
				j=10;
				continue;
			}
		}
		if(j>5) continue;
		cntO = cntX = cntT = 0;
		for(k=0;k<4;k++)
		{
			if(map[k][k] == 'O') cntO++;
			else if(map[k][k] == 'X') cntX++;
			else if(map[k][k] == 'T') cntT++;
		}
		if(cntO + cntT == 4) 
		{
			fout << "O won" << endl;
			chk = 1;
			continue;
		}
		else if(cntX + cntT == 4)
		{
			fout << "X won" << endl;
			chk = 1;
			continue;
		}


		cntO = cntX = cntT = 0;
		for(k=0;k<4;k++)
		{
			if(map[3-k][k] == 'O') cntO++;
			else if(map[3-k][k] == 'X') cntX++;
			else if(map[3-k][k] == 'T') cntT++;
		}
		if(cntO + cntT == 4) 
		{
			fout << "O won" << endl;
			chk = 1;
			continue;
		}
		else if(cntX + cntT == 4)
		{
			fout << "X won" << endl;
			chk = 1;
			continue;
		}

		if(chk==0 && cnt==0) fout << "Draw" << endl;
		else if(chk==0 && cnt!=0) fout << "Game has not completed" << endl;
	}
}