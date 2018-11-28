#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <cctype>
#include <cstring>
#define MAX 5010
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
	int a, b, c, i, j, k, L, D, N, resp;
	bool flag;
	string patron, cad, v[MAX];
	cin >> L >> D >> N;
	for(i = 0; i < D; i++){
		cin >> v[i];
	}
	getline(cin, patron);
	for(k = 1; k <= N; k++){
		resp = 0;
		for(patron = ""; (c = getchar()) != '\n' && c != EOF; )
			if(!isspace(c))
				patron+=c;
		for(i = 0; i < D; i++){
		//	cout << i << endl;
			j = 0;
			a = 0;
			flag = true;
			while((cad = next(patron, j)) != ""){
			//	cout << cad << endl;
				for(b = cad.size()-1; b >= 0; b--)
					if(cad[b] == v[i][a]){
						a++;
						break;
					}
				if(b < 0){
					flag = false;
					break;
				}
				if(a == L){
					if((cad = next(patron, j)) != ""){
						flag = false;
						break;
					}
					break;
				}
			}
			if(flag && a == L)
				resp++;
		}
		cout << "Case #"<< k << ": "<< resp << endl;
	}
	return 0;
}
