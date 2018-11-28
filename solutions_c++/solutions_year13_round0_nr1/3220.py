#include <fstream>

using namespace std;

int x[4][4];

bool test()
{
	int col[4], row[4], mdiag, odiag;

	for(int i = 0; i < 4; ++i) {
		col[i] = x[0][i] + x[1][i] + x[2][i] + x[3][i];
		row[i] = x[i][0] + x[i][1] + x[i][2] + x[i][3];
	}

	mdiag = x[0][0] + x[1][1] + x[2][2] + x[3][3];
	odiag = x[0][3] + x[1][2] + x[2][1] + x[3][0];

	return (col[0] >= 3) || (col[1] >= 3) || (col[2] >= 3) || (col[3] >= 3) 
		|| (row[0] >= 3) || (row[1] >= 3) || (row[2] >= 3) || (row[3] >= 3)
		|| mdiag >= 3 || odiag >= 3;
}

int main()
{
	ifstream in("A-large.in");
	ofstream out("out.txt");

	int n;
	in >> n;

	char s[10];
	in.getline(s, 10);

	for(int k = 1; k <= n; ++k) {
		bool not_filled = false;

		for(int i = 0; i < 4; ++i) {
			in.getline(s, 10);
			for(int j = 0; j < 4; ++j) {
				if(s[j] == 'X')
					x[i][j] = 1;
				else if(s[j] == 'O')
					x[i][j] = -1;
				else if(s[j] == 'T')
					x[i][j] = 0;
				else if(s[j] == '.') {
					not_filled = true;
					x[i][j] = -100;
				}
			}
		}

		in.getline(s, 10);

		out << "Case #" << k << ": ";

		bool x_won = test();
		if(x_won) {
			out << "X won" << endl;
			continue;
		}

		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j) {
				if(x[i][j] == 1)
					x[i][j] = -1;
				else if(x[i][j] == -1)
					x[i][j] = 1;
			}

		bool y_won = test();
		if(y_won) {
			out << "O won" << endl;
			continue;
		}

		out << (not_filled ? "Game has not completed" : "Draw") << endl;
	}

	system("pause");
	return 0;
}

/*

*/
