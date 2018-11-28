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
int n,s,p;

void init(){
	scanf("%d%d%d",&n,&s,&p);
	return;
}

int process(){
	int ans=0;
	for (int i=1;i<=n;i++){
		int cur;
		scanf("%d",&cur);
		if (cur>=(p+2*(max(0,p-1)))){
			ans++;
			continue;
		}
		if (s==0){
			continue;
		}
		if (cur>=(p+2*(max(0,p-2)))){
			ans++;
			s--;
			continue;
		}
	}
	return ans;
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int i=1;i<=tcase;i++){
		init();
		printf("Case #%d: %d\n",i,process());
	}	
	return 0;
}
