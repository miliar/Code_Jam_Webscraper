#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

int ans[502][21];
const string ref = "welcome to code jam";
map<char, vector<int> > dic;


int main(int argc, _TCHAR* argv[])
{
	ifstream cin("test__.in");
	ofstream fout("test__.out");

	int n;
	cin >> n; 
	
	char buff[600];
	cin.getline(buff, 600);
	
	for (int i = 0; i < ref.size(); ++i)
		dic[ref[i]].push_back(i+1);

	for (int i = 0; i < n; ++i) {
		cin.getline(buff, 600);
		int length = strlen(buff);

		for (int j = 0; j < length; ++j)
			for (int k = 0; k < 20; ++k)
				ans[j][k] = 0;

		if (buff[0] == 'w') 
			ans[0][1] = 1;
		
		for (int j = 1; j < strlen(buff); ++j) {
			if (buff[j] == 'w')
				ans[j][1] += 1;
			else {
				vector <int> tdic = dic[buff[j]];
				if (tdic.size() > 0) {
					for (int k = 0; k < tdic.size(); ++k) {
						ans[j][tdic[k]] += ans[j-1][tdic[k]-1];
					}
				}
			}

			for (int k = 1; k < 20; ++k) {
				ans[j][k] += ans[j-1][k];
				ans[j][k] %= 10000;
			}
		}

//		long long ccount = 0;
//		for (int j = 0; j < length; ++j) {
//			ccount += ans[j][19];
//			ccount %= 10000;
//		} 
		int ccount = ans[length-1][19];


		
		fout << "Case #" << i+1 << ": ";
		cout << "Case #" << i+1 << ": ";
		if (ccount == 0) {
			fout << "0000" << endl;
			cout << "0000" << endl;
		} else {
			for (int j = 3; j > int(log10((double)ccount)); --j) {
				fout << '0';
				cout << '0';
			}
			cout << ccount << endl;
			fout << ccount << endl;
		}
	}
	
	return 0;
}

