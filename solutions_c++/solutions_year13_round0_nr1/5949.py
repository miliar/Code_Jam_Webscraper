#include<fstream>
using namespace std;
void main()
{
	ifstream _in("in.txt");
	ofstream _out("out.txt");
	if (_in && _out)
	{
		int T = 0;
		_in >> T;
		string map[4][4];
		char ch;
		bool full;
		bool have_res;
		for (int ii=0; ii<T; ii++)
		{
			full = true;
			for (int i=0; i<4; i++)
			{
				for (int j=0; j<4; j++)
				{
					_in >> ch;
					switch(ch)
					{
					case 'X':
						map[i][j] = "X";
						break;
					case 'O':
						map[i][j] = "O";
						break;
					case 'T':
						map[i][j] = "XO";//both
						break;
					default:
						map[i][j] = "";//empty
						full = false;
						break;
					}
				}
			}
			_in.get();
			//
			have_res = false;
			char res;
			for (int i=0;i<4;i++)
			{
				if (map[i][1].find('X')!=-1 && map[i][2].find('X')!=-1 && map[i][3].find('X')!=-1 && map[i][0].find('X')!=-1)			
				{
					res = 'X';
					have_res = true;
				}
				else if (map[i][1].find('O')!=-1 && map[i][2].find('O')!=-1 && map[i][3].find('O')!=-1 && map[i][0].find('O')!=-1)			
				{
					res = 'O';
					have_res = true;
				}
				else if (map[1][i].find('X')!=-1 && map[2][i].find('X')!=-1 && map[3][i].find('X')!=-1 && map[0][i].find('X')!=-1)			
				{
					res = 'X';
					have_res = true;
				}
				else if (map[1][i].find('O')!=-1 && map[2][i].find('O')!=-1 && map[3][i].find('O')!=-1 && map[0][i].find('O')!=-1)			
				{
					res = 'O';
					have_res = true;
				}
			}
			if (!have_res)
			{
				if (map[0][0].find('O')!=-1 && map[1][1].find('O')!=-1 && map[2][2].find('O')!=-1 && map[3][3].find('O')!=-1)
				{
					res = 'O';
					have_res = true;
				}
				else if (map[0][0].find('X')!=-1 && map[1][1].find('X')!=-1 && map[2][2].find('X')!=-1 && map[3][3].find('X')!=-1)
				{
					res = 'X';
					have_res = true;
				}
				else if (map[0][3].find('X')!=-1 && map[1][2].find('X')!=-1 && map[2][1].find('X')!=-1 && map[3][0].find('X')!=-1)
				{
					res = 'X';
					have_res = true;
				}
				else if (map[0][3].find('O')!=-1 && map[1][2].find('O')!=-1 && map[2][1].find('O')!=-1 && map[3][0].find('O')!=-1)
				{
					res = 'O';
					have_res = true;
				}
			}
			if (have_res)
			{
				_out << "Case #" << ii+1 << ": " << res << " won" << endl;
			}
			else
			{
				if (full)
				{
					_out << "Case #" << ii+1 << ": " << "Draw" << endl;
				}
				else
				{
					_out << "Case #" << ii+1 << ": " << "Game has not completed" << endl;
				}
			}
		}
	}
}