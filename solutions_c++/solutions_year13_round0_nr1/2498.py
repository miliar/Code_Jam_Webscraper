#include <iostream>
#include <cstdio>
#include <algorithm>
#include <utility>

using namespace std;


int main()
{
	int runs;
	cin >> runs;
	getchar();
	
	int cols[4][2];
	int lines[4][2];
	int diagos[2][2];
	
	for (int run=0; run<runs; ++run) {
		fill(&cols[0][0], &cols[4][2], 0);
		fill(&lines[0][0], &lines[4][2], 0);
		fill(&diagos[0][0], &diagos[2][2], 0);
		int s = 16;
		for (int l=0; l<4; ++l) {
			for (int c=0; c<4; ++c) {
				char a = getchar();
				//cout << a;
				switch (a) {
					case 'X':
						++cols[c][0];
						++lines[l][0];
						if (l==c)
							++diagos[0][0];
						if (l==3-c)
							++diagos[1][0];
					break;
					case 'O':
						++cols[c][1];
						++lines[l][1];
						if (l==c)
							++diagos[0][1];
						if (l==3-c)
							++diagos[1][1];
					break;
					case 'T':
						++cols[c][0];
						++lines[l][0];
						++cols[c][1];
						++lines[l][1];
						if (l==c) {
							++diagos[0][0];
							++diagos[0][1];
						}
						if (l==3-c) {
							++diagos[1][0];
							++diagos[1][1];
						}
					break;
					case '.':
						--s;
					break;
					default:
						--s;
						cerr << "invalid char : " << a << endl;
				}
			}
			//cout << endl;
			getchar();
		}
		//cout << endl;
		getchar();
		bool xwin = false;
		bool owin = false;
		for (int i=0; i<2; ++i) {
			if (diagos[i][0] == 4)
				xwin = true;
			if (diagos[i][1] == 4)
				owin = true;
		}
		for (int i=0; i<4; ++i) {
			//cout << cols[i][0] << " " << lines[i][0] << endl;
			//cout << cols[i][1] << " " << lines[i][1] << endl;
			if (cols[i][0] == 4 or lines[i][0] == 4)
				xwin = true;
			if (cols[i][1] == 4 or lines[i][1] == 4)
				owin = true;
		}
		cout << "Case #" << run+1 << ": ";
		if (xwin and owin)
			cout << "Draw";
		else if (xwin)
			cout << "X won";
		else if (owin)
			cout << "O won";
		else if (s == 16)
			cout << "Draw";
		else
			cout << "Game has not completed";
		cout << endl;
	}
	
	return 0;
	
}

