/*
 * A.cpp
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




struct node{
	int child[26];
	int nChild;
	node(){
		memset(child,-1,sizeof child);
	}

};

node* all[75010];
int cur = 0;

void build(char* s,int n){
		if(!(*s) ) return;
		if(all[n]->child[(*s)-'a']==-1){
			all[n]->nChild++,all[n]->child[(*s)-'a'] = cur++;
			all[all[n]->child[(*s)-'a']] = new node();
		}
		build(s+1,all[n]->child[(*s)-'a']);
	}

char words[5001][16];

void dfs(int n,string cur){
	bool f = 0;
	for (int i = 0; i < 26; ++i) {
		if(all[n]->child[i]!=-1){
			string l = cur;
			l += (i+'a');
			dfs(all[n]->child[i],l);
			f = 1;
		}
	}
	if(!f)
		cout << cur << endl;
}

string s;

int memo[75010][3000];

int dp(int n,int i){
	if( i == s.size() )
		return 1;
	if( all[n]->nChild == 0 )
		return 0;
	if(memo[n][i] != -1)
		return memo[n][i];
	int sum = 0;
	int oldi = i;
	if( s[i]== '(' ){
		i++;
		int j = i;
		for (; j < s.size(); j++) {
			if(s[j] ==')')
				break;
		}
		while(s[i] != ')' ){
			if(all[n]->child[s[i]-'a'] != -1)
				sum += dp(all[n]->child[s[i]-'a'],j+1);
			i++;
		}
	}
	else{
		if(all[n]->child[s[i]-'a'] != -1)
			sum = dp(all[n]->child[s[i]-'a'],i+1);
	}
	return memo[n][oldi] = sum;
}

int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("A.out","wt",stdout);
	int l,d,n;
	scanf("%d%d%d",&l,&d,&n);
	cur = 1;
	all[0] = new node();
	for (int i = 0; i < d; ++i) {
		scanf(" %s",words[i]);
		build(words[i],0);
	}
	for (int i = 0; i < n; ++i) {
		cin >> s;
		memset(memo,-1,sizeof memo);
		cout << "Case #" << i+1  << ": " << dp(0,0) << endl;
	}
	//dfs(0,"");
	return 0;
}
