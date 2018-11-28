#include <iostream>
#include <set>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	for(int c = 1; c <= cases; c++) {
		int mkdir_count = 0;
		int n, m;
		cin >> n >> m;
		
		set<string> existed;
		string input_path;

		existed.insert("/");
		for(int i = 0; i < n; i++) {
			cin >> input_path;
			existed.insert(input_path);
		}
		
		for(int i = 0; i < m; i++) {
			cin >> input_path;

			if(existed.find(input_path) != existed.end()) continue;

			string basedir;
			for(int j = input_path.find('/', 1); 
					j < input_path.size();
					j = input_path.find('/', j + 1)) {
				basedir = input_path.substr(0, j);

				if(existed.find(basedir) == existed.end()) {
					mkdir_count++;
					existed.insert(basedir);
				}
			}
			mkdir_count++;
			existed.insert(input_path);
		}

		cout << "Case #" << c << ": " << mkdir_count << endl;
	}
	return 0;
}
