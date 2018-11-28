#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
using namespace std;
char elem[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
char op[8];
char comb[8][2];
int getId(char c){
	for(int i = 0; i < 8; i++){
		if(c == elem[i])
			return i;
	}
	return -1;
}
int main(){
	int T, C, D, N;
	char s[101];
	vector<char> v;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		memset(comb, 0, sizeof(comb));
		memset(op, 0, sizeof(op));
		scanf("%d", &C);
		for(int c = 0; c < C; c++){
			scanf("%s", s);
			int i = getId(s[0]);
			int j = getId(s[1]);
			comb[i][0] = s[1];
			comb[i][1] = s[2];
			comb[j][0] = s[0];
			comb[j][1] = s[2];
		}
		scanf("%d", &D);
		for(int d = 0; d < D; d++){
			scanf("%s",s);
			int i = getId(s[0]);
			int j = getId(s[1]);
			op[i] = s[1];
			op[j] = s[0];
		}
		scanf("%d", &N);
		scanf("%s", s);

		v.clear();
		for(int i = 0; i < N; i++){
			if(v.empty()){
				v.push_back(s[i]);
				continue;
			}
			if(comb[getId(s[i])][0] != 0 && comb[getId(s[i])][0] == v.back()){
				v.pop_back();
				v.push_back(comb[getId(s[i])][1]);
				continue;
			}
			char tmp = op[getId(s[i])];
			if(tmp != 0){
				if(find(v.begin(), v.end(), tmp) != v.end()){
					v.clear();
					continue;
				}
				else{
					v.push_back(s[i]);
					continue;
				}
			}

			v.push_back(s[i]);
		}
		cout << "Case #" << t << ": " << "[";
		if(v.empty())
			cout << "]";
		else{
			for(int i = 0; i < v.size()-1; i++){
				cout << v[i] << ", ";
			}
			cout << v[v.size()-1] << "]";
		}
		if(t < T)
			cout << endl;
	}
	return 0;
}
