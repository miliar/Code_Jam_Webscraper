#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int co = 0; int cx = 0; int ct  = 0;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	string s[5];
	int test;
	cin >> test; 
	bool e = false;
	for (int t = 1; t <= test; t++)
	{
		cin >> s[0];
		cin >> s[1];
		cin >> s[2];
		cin >> s[3];
		//cin >> s[4];
		co = 0; ct = 0; cx = 0; e = false;
			for (int i = 0; i < 4; i++)
			{ co = 0; cx = 0; ct = 0;
				for (int j = 0; j < 4; j++)
					if (s[i][j] == 'O')
						co++;
					else
						if (s[i][j] == 'X')
							cx++;
						else 
							if (s[i][j] == 'T')
								ct++;
				if (ct + cx == 4)
				{
					if (!e) cout << "Case #" << t << ": " << "X won" << endl;
					e = true;
				}
				if (ct + co == 4)
				{
					if (!e) cout << "Case #" << t << ": " << "O won" << endl;
					e = true;
				}
			}

			for (int j = 0; j < 4; j++)
			{ co = 0; cx = 0; ct = 0;
				for (int i = 0; i < 4; i++)
					if (s[i][j] == 'O')
						co++;
					else
						if (s[i][j] == 'X')
							cx++;
						else 
							if (s[i][j] == 'T')
								ct++;
				if (ct + cx == 4)
				{
					if (!e) cout << "Case #" << t << ": " << "X won" << endl;
					e = true;
				}
				if (ct + co == 4)
				{
					if (!e) cout << "Case #" << t << ": " << "O won" << endl;
					e = true;
				}
			}

			co = cx = ct = 0;
			for (int i = 0; i < 4; i++)
			{
				if (s[i][i] == 'O')
						co++;
					else
						if (s[i][i] == 'X')
							cx++;
						else 
							if (s[i][i] == 'T')
								ct++;
			}
				if (ct + cx == 4)
				{
					if (!e) cout << "Case #" << t << ": " << "X won" << endl;
					e = true;
				}
				if (ct + co == 4)
				{
					if (!e) cout << "Case #" << t  << ": " << "O won" << endl;
					e = true;
				}
			
			co = cx = ct = 0;int j = 0;
			for (int i = 0; i < 4; i++)
			{
				j = 3 - i;
				if (s[i][j] == 'O')
						co++;
					else
						if (s[i][j] == 'X')
							cx++;
						else 
							if (s[i][j] == 'T')
								ct++;
			}
				if (ct + cx == 4)
				{
					if (!e) cout << "Case #" << t << ": " << "X won" << endl;
					e = true;
				}
				if (ct + co == 4)
				{
					if (!e) cout << "Case #" << t << ": " << "O won" << endl;
					e = true;
				} 
			if (!e)
			{
				int cg  = 0;
				for (int i = 0; i < 4; i++)
					for (int j = 0; j < 4; j++)
						if (s[i][j] == '.')
							cg++;
			if (cg == 0)
					cout << "Case #" << t << ": " << "Draw" << endl;
				else
					cout << "Case #" << t << ": " << "Game has not completed" << endl;
			}
		}
}				
			
