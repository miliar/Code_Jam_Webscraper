#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long LL;

const int codeType = 0;

const int MAXL = 16;
const int MAXD = 5001;
const int MODD = 10000;

long long ans = 0;

int L, D, N;
char tar[MAXL];
vector<string> word;
string patt[MAXL], str;

void cal(const int& curlen) {
	vector<string> ::iterator it;

	if(curlen == L) {
		ans ++;
		return;
	}

	for(int i = 0; i < patt[curlen].length(); i ++) {
		tar[curlen] = patt[curlen][i];
		tar[curlen + 1] = '\0';
		it = lower_bound(word.begin(), word.end(), tar);
		if(it != word.end() && it->length() >= curlen + 1 && it->substr(0, curlen + 1) == tar)
			cal(curlen + 1);
	}
}

int main()
{
	int dep, cas = 1;
	
	if(codeType == 0) {
		freopen("A-small-attempt0.in", "r", stdin);
		freopen("A-small.out", "w", stdout);
	}
	else if(codeType == 1) {
		freopen("A-large.in", "r", stdin);
		freopen("A-large.out", "w", stdout);
	}
	else {
		freopen("input.txt", "r", stdin);
	}
	
	while(cin >> L >> D >> N) {
		word.clear();
		for(int i = 0; i < D; i ++) {
			cin >> str;
			word.push_back(str);
		}
		sort(word.begin(), word.end());

		for(int t = 1; t <= N; t ++) {
			cin >> str;
			for(int i = 0; i < L; i ++)
				patt[i] = "";
			dep = 0;
			for(int i = 0; i < str.length(); dep ++) {
				if(str[i] == '(') {
					for(int j = i + 1; j < str.length() && str[j] != ')'; j ++) {
						i = j + 1;
						patt[dep] += str[j];
					}
					i ++;
				}
				else {
					patt[dep] += str[i];
					i ++;
				}
			}

			ans = 0;
			cal(0);
			cout << "Case #" << t << ": " << ans << endl;
		}
	}	
	
	return 0;
}