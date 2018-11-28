#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

map< pair<char,char>, char> comb;
map<char, char> oppos;
vector<char> elms;

int main(int argc, char *argv[]){
	int T, C, D, N;
	cin >> T;
	for (int t = 1; t <= T; t++){
		comb.clear();
		oppos.clear();
		elms.clear();

		cin >> C;
		string buf;
		while(C--){
			cin >> buf;
			comb[make_pair(buf[0],buf[1])] = buf[2];
			comb[make_pair(buf[1],buf[0])] = buf[2];
		}
		cin >> D;
		while (D--){
			cin >> buf;
			oppos[buf[0]] = buf[1];
			oppos[buf[1]] = buf[0];
		}
		cin >> N;
		cin >> buf;
		string::iterator c = buf.begin();
		while (N--){
			elms.push_back(*c); c++;
			if (elms.size() < 2) continue;
			pair<char, char> p = make_pair(elms.back(), elms[elms.size()-2]);
			if (comb.find(p) != comb.end()){
				elms.pop_back();
				elms.back() = comb[p];
			}
			else {
				if (oppos.find(elms.back()) != oppos.end() && find(elms.begin(), elms.end(), oppos[elms.back()]) != elms.end()){
					elms.clear();

				}
			}
		}
		cout << "Case #" << t << ": [";
		for (int i = 0; i+1 < elms.size(); i++)
			cout << elms[i] << ", ";
		if (!elms.empty()) cout << elms.back();
		cout << "]" << endl;
	}
	return 0;
}


