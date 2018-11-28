#include <iostream>
#include <sstream>
using namespace std;


const int MAX_L = 1 << 10;
const string S = "welcome to code jam";
const int S_SZ = 19;
const int MOD = 10000;

int dp[MAX_L][S_SZ];

string int_to_str(int n) {stringstream ss; string ret; ss << n; ss >> ret; return ret;}

int rec(const string & text, int index, int n)
{
int & ret = dp[index][n];
	
	if(0 <= ret) return ret;
	if(n == S_SZ - 1) return ret = 1;
	
	ret = 0;
	
	for(int i = index + 1; i < text.size(); i ++)
		if(text[i] == S[n + 1])
			ret = (ret + rec(text, i, n + 1)) % MOD;
	
	return ret;
}

int main()
{
int Tests;
char buff[MAX_L];
	
	cin >> Tests;
	cin.getline(buff, MAX_L);
	
	for(int test = 1; test <= Tests; test ++)
	{
	string text;
	int ans = 0;
		
		cin.getline(buff, MAX_L);
		text = string(buff);
		
		for(int i = 0; i < MAX_L; i ++)
			for(int j = 0; j < S_SZ; j ++)
				dp[i][j] = - 1;
		
		for(int i = 0; i < text.size(); i ++)
			if(text[i] == S[0])
				ans = (ans + rec(text, i, 0)) % MOD;
		
		string s = int_to_str(ans);
		while(s.size() < 4) s = "0" + s;
		
		cout << "Case #" << test << ": " << s << "\n";
	}
	
//	system("pause");
	
	return 0;
}

/*
TEST 0:
3
elcomew elcome to code jam
wweellccoommee to code qps jam
welcome to codejam

*/
