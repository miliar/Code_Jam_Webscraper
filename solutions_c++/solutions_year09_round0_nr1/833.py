#include <iostream>
#include <vector>
#include <string>
using namespace std;

int L, D, N;
vector<string> dic;

int recur(string a, string b) {
	if(a == "" && b == "")
		return 1;
	else if(a[0] != '(') {
		if(a[0] == b[0])
		return recur(a.substr(1), b.substr(1));
	}
	else {
		int ans = 0;
		int i = 1;
		while(a[i] != ')')
			i++;
		string hlp = a.substr(1, i-1);
		a = a.substr(i+1);
		for(int j = 0; j < hlp.size(); j++)
			if(hlp[j] == b[0])
				ans += recur(a, b.substr(1));
		
		return ans;
	}
	return 0;
}

int main() {
	cin >> L >> D >> N;
	for(int i = 0; i < D; i++) {
		string temp;
		cin >> temp;
		dic.push_back(temp);
	}
	
	for(int i = 0; i < N; i++) {
		string temp;
		cin >> temp;
		int sol = 0;
		for(int j = 0; j < D; j++)
			sol += recur(temp, dic[j]);
		cout << "Case #" << i+1 << ": " << sol << endl;
	}
	fflush(stdin); getchar();
	return 0;
}
