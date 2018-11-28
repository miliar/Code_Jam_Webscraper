#include<iostream>
#include<cstring>
#include<string>
using namespace std;

string s[4];

bool same(char a,char b){
	if (a==b) return true;
	if (b=='T') return true;
	return false;
}

bool check(char c){
	for (int i=0;i<4;i++) {
		bool t1=true,t2=true;
		for (int j=0;j<4;j++) {
			t1&=same(c,s[i][j]);
			t2&=same(c,s[j][i]);
		}
		if (t1|t2) return true;
	}
	bool t1=same(c,s[0][0])&same(c,s[1][1])&same(c,s[2][2])&same(c,s[3][3]);
	bool t2=same(c,s[3][0])&same(c,s[2][1])&same(c,s[1][2])&same(c,s[0][3]);
	if (t1|t2) return true;
	return false;
}

bool checknc(){
	for (int i=0;i<4;i++)
		for (int j=0;j<4;j++)
			if (s[i][j]=='.') return true;
	return false;
}


void solve(){
	for (int i=0;i<4;i++) cin>>s[i];
	if (check('X')) {cout<<"X won\n"; return; }
	if (check('O')) {cout<<"O won\n"; return; }
 	if (checknc()) { cout<<"Game has not completed\n"; return; }
	cout<<"Draw\n";
}

int main(){
	
	freopen("a-large.in","r",stdin);
	freopen("a-large.out","w",stdout);
	
	int T;
	cin>>T;
	for (int cs=1;cs<=T;cs++) {
		cout<<"Case #"<<cs<<": ";
		solve();
	}
	
	
	
	return 0;
}
