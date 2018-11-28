#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <iostream>
#include <map>
#define ptr multimap<__int64,__int64>::iterator
using namespace std;
__int64 n;
multimap<__int64,__int64> hash;

void init(){
	scanf("%I64d",&n);
	hash.clear();
	return;
}

void insertpair(__int64 a,__int64 b){
	hash.insert(make_pair(a,b));
	return;
}

ptr getptr(__int64 p){
	ptr it=hash.upper_bound(p);
	if (it!=hash.begin()){
		it--;
	}
	return it;
}

void erase(ptr p){
	hash.erase(p);
	return;
}

void insert(__int64 p){
	__int64 l,r;
	l=r=p;
	ptr it=hash.upper_bound(p);
	if (it!=hash.begin()){
		ptr curit=it;
		curit--;
		if (curit->second==p-1){
			l=curit->first;
			erase(curit);
		}
	}
	if (it!=hash.end()){
		if (it->first==(p+1)){
			r=it->second;
			erase(it);
		}
	}
	insertpair(l,r);
	return;
}

void del(__int64 p){
	ptr it=getptr(p);
	if (it->first<p){
		insertpair(it->first,p-1);
	}
	if (it->second>p){
		insertpair(p+1,it->second);
	}
	erase(it);
}

__int64 processpos(__int64 p){
	__int64 l,r;
	ptr it=getptr(p);
	if (it==hash.end()){
		insert(p);
		return 0;
	}
	l=it->first;
	r=it->second;
	if (l>p||r<p){
		insert(p);
		return 0;
	}
	insert(l-1);
	insert(r+1);
	del(l+r-p);
	return (p-l+1)*(r-p+1);
}

__int64 process(){
	__int64 ans=0;
	for (__int64 i=1;i<=n;i++){
		__int64 p,v;
		scanf("%I64d%I64d",&p,&v);
		for (__int64 j=1;j<=v;j++){
			ans+=processpos(p);
		}
	}
	return ans;
}

int main(){
	__int64 cse;
	scanf("%I64d",&cse);
	for (__int64 i=1;i<=cse;i++){
		init();
		printf("Case #%I64d: %I64d\n",i,process());
	}
	return 0;
}
