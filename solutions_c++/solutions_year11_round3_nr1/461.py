#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <iostream>

#define ln printf("\n")
#define pii pair<int,int>
#define a first
#define b second
#define mp make_pair

using namespace std;

int n, c;
char r[110][110];

bool read(){
	//if() return false;	
	scanf("%d%d", &n, &c);
	
	for(int i = 0; i < n; i++){
		scanf("%s", r[i]);
	}	
	return true;
}

int cn = 1;

bool end(){
	for(int i = 0; i < n; i++){
		for(int j = 0; j < c; j++){
			if(r[i][j] == '#') return false;
		}
	}
	
	return true;
}

pii get(){
	for(int i = 0; i < n-1; i++){
		for(int j = 0; j < c-1; j++){
			if(r[i][j] == '#') return mp(i,j);
		}
	}
	
	return mp(-1,-1);
}

bool change(pii p){
	int x = p.b;
	int y = p.a;
	
	for(int i = 0; i < 2; i++){
		for(int j = 0; j < 2; j++){
			if(r[y+i][x+j] != '#') return false;
		}
	}
	
	r[y][x] = 47;
	r[y][x+1] = 92;
	r[y+1][x] = 92;
	r[y+1][x+1] = 47;
	
	return true;
}

void process(){
	pii p = get();
	/*
	ln;
	for(int i = 0; i < n; i++){
			for(int j = 0; j < c; j++){
				printf("%c", r[i][j]);
			}
			ln;
		}
	*/
	while(p.a != -1){
		if(change(p) == false) break;
		p = get();
	}



	printf("Case #%d:\n", cn++);
	if(!end()) printf("Impossible\n");
	else{
		for(int i = 0; i < n; i++){
			for(int j = 0; j < c; j++){
				printf("%c", r[i][j]);
			}
			ln;
		}
	} 
	
}

int main(){
	
	int cases; scanf("%d", &cases);
	
	while(cases-- && /**/ read()){		
		process();
	}
	
	
	return 0;
}
