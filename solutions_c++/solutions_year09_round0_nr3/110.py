#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;
string s;

string G = "welcome to code jam";
const int MOD = 10000;
int memo[555][555];
int dp(int a,int b)
{
	if(b == G.size()){return 1;}
	if(a==s.size()){return 0;}
	int &ret= memo[a][b];
	if(ret != -1){return ret;}
	ret = dp(a+1,b);
	if(s[a]==G[b])
	{
		ret += dp(a+1,b+1);
		ret %= MOD;
	}
	return ret;
}


int main(void)
{
	int CC;
	cin >> CC;
	getline(cin,s);//dummy
	for(int cn=1;cn <= CC;++cn)
	{
		getline(cin,s);
		memset(memo,-1,sizeof(memo));
		int out = dp(0,0);
		printf("Case #%d: %04d\n",cn,out);
	}
	return 0;
}
