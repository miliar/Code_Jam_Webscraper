
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

int rec_find(int i, string b, vector< vector<char> > &ps, vector<string> &v) {
	if( i >= ps.size() ) {
		if( v.size() == 0 ) {
			cout << b << endl;
			exit(1);
		}

		if( v.size() > 1 ) cout << "NASTY!" << endl;
		return v.size();
	}

	int sum = 0;
	for(int j = 0; j < ps[i].size(); j++) {
		vector<string> newv = vector<string>();
		string n = b+ps[i][j];

		for(int k = 0; k < v.size(); k++) {
			if( v[k].substr(0,i+1).compare(n) == 0 ) newv.push_back(v[k]);
		}
		//for(int j = 0; j < newv.size(); j++) cout << v[j] << endl;
		
		if( newv.size() > 0 )
			sum += rec_find(i+1, n, ps, newv);
	}

	return sum;
}

int main() 
{
	int L, D, N;

	cin >> L >> D >> N;

	vector<string> v = vector<string>(D, string(' ', L));

	for(int i = 0; i < D; i++) {
		cin >> v[i];
		//cout << v[i] << endl;
	}

	vector< vector<char> > ps = vector< vector<char> >(L, vector<char>());
	for(int i = 0; i < N; i++) {
		//cout << "case " << i+1 << endl;
		for(int j = 0; j < L; j++) {
			char c;
			cin >> c;
			if(c == '(') {
				cin >> c;
				while(c != ')') {
					for(int k = 0; k < D; k++) {
						if( v[k][j] == c ) {
							ps[j].push_back(c);
							break;
						}
					}
					cin >> c;
				}
			}
			else {
				for(int k = 0; k < D; k++) {
					if( v[k][j] == c ) {
						ps[j].push_back(c);
						break;
					}
				}
			}
			//cout << "possibles " << j << ": " << ps[j].size() << endl;
		}
		//cout << "read input" << endl;

		int possibles = rec_find(0, "", ps, v);
		cout << "Case #" << i+1 << ": " << possibles << endl;

		for(int j = 0; j < L; j++) ps[j].clear();
	}
	

	return 0;
}


