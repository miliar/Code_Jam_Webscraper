#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

//                      1 -- -- -- -- -- -19
const char* PATTERN = "Xwelcome to code jam";
const int MAXINPUT = 500;

const int table_row = 19;
const int table_col = MAXINPUT;
int table[table_row+1][table_col+1];

void run()
{
	string input;
	int casi; cin >> casi; getline(cin, input);
	for (int caso = 1; caso <= casi; caso++)
	{
		getline(cin, input);
		for (int r = 1; r <= table_row; r++) table[r][input.size()] = 0;

		for (int r = 1, ri = table_row; r <= table_row; r++, ri--)
			for (int c = input.size()-1; c >= 0; c--)
			{
				#ifdef DEBUG
					cerr << "Confronto " << input[c] << " || " << PATTERN[ri] << "  r = " << r << ", ri = " << ri << "\n";
				#endif
				if (input[c] == PATTERN[ri]) table[r][c] = (table[r-1][c+1] + table[r][c+1])%10000;
				else table[r][c] = table[r][c+1];
			}

		fprintf(stdout, "Case #%d: %04d\n", caso, table[table_row][0]);
	}
}

int main()
{
	#ifdef DEBUG
		cerr << "Table [" << table_row+1 << ", " << table_col+2 << "]\n";
	#endif
	for (int c = 0; c <= table_col+1; c++) table[0][c] = 1;
	run();
	return 0;
}


