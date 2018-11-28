// qua1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <string>
#include <cstdio>
#include <fstream>
#include <vector>
#include <map>
using namespace std;

string GetName(){
	char c;
	string Buf("");
	while(true){
		c = getchar();
		if(c == '\n'){
			break;
		}
		Buf += c;
	}
	return Buf;
}

void NewLine(){
	char c;
	while(true){
		c = getchar();
		if(c == '\n'){
			return;
		}
	}
}

int Query[1024];

int dp[1000][128];

int main()
{
	int t;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d", &t);
	int i, j, k, l;
	for(i = 1 ; i <= t ; ++i){
		int s, q;
		map<string, int> NameIndex;
		scanf("%d", &s);
		NewLine();
		int Count = 0;
		for(j = 0 ; j < s ; ++j){
			NameIndex[GetName()] = Count++;
		}
		scanf("%d", &q);
		NewLine();
		for(j = 0 ; j < q ; ++j){
			Query[j] = NameIndex[GetName()];
		}
		for(j = 1 ; j < q ; ++j){
			for(k = 0 ; k < s ; ++k){
				dp[j][k] = 2000;
			}
		}
		for(j = 0 ; j < s ; ++j){
			dp[0][j] = 0;
		}
		dp[0][Query[j]] = 2000;
		for(j = 1 ; j < q ; ++j){
			for(k = 0 ; k < s ; ++k){
				if(Query[j] == k){
					continue;
				}
				for(l = 0 ; l < s ; ++l){
					if(l == k){
						if(dp[j - 1][l] < dp[j][k]){
							dp[j][k] = dp[j - 1][l];
						}
					}
					else{
						if(dp[j - 1][l] + 1 < dp[j][k]){
							dp[j][k] = dp[j - 1][l] + 1;
						}
					}
				}
			}
		}
		int ans = 4000;
		for(j = 0 ; j < s ; ++j){
			if(dp[q - 1][j] < ans){
				ans = dp[q - 1][j];
			}
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}

