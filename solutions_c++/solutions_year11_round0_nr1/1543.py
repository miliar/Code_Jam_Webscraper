// a.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include<cstdio>
#include<iostream>
#define N 103
using namespace std;
struct node{
	char r;
	int p;
};

int main(){
	int T;
	int n;
	int i;
	node a;
	int pa,pb,t;
	int ta,tb;
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	int cas=1;
	while(T--){
		pa=pb=1;
		ta=tb=0;
		t=0;
		cin>>n;
		for(i=0;i<n;i++){
			cin>>a.r>>a.p;
			if(a.r=='O'){
				if(t<(a.p-pa>0?a.p-pa:pa-a.p)+ta+1)
					t=(a.p-pa>0?a.p-pa:pa-a.p)+ta+1;
				else
					t=t+1;
				ta=t;
				pa=a.p;
			}
			else{
				if(t<(a.p-pb>0?a.p-pb:pb-a.p)+tb+1)
					t=(a.p-pb>0?a.p-pb:pb-a.p)+tb+1;
				else
					t=t+1;
				tb=t;
				pb=a.p;
			}
		}
		cout<<"Case #"<<cas++<<": "<<t<<endl;
	}
}