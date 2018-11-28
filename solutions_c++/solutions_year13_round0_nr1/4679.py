#include <iostream>

using namespace std;

const int XWIN_1 = 'X' * 4;
const int XWIN_2 = 'X' * 3 + 'T';

const int OWIN_1 = 'O' * 4;
const int OWIN_2 = 'O' * 3 + 'T';

void main(void)
{
	char numcase[100];
	cin.getline(numcase, 100);

	int casecnt = atoi(numcase);


	for(int i = 0; i < casecnt; i++)
	{
		char tables[5][5];
		cin.getline(tables[0], 5);
		cin.getline(tables[1], 5);
		cin.getline(tables[2], 5);
		cin.getline(tables[3], 5);
		cin.getline(tables[4], 5);
		int notcomplete = 0;

		for( int y = 0; y < 4; y++ )
		{
			int k = 0;
			for(int x = 0; x < 4; x++)
			{
				if(tables[y][x] == '.')
				{
//					cout<<"Case #"<<i<<": "<<"Game has not completed\n";
					notcomplete++;
				}

				k+= tables[y][x];
			}

			if(k == XWIN_1 || k == XWIN_2)
			{
				cout<<"Case #"<<i+1<<": "<<"X won\n";
				goto T;
			}

			if(k == OWIN_1 || k == OWIN_2)
			{
				cout<<"Case #"<<i+1<<": "<<"O won\n";
				goto T;
			}
		}

		for( int x = 0; x < 4; x++ )
		{
			int k = 0;
			for(int y = 0; y < 4; y++)
			{
				k+= tables[y][x];
			}

			if(k == XWIN_1 || k == XWIN_2)
			{
				cout<<"Case #"<<i+1<<": "<<"X won\n";
				goto T;
			}

			if(k == OWIN_1 || k == OWIN_2)
			{
				cout<<"Case #"<<i+1<<": "<<"O won\n";
				goto T;
			}
		}
		
		int dia1 = tables[0][0] + tables[1][1] + tables[2][2] + tables[3][3];
		int dia2 = tables[0][3] + tables[1][2] + tables[2][1] + tables[3][0];

		if(dia1 == XWIN_1 || dia1 == XWIN_2)
		{
			cout<<"Case #"<<i+1<<": "<<"X won\n";
			goto T;
		}
		if(dia1 == OWIN_1 || dia1 == OWIN_2)
		{
			cout<<"Case #"<<i+1<<": "<<"O won\n";
			goto T;
		}

		if(dia2 == XWIN_1 || dia2 == XWIN_2)
		{
			cout<<"Case #"<<i+1<<": "<<"X won\n";
			goto T;
		}
		if(dia2 == OWIN_1 || dia2 == OWIN_2)
		{
			cout<<"Case #"<<i+1<<": "<<"O won\n";
			goto T;
		}
		
		if(notcomplete == 0)
			cout<<"Case #"<<i+1<<": "<<"Draw\n";
		else
			cout<<"Case #"<<i+1<<": "<<"Game has not completed\n";

T:
		;
	}
}
