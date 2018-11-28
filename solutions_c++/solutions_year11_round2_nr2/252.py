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
const int maxn=1000001;
int a[maxn];
int z,d;

void init(){
	int c;
	z=0;
	scanf("%d%d",&c,&d);
	d*=2;
	for (int i=1;i<=c;i++){
		int pos,cnt;
		scanf("%d%d",&pos,&cnt);
		pos*=2;
		for (int j=1;j<=cnt;j++){
			a[z]=pos;
			z++;
		}
	}
	sort(a,a+z);
	return;
}

bool isok(__int64 cur){
	__int64 curposi=((__int64)a[0])-cur;
	for (int i=1;i<z;i++){
		curposi=max(curposi+((__int64)d),((__int64)a[i])-cur);
		if (curposi>a[i]+cur){
			return false;
		}
	}
	return true;
}

double bsearch(){
	__int64 l=-1;
	__int64 r=10000000000000000LL;
//	isok(610351562499LL);
	while (l+1<r){
		__int64 mid=(l+r)>>1;
		if (isok(mid)){
			r=mid;
		} else {
			l=mid;
		}
//		printf("%I64d\n",mid);
	}
	return ((double)r)*0.5;
}

int main(){
//	freopen("dbg.txt","r",stdin);
	int cse;
	scanf("%d",&cse);
	for (int i=1;i<=cse;i++){
		init();
		printf("Case #%d: %.1f\n",i,bsearch());
	}	
	return 0;
}
