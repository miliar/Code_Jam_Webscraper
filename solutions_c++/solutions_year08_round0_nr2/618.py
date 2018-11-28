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
const int maxn=201;
int na,nb,t;
int lv[maxn],ar[maxn],tp[maxn];

void qsort(int l,int r){
	int i=l,j=r,mid=lv[(l+r)>>1];
	do {
		while (lv[i]<mid){
			i++;
		}
		while (lv[j]>mid){
			j--;
		}
		if (i<=j){
			swap(lv[i],lv[j]);
			swap(ar[i],ar[j]);
			swap(tp[i],tp[j]);
			i++;
			j--;
		}
	} while (i<=j);
	if (l<j){
		qsort(l,j);
	}
	if (i<r){
		qsort(i,r);
	}
	return;
}

void init(){
	scanf("%d",&t);
	scanf("%d%d",&na,&nb);
	for (int i=1;i<=na;i++){
		int th,tm;
		scanf("%d:%d",&th,&tm);
		int t=th*60+tm;
		lv[i]=t;
		scanf("%d:%d",&th,&tm);
		t=th*60+tm;
		ar[i]=t;
		tp[i]=1;
	}
	for (int i=1;i<=nb;i++){
		int th,tm;
		scanf("%d:%d",&th,&tm);
		int t=th*60+tm;
		lv[i+na]=t;
		scanf("%d:%d",&th,&tm);
		t=th*60+tm;
		ar[i+na]=t;
		tp[i+na]=2;
	}
	qsort(1,na+nb);
	return;
}

void process(){
	int ansa=0;
	int ansb=0;
	vector<int> ta,tb;
	ta.clear();
	tb.clear();
	for (int k=1;k<=na+nb;k++){
		if (tp[k]==1){
			int flag=-1;
			for (int i=0;i<ta.size();i++){
				if (ta[i]==-1){
					continue;
				}
				if (ta[i]<=lv[k]){
					flag=i;
					break;
				}
			}
			if (flag==-1){
				ansa++;
			} else {
				ta[flag]=-1;
			}
			tb.push_back(ar[k]+t);
		} else {
			int flag=-1;
			for (int i=0;i<tb.size();i++){
				if (tb[i]==-1){
					continue;
				}
				if (tb[i]<=lv[k]){
					flag=i;
					break;
				}
			}
			if (flag==-1){
				ansb++;
			} else {
				tb[flag]=-1;
			}
			ta.push_back(ar[k]+t);
		}
	}
	printf("%d %d\n",ansa,ansb);
	return;
}

int main(){
//	freopen("in.txt","r",stdin);
	int t;
	scanf("%d",&t);
	for (int cse=1;cse<=t;cse++){
		init();
		printf("Case #%d: ",cse);
		process();
	}
	return 0;
}
