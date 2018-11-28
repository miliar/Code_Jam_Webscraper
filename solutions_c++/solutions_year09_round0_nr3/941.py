// C.Welcome to Code Jam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"


#include"iostream"
#include"string.h"
using namespace std;
int x[20];
bool hash[20];
char str[600],map[600];
int main()
{
	int t,ci = 1,i,j;
	//freopen("G:\\C-large.in","r",stdin);
	//freopen("G:\\Cout.out","w",stdout);
	strcpy(map,"welcome to code jam");
	scanf("%d",&t);
	getchar();
	while(t--){
		
		memset(hash,0,sizeof(hash));
		memset(x,0,sizeof(x));
		gets(str);
		int len = strlen(str);
		for(i=0;i<len;i++){
			for(j=18;j>=0;j--){
				if(map[j] == str[i] ){
					if(j == 0){
						hash[0] = 1;
						x[0] = (x[0] + 1)%10000;
					}
					else if(hash[j-1]){
						hash[j] = 1;
						x[j] = (x[j] + x[j-1])%10000;
					}
				}
			}
		}
		printf("Case #%d: %04d\n",ci++,x[18]);
	}
	return 0;
}
						


