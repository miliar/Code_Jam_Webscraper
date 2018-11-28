#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
#include <fstream>
#include <cstdio>
using namespace std;

int L, D, N;
ifstream in("in.txt");
ofstream out("out.txt");

string str[5001];
string pattern;
bool used[20][30];

int main() {
	in >> L >> D >> N;	
	for(int i = 0; i < D; ++i) {
		in >> str[i];
	}

	for(int i = 0; i < N; ++i) {
		memset(used, false, sizeof(used));
		in >> pattern;
		int start = 0;
		for(int j = 0; pattern[j]; ++j) {
			if(pattern[j] == '(') {
				int v = j + 1;

				while(true) {
					if(pattern[v] == ')') {
						break;
					}
					used[start][pattern[v]-'a'] = true;
					++v;
				}
				j = v;
			} else {
				used[start][pattern[j]-'a'] = true;
			}
			++start;
		}
		int ans = 0;
		for(int k = 0; k < D; ++k) {
			bool flag = true;
			for(int j = 0; str[k][j]; ++j) {
				if(used[j][str[k][j] - 'a'] == false) {
					flag = false;
					break;
				}
			}
			if(flag)
				++ans;
		}
		out << "Case #" << (i+1) << ": " << ans << endl;
		
	}
	return 0;

}