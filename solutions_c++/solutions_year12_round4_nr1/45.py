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
const int maxn=10001;
int d[maxn],l[maxn],f[maxn];
int n,D;

void init(){
	scanf("%d",&n);
	for (int i=0;i<n;i++){
		scanf("%d%d",&d[i],&l[i]);
	}
	scanf("%d",&D);
	d[n]=D;
	l[n]=0;
	n++;
	memset(f,0xff,sizeof(f));
	f[0]=d[0];
	return;
}

void calc(){
	for (int i=1;i<n;i++){
		for (int j=0;j<i;j++){
			if (f[j]!=-1){
				if (f[j]+d[j]>=d[i]){
					f[i]=max(f[i],min(l[i],d[i]-d[j]));
				}
			}
		}
	}
	if (f[n-1]==-1){
		puts("NO");
	} else {
		puts("YES");
	}
	return;
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int i=1;i<=tcase;i++){
		init();
		printf("Case #%d: ",i);
		calc();
	}	
	return 0;
}
