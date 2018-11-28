#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cstring>

using namespace std;
typedef pair<char, char> pcc;

int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int caseNum = 1; caseNum <= T; ++caseNum){
		int C, D, N;
		cin >> C;
		map<pcc, char> combine;
		for(int i = 0; i < C; ++i){
			string s;
			cin >> s;
			combine.insert(make_pair(pcc(s[0], s[1]), s[2]));
			combine.insert(make_pair(pcc(s[1], s[0]), s[2]));
		}
		cin >> D;
		int opposedFlags[26] = { 0 };
		for(int i = 0; i < D; ++i){
			string s;
			cin >> s;
			opposedFlags[s[0] - 'A'] |= (1 << (s[1] - 'A'));
			opposedFlags[s[1] - 'A'] |= (1 << (s[0] - 'A'));
		}
		cin >> N;
		int appeared[26] = { 0 };
		string input;
		vector<char> elements;
		cin >> input;
		for(int i = 0; i < input.size(); ++i){
			elements.push_back(input[i]);
			if(elements.size() >= 2){
				map<pcc, char>::iterator it = combine.find(pcc(
					elements[elements.size() - 1], elements[elements.size() - 2]
				));
				if(it != combine.end()){
					--(appeared[elements[elements.size() - 2] - 'A']);
					elements.pop_back();
					elements.pop_back();
					++(appeared[it->second - 'A']);
					elements.push_back(it->second);
					continue;
				}
			}
			++(appeared[input[i] - 'A']);
			int opposed = opposedFlags[input[i] - 'A'];
			for(int j = 0; j < 26; ++j){
				if(appeared[j] > 0 && (opposed & (1 << j))){
					elements.clear();
					memset(appeared, 0, sizeof(appeared));
					break;
				}
			}
		}
		cout << "Case #" << caseNum << ": [";
		for(int i = 0; i < elements.size(); ++i){
			cout << elements[i];
			if(i != elements.size() - 1){
				cout << ", ";
			}
		}
		cout << "]" << endl;
	}
	return 0;
}
