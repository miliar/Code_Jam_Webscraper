#include <stdio.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <stdio.h>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <math.h>
#include <map>
#define MaxLength INT_MAX
#define MaxNode 12
#define MN 1000005
using namespace std;

long long M,T,N,D,L,H,X,S,R,t;
long long mem[MN];
long long P[MN];
int size;
int main(){
	int i,j,k,len,tt,n,m,maxv,minv;
	long long result,temp;
	int size;
	int x,y,r;
	char ch[500];
	char ss[500];
	int dp[26];
	dp[0] = 24;
	dp[1] = 7;
	dp[2] = 4;
	dp[3] = 18;
	dp[4] = 14;
	dp[5] = 2;
	dp[6] = 21;
	dp[7] = 23;
	dp[8] = 3;
	dp[9] = 20;
	dp[10] = 8;
	dp[11] = 6;
	dp[12] = 11;
	dp[13] = 1;
	dp[14] = 10;
	dp[15] = 17;
	dp[16] = 25;
	dp[17] = 19;
	dp[18] = 13;
	dp[19] = 22;
	dp[20] = 9;
	dp[21] = 15;
	dp[22] = 5;
	dp[23] = 12;
	dp[24] = 0;
	dp[25] = 16;
	gets(ch);
	tt=1;
	while(gets(ch)){
		printf("Case #%d: ",tt++);
		for(int i=0; i<strlen(ch); i++)
			if(ch[i]>='a' && ch[i]<='z')
				printf("%c",dp[ch[i]-'a']+'a');
			else
				cout << ch[i];
		puts("");
	}
	for(tt=1; tt<=T;tt++){
	}

	return 0;
}
