#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
	freopen("in.in", "r", stdin);
	string english = "abcdefghijklmnopqrstuvwxyz";
	string google =  "yhesocvxduiglbkrztnwjpfmaq";
	map<char, char> key;
	for(int i = 0; i < 26; i++){
		key[english[i]] = google[i];
	}
	string str;
	int T;
	cin >> T;
	cin.ignore();
	for(int c = 1; c <= T; c++){
		getline(cin, str);
		istringstream iss(str);
		string word;
		cout << "Case #" << c << ":";
		while(iss >> word){
			cout << " ";
			for(int i = 0; i < (int)word.length(); i++){
				cout << key[word[i]];
			}
		}
		cout << endl;
	}
	return 0;
}

