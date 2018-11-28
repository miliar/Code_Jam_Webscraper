#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<string> vs;

#define PB push_back
const long double PI = 3.1415926535897932384626433832795;

int main(int argc, char *argv[])
{
	ifstream myfile;
	myfile.open(argv[1]);
	int num_tc, tmp, num_buttons;
	myfile >> num_tc;
	vi orange, blue, seqVal;
	vector<char> seqCol;
	char col;

	for (int i=0; i<num_tc; ++i) {
		orange.clear();	blue.clear();
		seqVal.clear(); seqCol.clear();
		myfile >> num_buttons;
		for (int loop=0; loop < num_buttons; ++loop) {
			myfile >> col;
			myfile >> tmp;
			if (col == 'B') {
				blue.push_back(tmp);
			} else {
				orange.push_back(tmp);
			}
			seqVal.push_back(tmp);
			seqCol.push_back(col);
		}
		vi::iterator or_it = orange.begin(), bl_it = blue.begin(), seqVal_it = seqVal.begin();
		vector<char>::iterator seqCol_it = seqCol.begin();
		int result = 0, cur_blue = 1, cur_orange = 1;
		while (seqCol_it != seqCol.end()) {
			int button_pressed = 0;
			if (*seqCol_it == 'B' and *seqVal_it == cur_blue) {
				//press button
				++seqCol_it, ++seqVal_it, ++bl_it;
				button_pressed = 1;
			} else {
				if (cur_blue != *bl_it) {
					if (*bl_it > cur_blue) ++cur_blue;
					else --cur_blue;
				}
			}

			if (*seqCol_it == 'O' and *seqVal_it == cur_orange) {
				if (!button_pressed)	++seqCol_it, ++seqVal_it, ++or_it;
			} else {
				if (cur_orange != *or_it) {
					if (*or_it > cur_orange) ++cur_orange;
					else --cur_orange;
				}
			}
			++result;
		}
		cout << "Case #" << i + 1 << ": " << result << "\n";
	}
	myfile.close();
	return 0;
}

