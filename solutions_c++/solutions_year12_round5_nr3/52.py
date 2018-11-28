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
const __int64 maxn=201;
const __int64 oo=1000000000000000001LL;
__int64 m,f,n,cnt;
__int64 s[maxn],q[maxn],qcnt[maxn];
pair<int,int> a[maxn];

void init(){
	scanf("%I64d%I64d%I64d",&m,&f,&n);
	for (__int64 i=0;i<n;i++){
		__int64 p,s;
		scanf("%I64d%I64d",&p,&s);
		a[i]=make_pair(p,s+1);
	}
	return;
}

__int64 multiply(__int64 a,__int64 b){
	if (oo/b>=a){
		return a*b;
	} else {
		return oo;
	}
}

__int64 addition(__int64 a,__int64 b){
	return min(a+b,oo);
}

__int64 find(__int64 day){
	if (day>q[cnt]){
		return oo;
	}
	__int64 pos=lower_bound(q,q+cnt+1,day)-q-1;
	return addition(qcnt[pos],multiply(day-q[pos],s[cnt]));
}

__int64 calc(__int64 value,__int64 pos){
	__int64 k=value/pos;
	__int64 r=value%pos;
	__int64 p=multiply(f,pos);
	p=addition(p,multiply(r,find(k+1)));
	p=addition(p,multiply(pos-r,find(k)));
	return p;
}

bool check(__int64 value){
	if (value==0){
		return false;
	}
	__int64 st=1;
	__int64 en=value;
	while (true){
		if (en<=st+2){
			break;
		}
		__int64 mid=(st+en)/2;
		if (calc(value,mid)<calc(value,mid+1)){
			en=mid+1;
		} else {
			en=mid;
		}
	}
	for (__int64 i=st;i<=en;i++){
		if (calc(value,i)>m){
			continue;
		}
		return true;
	}
	return false;
}

__int64 process(){
	sort(a,a+n);
	cnt=0;
	__int64 cur=0;
	__int64 tmp=0;
	memset(q,0,sizeof(q));
	memset(qcnt,0,sizeof(qcnt));
	for (__int64 i=0;i<n;i++){
		if (cur>=a[i].second){
			continue;
		}
		tmp+=multiply(a[i].second-cur,a[i].first);
		s[cnt]=a[i].first;
		cnt++;
		q[cnt]=a[i].second;
		qcnt[cnt]=tmp;
		cur=a[i].second;
	}
	__int64 st=0;
	__int64 en=oo;
	while (true){
		if (en<=st){
			break;
		}
		__int64 mid=(st+en+1)/2;
		if (check(mid)){
			st=mid;
		} else {
			en=mid-1;
		}
	}
	return st;
}

int main(){
	__int64 tcase;
	scanf("%I64d",&tcase);
	for (__int64 i=1;i<=tcase;i++){
		init();
		printf("Case #%I64d: %I64d\n",i,process());
	}
	return 0;
}
