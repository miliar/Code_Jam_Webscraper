
#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int d[1001][20];
	
char buf[1000];

char t[20] = "welcome to code jam"; // strlen = 19

int sch(int x, int y){

	if(d[x][y] != -1){
		return d[x][y] % 10000;
	}

	if(x == y){
		bool yes = true;
		for(int i=0; i<x; ++i){
			if(buf[i] != t[i]){
				yes = false;
			}
		}
		return d[x][y] = yes;
	}

	return d[x][y] = (sch(x-1, y) + ((buf[x-1] == t[y-1])?sch(x-1, y-1):0)) % 10000;
}

int main(){

	int N;

	cin >> N;
	
	gets(buf);

	for(int ncase = 1; ncase <=N; ++ncase){
		
		gets(buf);

		int len = strlen(buf);
		
		for(int i=0; i<=len; ++i){
			for(int j=0; j<=19; ++j){
				d[i][j] = -1;
			}
		}
		
		printf("Case #%d: %04d\n", ncase, sch(len, 19));
	}
	return 0;
}
