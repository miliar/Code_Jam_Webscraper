#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<sstream>
#include<string>
#include<vector>

using namespace std;
typedef pair<char, int> step;

int B[102], O[102];
int main(){
	int T, N, bt, blen, olen;
	char c;
	string input;
	cin >> T;
	getline(cin, input);
	for(int t = 1; t <= T; t++){
		olen = blen = 1;
		O[0] = B[0] = 1;
		getline(cin, input);
		istringstream is(input);
		is >> N;
		vector<step> v;
		for(int i = 0; i < N; i++){
			is >> c >> bt;
			v.push_back(make_pair(c,bt));
			if(c == 'O')
				O[olen++] = bt;
			else if(c == 'B')
				B[blen++] = bt;
		}
		int ans = 0;
		int oidx = 1, bidx = 1;
		int ocur = 1, bcur = 1, tmp;
		vector<step>::iterator it;
		for(it = v.begin(); it != v.end(); it++){
			c = it->first;
			bt = it->second;
			if(c == 'O'){
				tmp = abs(bt-ocur)+1;
				ans += tmp;
				ocur = bt;
				oidx++;
				if(abs(bcur-B[bidx]) > tmp){
					if(B[bidx] < bcur)
						bcur -= tmp;
					else
						bcur += tmp;
				}
				else{
					bcur = B[bidx];
				}

			}
			else if(c == 'B'){
				tmp = abs(bt-bcur)+1;
				ans += tmp;
				bcur = bt;
				bidx++;
				if(abs(ocur-O[oidx]) > tmp){
					if(O[oidx] < ocur){
						ocur -= tmp;
					}
					else
						ocur += tmp;
				}
				else{
					ocur = O[oidx];
				}
			}
		}
		cout << "Case #" << t << ": " << ans;
		if(t < T) cout << endl;
	}
	return 0;
}
