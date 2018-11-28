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

int n;
int m[110][110];
char buf[110];
double win[110];
double o[110];
double oo[110];

bool read(){
	scanf("%d", &n);
	
	for(int i = 0; i < n; i++){
		scanf("%s", buf);
		for(int j = 0; j < n; j++){
			if(buf[j] == '.') m[i][j] = -1;
			else m[i][j] = buf[j]-'0';
		}
	}
	
	return true;
}

double wp(int team, int take){
	double res = 0;
	double temp = 0;

	for(int i = 0; i < n; i++){
		if(i == take) continue;
		if(m[team][i] == -1) continue;
		if(m[team][i] == 1) res += 1;
		temp += 1;
	}
	
	res /= temp;

	//printf("%d %d = %lf\n", team, take, res);	
	return res;
}
int cn = 1;
void process(){	
	int temp;

	for(int i = 0; i < n; i++){		
		win[i] = wp(i, -1);
	}
	
	for(int i = 0; i < n; i++){
		o[i] = 0;
		temp = 0;
		for(int j = 0; j < n; j++){
			if(i == j) continue;
			if(m[i][j] == -1) continue;
			o[i] += wp(j, i);
			temp++;
		}
		
		o[i] /= temp;	
	}
	
	for(int i = 0; i < n; i++){
		oo[i] = 0;
		temp = 0;
		
		for(int j = 0; j < n; j++){
			if(i == j) continue;
			if(m[i][j] == -1) continue;
			oo[i] += o[j];
			temp++;
		}
		
		oo[i] /= temp;
	}
	
	printf("Case #%d:\n", cn++);
	
	for(int i = 0; i < n; i++){
		printf("%.10lf\n", 0.25*win[i]+0.5*o[i]+0.25*oo[i]);
	}
	
	

	
}

int main(){

	int cases; scanf("%d", &cases);
	
	while(cases-- && /**/ read()){		
		process();
	}
	
	return 0;
}
