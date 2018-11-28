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

using namespace std;

const int inf = 0x7f7f7f7f;
const double pi=acos(-1.0);
const double eps = 1e-8;



int c, n, d;
char w[110];
char s[110];
char merg[333][333];
bool opose[333][333];
bool contain[333];

bool read(){
	//if() return false;	
	scanf("%d", &c);
	
	memset(merg, 0, sizeof merg);
	memset(opose, 0, sizeof opose);
	memset(contain, 0, sizeof contain);
	
	for(int i = 0; i < c; i++){
		scanf("%s", w);
		merg[w[0]][w[1]] = w[2];
		merg[w[1]][w[0]] = w[2];
	}
	
	scanf("%d", &d);
	
	for(int i = 0; i < d; i++){
		scanf("%s", w);
		opose[w[0]][w[1]] = true;
		opose[w[1]][w[0]] = true;
	}
		
	scanf("%d", &n);
	
	scanf("%s", s);	
		
	return true;
}

bool isopose(int pw){
	for(int i = 0; i < pw; i++){
		for(int j = i+1; j < pw; j++){
			if(opose[w[i]][w[j]]) return true;
		}
	}
	
	return false;
}

int cn = 1;

void process(){
	int pw = 0;
	int ps = 0;
	
	while(ps != n){
		w[pw++] = s[ps++];
		if(pw >= 2){
			if(merg[w[pw-1]][w[pw-2]]){
				w[pw-2] = merg[w[pw-1]][w[pw-2]];
				pw--;
			}					
		}
		if(isopose(pw)) pw = 0;	
		//w[pw] = 0;
		//printf("%s\n", w);
	}	
		
	printf("Case #%d: [", cn++);
	
	if(pw > 0) printf("%c", w[0]);
	for(int i = 1; i < pw; i++) printf(", %c", w[i]);
	printf("]\n"); 
}

int main(){
	freopen("a.txt", "r", stdin);	
	freopen("b.txt", "w", stdout);
	int cases; scanf("%d", &cases);
	
	while(cases-- && /**/ read()){		
		process();
	}
	
	//while(1);
	
	return 0;
}
