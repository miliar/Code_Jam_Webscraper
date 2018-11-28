#include <iostream>
#include <cstdlib>
#include <string>
#include <map>

using namespace std;

int main()
{
	string input;
	getline(cin, input);

	unsigned T = atoi(input.c_str());

	for (unsigned i = 0; i < T; i++)
	{
		bool x_win = false, o_win = false, incomplete = false;
		
		map<string, int> win_hash;

		// Grab board input row by row
		for (unsigned j = 0; j < 4; j++)
		{
			string row;
			while (row == "") getline(cin, row);

			if (x_win || o_win) continue;

			// Track possible x wins and o wins
			for (unsigned k = 0; k < 4; k++)
			{
				if (row[k] == 'X' || row[k] == 'T')
				{
					win_hash["rowx"]++;
					if (k == j) win_hash["diagx1"]++;
					if (k + j == 3) win_hash["diagx2"]++;
					win_hash[string("colx") + char('1' + k)]++;
				}
				if (row[k] == 'O' || row[k] == 'T')
				{
					win_hash["rowo"]++;
					if (k == j) win_hash["diago1"]++;
					if (k + j == 3) win_hash["diago2"]++;
					win_hash[string("colo") + char('1' + k)]++;
				}
				if (row[k] == '.') incomplete = true;
			}

			/* debug:
			cout << "row " << (j+1) << " x hash:" << endl;
			cout << "rowx: " << win_hash["rowx"] << endl;
			cout << "diagx1: " << win_hash["diagx1"] << endl;
			cout << "diagx2: " << win_hash["diagx2"] << endl;
			cout << "colx1: " << win_hash["colx1"] << endl;
			cout << "colx2: " << win_hash["colx2"] << endl;
			cout << "colx3: " << win_hash["colx3"] << endl;
			cout << "colx4: " << win_hash["colx4"] << endl;
			cout << endl;
			*/

			// Check x/o win conditions
			if (win_hash["rowx"] == 4) x_win = true;
			else if (win_hash["rowo"] == 4) o_win = true;

			// Reset row check
			win_hash["rowx"] = win_hash["rowo"] = 0;
		}

		if (win_hash["diagx1"] == 4 || win_hash["diagx2"] == 4) x_win = true;
		else if (win_hash["colx1"] == 4 || win_hash["colx2"] == 4 || win_hash["colx3"] == 4 || win_hash["colx4"] == 4) x_win = true;
		if (win_hash["diago1"] == 4 || win_hash["diago2"] == 4) o_win = true;
		else if (win_hash["colo1"] == 4 || win_hash["colo2"] == 4 || win_hash["colo3"] == 4 || win_hash["colo4"] == 4) o_win = true;
		
		cout << "Case #" << i + 1 << ": ";
		if (x_win) cout << "X won" << endl;
		else if (o_win) cout << "O won" << endl;
		else if (incomplete) cout << "Game has not completed" << endl;
		else cout << "Draw" << endl;
	}

	return 0;
}
