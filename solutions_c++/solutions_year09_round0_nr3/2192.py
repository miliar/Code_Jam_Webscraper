#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>

using namespace std;
#define THRESHOLD 10000
int dp[600][25];
	string str = "welcome to code jam";
	string cc;
string toStr(int i){
	stringstream ss;
	ss << i;
	string ret ;
	ss >> ret;
	int len = 4 - ret.size();
	while(len--)ret="0"+ret;
	return ret;
}
int rec(int i,int j){
	if(j == str.size())return 1;
	if(i == cc.size())return 0;
	int& res = dp[i][j];
	if(res != -1)return res;
	res = 0;
	res += rec(i+1,j);
	if(cc[i] == str[j])res += rec(i+1,j+1);
	res %= THRESHOLD;
	return res;
}

int main(){

	int n;
	cin >> n;
	string inp;
	getline(cin,inp);
	int ind = 1;
	while(n --){
		getline(cin,inp);
		cc = inp;
		memset(dp,-1,sizeof dp);
		cout<<"Case #"<<ind<<": "<<toStr(rec(0,0))<<endl;
		ind ++;
	}
	return 0;
}