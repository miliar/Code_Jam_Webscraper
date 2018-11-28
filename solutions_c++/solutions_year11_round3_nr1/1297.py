#include <iostream>
#include <vector>

using namespace std;


struct Row {
	string line;
	int sharp_c;
};

bool checkLine(string & s) {
	
	for (int i=0; i<s.length(); i++) {
		if (s[i] == '#' && i<s.length() && s[i+1] != '#') return false;
		else if (s[i] == '#' && i<s.length() && s[i+1] == '#') i++; 
	}
	
	return true;
}

int getSharpCount(string & s) {
	int count=0;
	
	for (int i=0; i<s.length(); i++) {
		if (s[i] == '#') count++;
	}
	
	return count;
}

int main() {
	
	int T, R, C;
	
	cin >> T;
	
	for (int i=0; i<T; i++) {
		cin >> R >> C;
		
		Row row[R];
		char out[R][C+1];
		int sharp_c=0;
		
		getline(cin, row[0].line);
		for (int j=0; j<R; j++) {
			getline(cin, row[j].line);
			
			row[j].sharp_c = getSharpCount(row[j].line);
			sharp_c += row[j].sharp_c;
		}
		
		cout << "Case #" << (i+1) << ":\n";
		if (sharp_c == 0) {
			for (int j=0; j<R; j++) cout << row[j].line << "\n";
		}
		else if ((sharp_c % 4) != 0) cout << "Impossible\n";
		else {
			for (int j=0; j<R; j++) {
				if (!checkLine(row[j].line )) {					
					cout << "Impossible\n";
					break;
				}
				
				for (int j=0; j<R; j++) {
					for (int k=0; k<row[j].line.length(); k++) {
						if (row[j].line[k] == '.') out[j][k] =  '.';
						else if (row[j].line[k] == '\\'
											|| row[j].line[k] == '/') continue;
						else {
							if (j<R && row[j+1].line[k] == '#' && row[j+1].line[k+1] == '#') {
								 row[j].line[k] = '/';
								 row[j].line[k+1] = '\\';
								 row[j+1].line[k] = '\\';
								 row[j+1].line[k+1] = '/';
								 
								 out[j][k] = '/';
								 out[j][k+1] = '\\';
								 out[j+1][k] = '\\';
								 out[j+1][k+1] = '/';
								 
								 k++;
							}
							else if (j>=R) {
								cout << "Impossible\n";
								goto out;
							}
							else if (row[j+1].line[k] == '#' && row[j+1].line[k+1] != '#') {
								cout << "Impossible\n";
								goto out;
							}
						}
					}
				}
			}
			
			for (int j=0; j<R; j++) {
				out[j][C] = '\0';
				cout << out[j] << "\n";
			}
		}
		out:;
	}
}
