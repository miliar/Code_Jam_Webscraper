#include<iostream>
using namespace std;
char c[256][256];
char d[256][256];
string sub(string str,int beg,int end) {
	string ans = "";
	if (end <0) return ans;
	while(beg<=end) {
		ans += str[beg++];
	}
	return ans;
	
}
bool check(string ans) {
	for(int i = 0;i < ans.size(); i ++) {
		for(int j = i+1; j < ans.size(); j ++) {
			if(d[ans[i]][ans[j]]) return 1;
		}
	}
	return 0;
}
int main() {
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	int t;
	cin >> t;
	for(int cas = 1; cas <=t; cas ++) {
		int C;
		cin >>C;
		for(int i = 0; i < 256; i ++) {
			for(int j = 0; j < 256;j++) {
				c[i][j]= d[i][j] =0;
			}
		}
		string str;
		while(C--) {
			
			cin>> str;
			c[str[0]][str[1]]=str[2];
			c[str[1]][str[0]]=str[2];
		}
		int D;
		cin >> D;
		while(D--) {
			cin >>str;
			d[str[0]][str[1]] =1;
			d[str[1]][str[0]] =1;
		}
		cin >>D;
		cin >> str;
		string ans;		
		ans = "";
		int len;
		
		for(int i = 0;i < str.size(); i ++) {
			
			ans += str[i];
			len = ans.size();
			if(len >=2) {
				if (c[ans[len-1]][ans[len-2]]) {
					ans = sub(ans,0,len-3) + c[ans[len-1]][ans[len-2]];					
				}
				if(check(ans)) ans = "";
			}
			
		}
		cout <<"Case #"<<cas<<": [";
		for(int i = 0; i< ans.size(); i ++) {
			if(i) cout <<", ";
			cout << ans[i];
			
			
		}
		cout <<"]" <<endl;
		
	}
	return 0;
}
