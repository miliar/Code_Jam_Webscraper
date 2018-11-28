//============================================================================
// Name        : gcj2012qualB.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <cstdio>
using namespace std;

#define For(i,a,b) for(int i = a; i < b; i++)
#define rep(i,x) For(i,0,x)
#define Foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define size(x) ((x).size())
#define F first
#define S second
#define mp make_pair

int main() {
	int np; cin>>np;
	rep(tp, np){
		int n,s,p; cin>>n>>s>>p;
		int res = 0;
		rep(i,n){
			int t; cin>>t;
			int div = t / 3, rem = t % 3;

			int top = (rem > 0 ? div + 1 : div);

			if(top >= p)
				res++;
			else if(s > 0)
				if( (rem == 2 && top == p - 1) || (rem == 0 && div > 0 && top >= p-1) ){
					res++;
					s--;
				}
		}
		printf("Case #%d: %d\n", tp + 1, res);
	}
}
