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

const int MAXN = 50;

int T;
int N;
int idx[MAXN];
string s[MAXN],str;

void init(){
}

struct Node{
	int key, step;
	Node(int k, int s):key(k),step(s){}
	bool operator<(const Node& b)const{
		return step > b.step;
	}
};

int getKey(){
	int key = 1;
	for(int i = 0; i < N; ++i){
		key = key * 10 + idx[i];
	};
	return key;
}

int solve(){
	for(int i = 0; i < N; ++i){
		idx[i] = 0;
		for(int j = N-1; j >= 0; --j){
			if(s[i][j] != '0'){
				idx[i] = j;
				break;
			}
		}
	}

	map<int,int> mii;
	queue<Node> pq;
	pq.push(Node(getKey(), 0));
	mii.insert(make_pair(getKey(), 0));
	while(!pq.empty()){
		Node now = pq.front();
		pq.pop();
		int j = N-1;
		for(int i = 0; i < N; ++i){
			idx[j--] = now.key % 10;
			now.key /= 10;
		}
		bool f = true;
		for(int i = 0; i < N; ++i){
			if(idx[i] > i){
				f = false;
			}
		}
		if(f) return now.step;
		for(int i = 0; i + 1 < N; ++i){
					swap(idx[i+1], idx[i]);
					int key = getKey();
					if(mii.find(key) == mii.end()){
						pq.push(Node(key, now.step+1));
						mii.insert(make_pair(key, now.step + 1));
					}
					swap(idx[i+1], idx[i]);
		}
	}
	return -1;
}

int main()
{
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	//freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	scanf("%d", &T);
	init();
	for(int tt = 1; tt <= T; ++tt)
	{
		scanf("%d", &N);
		getline(cin, str);
		for(int i = 0; i < N; ++i){
			getline(cin, s[i]);
		}
		int ans = solve();
		printf("Case #%d: %d\n", tt, ans);
	}

	return 0;
}
