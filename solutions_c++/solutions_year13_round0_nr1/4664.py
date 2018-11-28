// fstream::open
#include <fstream>
#include <string>

using namespace std;

int main()
{

	fstream filestrIn, filestrOut;
	int cases;
	filestrIn.open("in.txt", fstream::in);
	filestrOut.open("out.txt", fstream::out);

	int currentCases = 1;
	filestrIn >> cases;
	// >> i/o operations here <<

	while (currentCases <= cases) {
		string line[4];
		filestrIn >> line[0] >> line[1] >> line[2] >> line[3];
		char R = '.';
		int ok;
		char goalChar = 'X';

		for (int i = 0; i < 4; i++) {
			int ok = true;
			for (int j = 0; j < 4; j++) {
				if (line[i][j] != 'T' && line[i][j] != goalChar) {
					ok = false;
					break;
				}
			}
			if (ok) {
				R = goalChar;
				goto OUT;
			}
		}

		for (int i = 0; i < 4; i++) {
			int ok = true;
			for (int j = 0; j < 4; j++) {
				if (line[j][i] != 'T' && line[j][i] != goalChar) {
					ok = false;
					break;
				}
			}
			if (ok) {
				R = goalChar;
				goto OUT;
			}
		}


		ok = true;
		for (int j = 0; j < 4; j++) {
			if (line[j][j] != 'T' && line[j][j] != goalChar) {
				ok = false;
				break;
			}
		}
		if (ok) {
			R = goalChar;
			goto OUT;
		}


		ok = true;
		for (int j = 0; j < 4; j++) {
			if (line[j][3 - j] != 'T' && line[j][3 - j] != goalChar) {
				ok = false;
				break;
			}
		}
		if (ok) {
			R = goalChar;
			goto OUT;
		}

		goalChar = 'O';

		for (int i = 0; i < 4; i++) {
			int ok = true;
			for (int j = 0; j < 4; j++) {
				if (line[i][j] != 'T' && line[i][j] != goalChar) {
					ok = false;
					break;
				}
			}
			if (ok) {
				R = goalChar;
				goto OUT;
			}
		}

		for (int i = 0; i < 4; i++) {
			int ok = true;
			for (int j = 0; j < 4; j++) {
				if (line[j][i] != 'T' && line[j][i] != goalChar) {
					ok = false;
					break;
				}
			}
			if (ok) {
				R = goalChar;
				goto OUT;
			}
		}


		ok = true;
		for (int j = 0; j < 4; j++) {
			if (line[j][j] != 'T' && line[j][j] != goalChar) {
				ok = false;
				break;
			}
		}
		if (ok) {
			R = goalChar;
			goto OUT;
		}


		ok = true;
		for (int j = 0; j < 4; j++) {
			if (line[j][3 - j] != 'T' && line[j][3 - j] != goalChar) {
				ok = false;
				break;
			}
		}
		if (ok) {
			R = goalChar;
			goto OUT;
		}

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (line[j][i] == '.') {
					R = 'I';
					goto OUT;
				}
			}
		}

		OUT:
		filestrOut << "Case #" << currentCases << ": ";
		if(R == 'X' || R =='O')
			filestrOut << R << " won\n";
		else if(R == 'I')
			filestrOut << "Game has not completed\n";
		else
			filestrOut << "Draw\n";

		currentCases++;
	}
	filestrIn.close();
	filestrOut.close();

	return 0;
}