#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;
const __int64 maxn=101;
__int64 l,n,limit;
__int64 a[maxn],d[maxn];
__int64 queue[100000];
bool v[100000];

void init(){
	scanf("%I64d%I64d",&l,&n);
	for (__int64 i=0;i<n;i++){
		scanf("%I64d",&a[i]);
	}
	sort(a,a+n);
	limit=a[n-1];
	return;
}

void bellman_ford(){
	memset(d,0xff,sizeof(d));
	memset(v,false,sizeof(v));
	__int64 head=0;
	__int64 tail=1;
	d[0]=0;
	queue[0]=0;
	v[0]=true;
	while (true){
		if (head==tail){
			break;
		}
		__int64 cur=queue[head];
		head++;
		v[cur]=false;
		for (__int64 i=0;i<=n-2;i++){
			__int64 tcur=cur+a[i];
			if (tcur<limit){
				if (d[tcur]==-1||d[tcur]>d[cur]+1){
					d[tcur]=d[cur]+1;
					if (v[tcur]){
						continue;
					}
					v[tcur]=true;
					queue[tail]=tcur;
					tail++;
				}
				continue;
			}
			if (d[tcur-limit]==-1||d[tcur-limit]>d[cur]){
				d[tcur-limit]=d[cur];
				if (v[tcur-limit]){
					continue;
				}
				v[tcur-limit]=true;
				queue[tail]=tcur-limit;
				tail++;
			}
		}
	}
	return;
}

void process(){
	bellman_ford();
	if (d[l%limit]==-1){
		puts("IMPOSSIBLE");
	} else {
		printf("%I64d\n",d[l%limit]+l/limit);
	}
	return;
}

int main(){
	__int64 cse;
	scanf("%I64d",&cse);
	for (__int64 i=1;i<=cse;i++){
		init();
		printf("Case #%I64d: ",i);
		process();
	}
	return 0;
}
