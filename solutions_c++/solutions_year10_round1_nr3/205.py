/*
 *  C.cpp
 *  
 *
 *  Created by Pro.hessam on ۸۹/۳/۱.
 *  Copyright 2010 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>
#include <map>

using namespace std;

struct state{
	int a, b;
	state(int _a= 0, int _b= 0): a(_a), b(_b) { }
	inline bool operator < (const state & second) const{
		return a!=second.a ? a<second.a : b<second.b;
	}
};
map<state, char> mip;

char DFS(int a, int b){
	if (a == 0)
		return 'W';
	if (b >= 2*a)
		return 'W';
	state now(a, b);
	if (mip.find(now) != mip.end())
		return mip[now];
	for (int k=1 ; a*k<=b ; k++)
		if (DFS(min(a, b-a*k), max(a, b-a*k)) == 'L'){
			mip[now]= 'W';
			return 'W';
		}
	mip[now]= 'L';
	return 'L';
}
/******************************/
int main(){
	int test;
	cin >> test;
	for (int t=1 ; t<=test ; t++){
		int a1, a2, b1, b2;
		cin >> a1 >> a2 >> b1 >> b2;
		int res= 0;
		for (int i=a1 ; i<=a2 ; i++)
			for (int j=b1 ; j<=b2 ; j++)
				if (DFS(min(i, j), max(i, j)) == 'W')
					res++;
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}

