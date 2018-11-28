#include <map>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

string str;
long long value;
int n;
long long cnt = 0;

void go(int x){
	if(x==n){
		bool ok = false;
		ok |= (value % 2 == 0);
		ok |= (value % 3 == 0);
		ok |= (value % 5 == 0);
		ok |= (value % 7 == 0);
		cnt += ok;
		return;
	}		
	for(int i=1; i<=n-x; i++){
		string v = str.substr(x,i);
		long long vv;
		vv =_atoi64(v.c_str());
		value += vv;
		go(x+i);
		value -= vv;
		if(x){
			value -= vv;
			go(x+i);
			value += vv;
		}
	}
}
int main(void){
	freopen("input.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	int i,j,k,l,m,t;
	scanf("%d", &t);
	for(int out=1; out<=t; out++){
		cin >> str;
		value = 0;
		cnt = 0;
		n = str.size();
		go(0);
		printf("Case #%d: %lld\n", out, cnt);
	}
}