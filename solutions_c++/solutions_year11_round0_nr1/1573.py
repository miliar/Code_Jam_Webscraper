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
int type[maxn],pos[maxn];
int n;

void init(){
	scanf("%d",&n);
	for (int i=1;i<=n;i++){
		char cc=getchar();
		int tpos;
		cc=getchar();
		scanf("%d",&tpos);
		if (cc=='O'){
			type[i]=0;
		} else {
			type[i]=1;
		}
		pos[i]=tpos;
	}
	return;
}

int simulate(){
	int lt[2]={0,0};
	int lp[2]={1,1};
	int curtime=0;
	for (int i=1;i<=n;i++){
		if ((curtime-lt[type[i]])>=abs(pos[i]-lp[type[i]])){
			curtime++;
			lt[type[i]]=curtime;
		} else {
			lt[type[i]]+=abs(pos[i]-lp[type[i]])+1;
			curtime=lt[type[i]];
		}
		lp[type[i]]=pos[i];
	}
	return max(lt[0],lt[1]);
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int t=1;t<=tcase;t++){
		init();
		printf("Case #%d: %d\n",t,simulate());
	}
	return 0;
}
