/*
 *  template.cpp
 *  
 *
 *  Created by Kashyap Kolipaka on 9/2/09.
 *  Copyright 2009 Rutgers University. All rights reserved.
 *
 */

#include "template.h"
#include <cstdio>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <vector>
#include <sstream>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b) for(int i = a; i <b ; i++)
#define FRR(i,a,b) for(int i = b - 1; i >=a ; i--)
#define sz size()
#define pb push_back
#define VI vector<int>
#define VVI vector<VI>
#define eps 1e-9
#define VS vector<string>

bool match(string pattern, string text){
	int pi = 0;
	FOR(i,0,text.sz){
		if(pattern[pi] == '('){
			pi++;
			bool matched = false;
			while(pattern[pi] != ')'){
				if(text[i] == pattern[pi])matched = true;
				pi++;
			}
			pi++;
			if(!matched) return false;
		}
		else {
			if(pattern[pi] != text[i]) return false;
			pi++;
		}
	}
	return true;
}

	int main(){
		int L, D, N;
		cin >> L >> D >> N;
		VS word; VS pattern;
		FOR(i,0,D){
			string tmp;
			cin >> tmp;
			word.pb(tmp);
		}
		FOR(i,0,N){
			string tmp;
			cin >> tmp;
			pattern.pb(tmp);
		}
		FOR(i,0,N){
			int count = 0;
			FOR(j,0,D)count += match(pattern[i], word[j]);
			cout << "Case #"<< i+1 << ": "<< count << endl;
		}
	}