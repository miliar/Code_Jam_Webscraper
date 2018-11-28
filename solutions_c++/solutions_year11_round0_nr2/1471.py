#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
const int maxn=1001;
int comb[maxn][3];
int opp[maxn][2];
char str[maxn];
int c,d,n;

void init(){
	scanf("%d",&c);
	for (int i=1;i<=c;i++){
		char str[maxn];
		scanf("%s",str);
		for (int j=0;j<3;j++){
			comb[i][j]=str[j]-'A';
		}
	}
	scanf("%d",&d);
	for (int i=1;i<=d;i++){
		char str[maxn];
		scanf("%s",str);
		for (int j=0;j<2;j++){
			opp[i][j]=str[j]-'A';
		}
	}
	scanf("%d",&n);
	scanf("%s",str);
	return;
}

void simulate(){
	int list[maxn];
	int z=0;
	list[0]=-1;
	for (int i=0;i<n;i++){
		int cur=str[i]-'A';
		for (int j=1;j<=c;j++){
			if (((comb[j][0]==list[z])&&(comb[j][1]==cur))||((comb[j][0]==cur)&&(comb[j][1]==list[z]))){
				list[z]=comb[j][2];
				cur=-1;
				break;
			}
		}
		if (cur==-1){
			continue;
		}
		for (int j=1;j<=d;j++){
			for (int k=1;k<=z;k++){
				if (((opp[j][0]==cur)&&(opp[j][1]==list[k]))||((opp[j][0]==list[k])&&(opp[j][1]==cur))){
					z=0;
					cur=-1;
					break;
				}
			}
			if (cur==-1){
				break;
			}
		}
		if (cur==-1){
			continue;
		}
		z++;
		list[z]=cur;
	}
	printf("[");
	for (int i=1;i<=z;i++){
		printf("%c",'A'+list[i]);
		if (i!=z){
			printf(", ");
		}
	}
	printf("]");
	return;
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int i=1;i<=tcase;i++){
		init();
		printf("Case #%d: ",i);
		simulate();
		printf("\n");
	}
	return 0;
}
