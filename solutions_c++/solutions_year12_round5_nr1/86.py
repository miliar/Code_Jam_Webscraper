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
#include <vector>
using namespace std;
const int maxn=1001;
int n;
int l[maxn],p[maxn];
pair<double,int> a[maxn];

void init(){
	scanf("%d",&n);
	for (int i=0;i<n;i++){
		scanf("%d",&l[i]);
	}
	for (int i=0;i<n;i++){
		scanf("%d",&p[i]);
	}
	return;
}

void process(){
	for (int i=0;i<n;i++){
		a[i]=make_pair(-1.0*p[i]*l[i],i);
	}
	sort(a,a+n);
	for (int i=0;i<n;i++){
		printf(" %d",a[i].second);
	}
	puts("");
	return;
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int i=1;i<=tcase;i++){
		init();
		printf("Case #%d:",i);
		process();
	}
	return 0;
}
