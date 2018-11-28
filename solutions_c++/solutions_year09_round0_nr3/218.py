/*
 * C.cpp
 *
 *  Created on: Sep 3, 2009
 *      Author: Amr
 */


#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <complex>
using namespace std;

string s;
string jj = "welcome to code jam";

int memo[510][20];

int dp(int i, int j){
	//cout << i << " " << j << endl;
	if( j == jj.size() )
		return 1;
	if( i == s.size() )
		return 0;
	if( memo[i][j] != -1)
		return memo[i][j];
	memo[i][j] = 0;
	if( s[i] == jj[j] )
		memo[i][j] = (dp(i+1,j+1))%10000;
	memo[i][j] += (dp(i+1,j))%10000;
	memo[i][j] %= 10000;
	return memo[i][j];
}

int main()
{
	freopen("C-large.in","rt",stdin);
	freopen("C.out","wt",stdout);
	int t;
	scanf("%d ",&t);
	int ii = 1;
	while(t--){
		getline(cin,s);
		memset(memo,-1,sizeof memo);
		//cout << s << "\n" << jj << endl;
		printf("Case #%d: %04d\n",ii++,dp(0,0));
	}
	return 0;
}
