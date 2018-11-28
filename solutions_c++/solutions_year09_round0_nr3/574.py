#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <queue>
#include <map>
#include <cmath>
#include <memory.h>
#include <string>
#include <iostream>
using namespace std;
const int maxlen=502;
const int l1=19;
const int modo=10000;
const char pat[20]={"welcome to code jam"};
char str[maxlen];
int l2;
int f[l1+1][maxlen+1];

void init(){
	gets(str);
	l2=strlen(str);
	return;
}

int dp(){
	memset(f,0,sizeof(f));
	for (int i=0;i<=l2;i++){
		f[0][i]=1;
	}
	for (int i=1;i<=l1;i++){
		for (int j=1;j<=l2;j++){
			if (pat[i-1]==str[j-1]){
				f[i][j]+=f[i-1][j-1];
			}
			//f[i][j]+=f[i-1][j];
			f[i][j]+=f[i][j-1];
			f[i][j]%=modo;
		}
	}
	return f[l1][l2];
}

int main(){
	int t;
	scanf("%d",&t);
	gets(str);
	for (int k=1;k<=t;k++){
		init();
		printf("Case #%d: %04d\n",k,dp());
	}
	return 0;
}
