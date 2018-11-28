#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <fstream>

using namespace std;

int find(string s, string match){	
	int res = 0;
	for(int i = 0; i < s.size(); i++){
		if(s[i] == match[0]){
			if(match.size() > 1){
				string newMatch;
				newMatch = match.substr(1, match.size() - 1);
				string newS;
				newS = s.substr(i + 1, s.size() - i - 1);
				res += find(newS, newMatch);
			}else{
				res++;
			}
		}
	}
	return res % 10000;
}

int main(){

	ifstream ifs("C-small-attempt0.in");
	freopen("out.txt", "wt", stdout);

	string match = "welcome to code jam";
	int n;
	ifs >> n;
	string tmp;
	getline(ifs, tmp);
	
	for(int i=0; i<n; i++){
		string s;
		getline(ifs, s);
		int ans = find(s, match);

		printf("Case #%i: ", i+1);
		for(int i=3; i>0; i--){
			if(ans % (int)pow(10., (double)i) == ans){
				printf("0");
			}
		}
		printf("%i\n", ans);
	}

	return 0;
}