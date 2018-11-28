#include <map>
#include <cmath>
#include <queue>
#include <ctime>
#include <string>
#include <vector>
#include <fstream>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

int main(int argc, char **argv) {

    ios::sync_with_stdio(false);
	int t;
	string in;
    char *b = "yhesocvxduiglbkrztnwjpfmaq";

	ifstream cin("A-small-attempt2.in");
	ofstream cout("A-small-attempt.out");

	cin >> t;
	cin.ignore();
	for(int i = 1; i <= t; ++i) {
		getline(cin, in);
		cout << "Case #" << i << ": ";
		for(int j = 0; j < in.length(); ++j) {
			if(in[j] == ' ')
				cout << " ";
			else
				cout << b[in[j] - 97];
		}
		cout << endl;
	}
    return 0;
}