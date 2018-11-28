#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int n,m;
int tar;

void init(){
	scanf("%d%d%d",&n,&m,&tar);
	return;
}

bool solve(){
	for (int x1=0;x1<=n;x1++){
		for (int y1=0;y1<=m;y1++){
			for (int x2=0;x2<=n;x2++){
				for (int y2=0;y2<=m;y2++){
					if (abs(x1*y2-x2*y1)==tar){
						printf("0 0 %d %d %d %d\n",x1,y1,x2,y2);
						return true;
					}
				}
			}
		}
	}
	return false;
}

int main(){
	int t;
	scanf("%d",&t);
	for (int cse=1;cse<=t;cse++){
		init();
		printf("Case #%d: ",cse);
		if (!solve()){
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}
