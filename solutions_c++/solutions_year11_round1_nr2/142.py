#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <numeric>
#include <utility>
#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;
typedef long long ll;

vector<string> dic[11];
vector<string> allDic;
string l;
int N,M;

int solveCase(const string& word) {
	//cout << "selection:" << word << endl;
	int len = word.length();
	int dicLen = dic[len].size();
	int score = 0;
	vector<bool> live(dicLen, true);
	for(int i = 0; i < 26; ++i) {
		bool found = false;
		for (int j = 0; j < dicLen && !found; ++j) {
			if (!live[j]) continue;
			for (int k = 0; k < len; ++k) {
				if(dic[len][j][k] == l[i]) {
					found = true;
					//cout << j << " " << k << endl;
					break;
				}
			}
		}
		if (!found) {
			continue;
		}
		bool contain = false;
		for (int j = 0; j < len; ++j) {
			if(word[j] == l[i]) {
				contain = true;
				break;
			}
		}
		if (!contain) {
			++score;
		}
		for(int j = 0; j < dicLen; ++j) {
			if (!live[j]) continue;
			for (int k = 0; k < len; ++k) {
				if ((word[k] == l[i]) ^ (dic[len][j][k] == l[i])) {
					live[j] = false;
				}
			}
		}
	}
	return score;
}

void solve(){
	int maxScore = -1;
	string ans;
	for(int i = 0; i < N; ++i) {
		int score = solveCase(allDic[i]);
		if (score > maxScore) {
			maxScore = score;
			ans = allDic[i];
		}
	}
	cout << " " << ans;
}

int main()
{
	int T;
	cin >> T;
	for(int i = 0; i < T; ++i){
		for (int j = 0; j < 11; ++j) {
			dic[j].clear();
		}
		allDic.clear();
		l.clear();
		cin >> N >> M;
		string word;
		for (int j = 0; j < N; ++j) {
			cin >> word;
			allDic.push_back(word);
			dic[word.size()].push_back(word);
		}
		cout << "Case #" << (i+1) << ":";	
		for (int j = 0; j < M; ++j) {
			cin >> l;
			solve();
		}
		cout << endl;
	}
	return 0;
}

