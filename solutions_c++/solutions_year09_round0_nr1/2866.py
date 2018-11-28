#include <iostream>
#include <vector>
#include <string>

using namespace std;

int matchp(string w, string p) {

	int i, j, pos = 0;;
	bool zat = false;
	bool match = false;
	
	while ( i < p.length() ) {
	
		if (p[i] == '(') {
		
			match = false;
		
			while ( p[i] != ')' ) {
			
				if (p[i] == w[pos] && match == false) {
					match = true;
				}
				
				i++;
			
			}
			
			if (match == false) 
				return 0;
		
		}
		
		if (p[i] != w[pos] && p[i] != ')') {
			return 0;
		}
		
		pos++;
		i++;
	
	}
	
	return 1;
	
}

int main() {

	int n,l,d;
	int i,j, res;
	vector<string> wrds(0);
	string patt;
	string tmp;
	
	cin >> l;
	cin >> d;
	cin >> n;
	
	for (i = 0; i <= d; i++) {
	
		std::getline(cin,tmp);
		
		wrds.push_back(tmp);
	
	}
	
	for (i = 0; i < n; i++) {
	
		res = 0;
	
		std::getline(cin,patt);
		
		for ( j = 1; j < wrds.size(); j++) {
		
			res += matchp(wrds[j], patt);
		}
		
		cout << "Case #" << i + 1 << ": " << res << endl;
	
	}

	return 0;
};
