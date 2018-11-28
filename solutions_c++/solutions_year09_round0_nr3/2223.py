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
int dp[1000][50];

string toStr(int i){
stringstream ss;
ss << i;
string ret ;
ss >> ret;
int len = 4 - ret.size();
while(len--)ret="0"+ret;
return ret;
}
int main(){
string str = "welcome to code jam";
int n;
cin >> n;
string inp;
getline(cin,inp);
int ind = 1;
while(n --){
getline(cin,inp);
// cout<<inp<<endl;
memset(dp,-1,sizeof dp);
int i,j,k;
for(i = 0; i < inp.size(); ++i){
for(j = 0; j < str.size(); ++j){
if(inp[i] == str[j]){

if(j == 0){
dp[i][0] = 1;
}
else{
dp[i][j] = 0;
for(k = 0; k < i; ++k){
if(dp[k][j-1] != -1)dp[i][j] = (dp[i][j] + dp[k][j-1])%THRESHOLD;
}
if(dp[i][j] == 0)dp[i][j] = -1;
}
// cout<<i<<" "<<j<<" "<<dp[i][j]<<endl;
}
}
}
int res = 0;
for(i = 0; i < inp.size(); ++i){
if(dp[i][18] != -1)res = (res + dp[i][18])%THRESHOLD;
}
cout<<"Case #"<<ind<<": "<<toStr(res)<<endl;
ind ++;
}
return 0;
}
