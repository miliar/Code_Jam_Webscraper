#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <cctype>
#include <cstring>
#include <queue>
#include <stack>
#define x first
#define y second
#define MOD 10000
#define MAX 503
using namespace std;

string next(string s, int &i){
	string r = "";
	if(i == s.size())
		return r;
	if(s[i] == '('){
		i++;
		while(s[i] != ')'){
			r+=s[i];
			i++;
		}
		i++;
		return r;
	}
	r = s[i];
	i++;
	return r;
}

int main(){
	int i, j, k, a, b, f, c, N, m[25][MAX];
	string s, t = "welcome to code jam";
	f = t.size();
	cin >> N;
	getline(cin, s);
	for(k = 1; k <= N; k++){
		getline(cin, s);
		c = s.size();
		if(s[0] == t[0])
			m[0][0] = 1;
		else
			m[0][0] = 0;
		for(i = 1; i < c; i++){
			if(s[i] == t[0])
				m[0][i] = m[0][i-1]+1;
			else
				m[0][i] = m[0][i-1];
		}
		for(i = 1; i < f; i++){
			m[i][0] = 0;
			for(j = 1; j < c; j++){
				if(t[i] == s[j]){
					for(a = j-1; a >= 0; a--)
						if(t[i-1] == s[a])
							break;
					if(a < 0)
						m[i][j] = m[i][j-1];
					else
						m[i][j] = (m[i][j-1]+m[i-1][a])%MOD;
				}
				else
					m[i][j] = m[i][j-1];
			}
		}
/*		for(i = 0; i < f; i++){
			for(j = 0; j < c; j++)
				cout << m[i][j] << " ";
			cout << endl;
		}*/
		printf("Case #%d: %04d\n", k, m[f-1][c-1]);
	}
	return 0;
}
