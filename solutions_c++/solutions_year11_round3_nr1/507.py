#include <iostream>
#include <vector>

using namespace std;

bool fix(vector<string> & p){
	for(int l = 0; l < p.size(); l++){
		for(int c = 0; c < p[l].length(); c++){
			if(p[l][c] == '#'){
				if(l+1 == p.size() || c+1 == p[l+1].length()) return false;
				if(p[l][c+1] != '#' || p[l+1][c] != '#' || p[l+1][c+1] != '#'){
					return false;
				}
				p[l][c] = '/';
				p[l][c+1] = '\\';
				p[l+1][c] = '\\';
				p[l+1][c+1] = '/';
			}
		}
	}
	return true;
}

void solve(int tc){
	int r, c;
	cin >> r >> c;
	string s = "";
	vector<string> p;
	while(s.empty()){
		getline(cin, s);
	}
	p.push_back(s);
	for(int i = 1; i < r; i++){
		getline(cin, s);
		p.push_back(s);
	}
	cout << "Case #" << tc << ": " << endl;
	if(fix(p)){
		for(vector<string>::iterator it = p.begin(); it != p.end(); ++it){
			cout << *it << endl;
		}
	} else cout << "Impossible" << endl;
}

int main(){
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		solve(i+1);
	}
	return 0;
}
