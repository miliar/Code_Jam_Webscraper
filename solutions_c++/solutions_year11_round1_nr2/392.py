								/* in the name of Allah */
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <cstdio>
#include <cmath>
#include <map>

using namespace std;

ifstream fin("B_The Killer Word.in");
ofstream fout("B_The Killer Word.out");

#define cin fin
#define cout fout

int n, m;
string d[110];
string ls;
bool mark[110];
bool hv[110][30];

int calc(int idx, string ls){
	memset(mark, false, sizeof mark);
	string w = d[idx];
	int ret = 0;
	for(int i = 0; i < n; i++)
		if(d[i].length() != w.length())
			mark[i] = true;
	int rem = w.length();
	for(int i = 0; rem && i < 26; i++){
		char ch = ls[i];
		if(hv[idx][ch - 'a']){
			for(int j = 0; j < w.length(); j++)
				if(w[j] == ch)
					rem--;
			for(int j = 0; j < n; j++){
				if(mark[j]) continue;
				for(int k = 0; k < w.length(); k++){
					if((w[k] == ch && d[j][k] != ch) || (w[k] != ch && d[j][k] == ch)){
						mark[j] = true;
						break;
					}
				}
			}
		}
		else{
			bool fl = false;
			for(int j = 0; j < n; j++){
				if(mark[j]) continue;
				if(hv[j][ch - 'a']){
					mark[j] = true;
					fl = true;
				}
			}
			if(fl) ret++;
		}
		//cout << i << ' ' << rem << ' ' << ret << ' ' << ch << endl;
	}
	return ret;
}

int main(){
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> n >> m;
		memset(hv, false, sizeof hv);
		for(int i = 0; i < n; i++){
			cin >> d[i];
			for(int j = 0; j < d[i].length(); j++)
				hv[i][d[i][j] - 'a'] = true;
		}
		cout << "Case #" << ++test << ":";
		for(int i = 0; i < m; i++){
			cin >> ls;
			string res = d[0];
			int mx = 0;
			for(int j = 0; j < n; j++){
				int t = calc(j, ls);
				if(t > mx){
					mx = t;
					res = d[j];
				}
				//cerr << j << ' ' << t << endl;
			}
			cout << ' ' << res;
		}
		cout << endl;
	}
	return 0;
}