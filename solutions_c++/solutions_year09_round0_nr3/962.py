#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;

ifstream fin("c.in");
ofstream fout("c.out");

#define MOD 10000

int n;

int dp[50][500];

string t,msg,tmp;

int f(int c, int pos) {
	if(dp[c][pos]!=-1)return dp[c][pos];
	if(c==t.size()) {
		dp[c][pos]=1;
		return 1;
	}
	if(pos==msg.size()) {
		dp[c][pos]=0;
		return 0;
	}
	int ret = 0;
	int i;
	for(i=pos;i<msg.size();++i) if(msg[i]==t[c]) {
		ret += f(c+1,i+1);
		ret %= MOD;
	}
	dp[c][pos]=ret;
	return ret;
}

int main() {
	t = "welcome to code jam";
	getline(fin,tmp);
	stringstream sin;
	sin<<tmp;
	sin>>n;
	int test,c,pos;
	for(test=1;test<=n;++test) {
		getline(fin,msg);
		for(c=0;c<=t.size();++c) for(pos=0;pos<=msg.size();++pos) dp[c][pos] = -1;
		int ret = f(0,0);
		sin.clear();
		sin<<ret;
		sin>>tmp;
		while(tmp.size()<4)tmp = "0"+tmp;
		fout<<"Case #"<<test<<": "<<tmp<<endl;
	}
	return 0;
}
