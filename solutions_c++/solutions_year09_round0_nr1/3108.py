#include <iostream>
#include <string>
#include <vector>
#include <cstdio>

using namespace std;
#define fors(i, n) for(int i=0, len=n; i<len; ++i)

#define ML 32
#define MD 5120
#define MN 512
int main(){
	int L, D, N;
	cin >> L >> D >> N;
	char strs[MD][ML] = {""};
	fors(i, D) scanf("%s ", strs[i]);
	vector<char> nl[MN];
	fors(k, N){
		string line;
		getline(cin, line);
		int cnt = 0;
		bool multiple = false;
		vector<char> vec;
		fors(s, line.size()){
			if(line[s] == '('){
				multiple = true;
				continue;
			}
			if(line[s] == ')'){
				multiple = false;
				nl[cnt] = vec;
				vec.clear();
				++cnt;
				continue;
			}
			vec.push_back(line[s]);
			if(!multiple){
				nl[cnt] = vec;
				vec.clear();
				++cnt;
			}
		}
		bool isans[MD];
		fors(i, MD) isans[i] = true;
		fors(x, L){
			fors(y, D){
				vector<char> vec = nl[x];
				bool isnow[MD] = {false};
				fors(p, vec.size()){
					if(vec[p] == strs[y][x]){
						isnow[y] = true;
						break;
					}
				}
				if(isans[y] && !isnow[y]) isans[y] = false;
			}
		}
		int ans = 0;
		fors(i, D) if(isans[i]) ++ans;
		cout << "Case #" << k+1 << ": " << ans << endl;
	}
	return 0;
}
