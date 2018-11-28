#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>

using namespace std;

int size = 'z'-'a'+1;
char dict['z'-'a'+1] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	vector<string> v;
	string temp;
	int n = 0;
	/*
	dict['z'-'a'] = 'q';
	dict['q'-'a'] = 'z';
	for (int i = 0; i < 23; i++) {
		cin >> temp;
		v.push_back(temp);
	}


	for (int i = 0; i < v.size(); i++) {
		cin >> temp;
		for (int j = 0; j < temp.length(); j++)
			dict[v[i][j] - 'a'] = temp[j];
	}	

	for (int i = 0; i < 'z' - 'a' + 1; i++) {
		// cout << (char)(i + 'a') << " " << dict[i] << endl;
		cout << "'" << dict[i] << "', ";
	}
	*/
	cin >> n;
	for (int i = 0; i < n;) {
		getline(cin, temp);
		if (temp == "")
			continue;
		
		for (int j = 0; j < temp.length(); j++)
			if (temp[j] >= 'a' && temp[j] <= 'z')
				temp[j] = dict[temp[j]-'a'];
		cout << "Case #" << i+1 << ": " << temp << endl;
		i++;
	}

	return 0;
}