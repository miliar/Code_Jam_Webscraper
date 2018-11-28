#include<iostream>
#include<queue>
#include<vector>
#include<string>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<map>
#include<set>
#define pb push_back
#define INF (1 << 28)
#define EPS (1e-9)
#define mp(x,y) make_pair(x,y)
#define rep(i,n) for(int i = 0; i < n; i++)
#define REP(i,n) for(int i = 0; i <= n; i++)



using namespace std;

int main(){
	int n;
	cin >> n;
	string replace = "yhesocvxduiglbkrztnwjpfmaq";
	cin.ignore();
	for(int T = 1; T <= n; T++){
		string s;
		getline(cin,s);
		string ans = "";
		for(int i = 0; i < s.size(); i++){
			if(s[i] == ' ')ans += " ";
			else ans += replace[s[i] - 'a'];
		}
		cout << "Case #" << T << ": " << ans << endl;  	
		
	}
	return 0;
}

