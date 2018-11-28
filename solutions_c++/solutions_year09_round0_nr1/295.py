// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <set>
#include <map>

/////////////////////////
///@author: sakar2003 ///
///@lang: C++         ///
/////////////////////////

using namespace std;

const int MAXN = 5010;

int T;

int L,D,N;
string s[MAXN];
vector<string> vs;
bool b[MAXN];

void predo(string & str){	
	vs.clear();
	for(int i = 0; i < str.size(); ++i){
		string temp;
		if(str[i] == '('){
			for(++i; str[i] != ')'; ++i){
				temp.push_back(str[i]);
			}
		}
		else{			
			temp.push_back(str[i]);
		}
		vs.push_back(temp);
	}
}


int solve(){
	if(vs.size() != L) return 0;

	for(int i = 0; i < D; ++i){
		b[i] = true;
	}
	
	for(int i = 0; i < vs.size(); ++i){
		for(int k = 0; k < D; ++k){
			bool f = false;
			for(int j = 0; !f && j < vs[i].size(); ++j){
				f = f || (vs[i][j] == s[k][i]);
			}
			b[k] = b[k] && f;
		}
	}
	int ans = 0;
	for(int i = 0; i < D; ++i){
		ans += b[i];
	}
	return ans;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("Alarge.txt", "w", stdout);
	//scanf("%d", &T);
	scanf("%d%d%d", &L, &D, &N);
	for(int i = 0; i < D; ++i){
		cin >> s[i];
	}

	for(int tt = 1; tt <= N; ++tt)
	{
		string str;
		cin >> str;
		predo(str);
		printf("Case #%d: %d\n", tt, solve());
	}

	return 0;
}

