#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int check(const string& s)
{
	if(find(s.begin(),s.end(),'.') != s.end()){
		return 0;
	}
	else if(find(s.begin(),s.end(),'X') == s.end()){
		return 1;
	}
	else if(find(s.begin(),s.end(),'O') == s.end()){
		return 2;
	}
	else {
		return -1;
	}
}

int main()
{
	int n;
	cin >> n;
	string s[4],temp;
	char str[5] = {};
	
	for(int i = 1; i <= n; ++i){
		int t = -1;
		for(int j = 0; j < 4; ++j){
			cin >> s[j];
		}
		for(int j = 0; j < 4; ++j){
			t = max(t,check(s[j]));
		}	
		for(int j = 0; j < 4; ++j){
			for(int k = 0; k < 4; ++k){
				str[k] = s[k][j];
			}
			temp = str;
			t = max(t,check(temp));
		}
		for(int j = 0; j < 4; ++j){
			str[j] = s[j][j];
		}
		temp = str;
		t = max(t,check(temp));
		
		for(int j = 0; j < 4; ++j){
			str[j] = s[3 - j][j];
		}
		temp = str;
		t = max(t,check(temp));
		
		if(t == 1){
			cout << "Case #" << i << ": O won" << endl;
			continue;
		}
		else if(t == 2){
			cout << "Case #" << i << ": X won" << endl;
			continue;
		}
		else if(t == 0){
			cout << "Case #" << i << ": Game has not completed" << endl;
			continue;
		}
		else {
			cout << "Case #" << i << ": Draw" << endl;
			continue;
		}
	}
}