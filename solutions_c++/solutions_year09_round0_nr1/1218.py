#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <stdio.h>
#include <math.h>

using namespace std;

char buffer[1024];

int main() {
	int numtests, len, nw, cnt;
	vector<string> words;
	string w;
	scanf("%d %d %d\n",&len, &nw, &numtests);
	for(int i = 0; i < nw; ++i) {
		gets(buffer);
		words.push_back(buffer);
	}
	for(int t = 1; t <= numtests; ++t) {
		gets(buffer);
		w = buffer;
		cnt = 0;
		vector<vector<bool> > mat(nw,vector<bool>(len));
		vector<string> tok;
		int i = 0;
		while(i < w.size()) {
			if(w[i] == '(') {
				int pos = w.find(')',i);
				tok.push_back(w.substr(i+1,pos - i - 1));
				i = pos + 1;
			}
			else {
				tok.push_back(string(1,w[i]));
				++i;
			}
		}
		for(int i = 0; i < len; ++i)
			for(int j = 0; j < nw; ++j) {
				for(int k = 0; k < tok[i].size(); ++k)
					if((i == 0 || mat[j][i-1] == 1) && words[j][i] == tok[i][k])
						mat[j][i] = 1;
			}
		for(int i = 0; i < nw; ++i)
			if(mat[i].back() == 1)
				++cnt;
		cout << "Case #" << t << ": " << cnt << endl;
	}
	return 0;
}
