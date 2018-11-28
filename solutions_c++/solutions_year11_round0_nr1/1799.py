
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<string>
#include<string.h>
#include<cstring>
#include<stack>
#include<queue>
#include<cassert>
#include<cmath>
using namespace std;

#define LL long long int 
#define PII pair<int,int> 

queue<PII >A,B;
PII e1,e2,dummy;
int main(){
	int i,n,but,t,curA,curB,test;
	char col;
	scanf("%d",&t);
	for(test=1;test<=t;test++){
		scanf("%d",&n);
		for(i=1;i<=n;i++){
			scanf(" %c %d",&col,&but);
			if(col=='O')
				A.push(make_pair(i,but));
			else
				B.push(make_pair(i,but));
		}
		curA=curB=1;
		int time=0;
		dummy.first=10000000;
		while(1){
			if(A.empty()&&B.empty())
				break;
			e1=e2=dummy;
			if(!A.empty())
				e1=A.front();
			if(!B.empty())
				e2=B.front();
			time++;
			if(e1.first<e2.first){
				if(e1.second==curA)
					A.pop();
				else if(e1.second> curA)
					curA++;
				else
					curA--;
				if(e2.second>curB)
					curB++;
				else if(e2.second!=curB)
					curB--;
			}
			else{
				if(e2.second==curB)
					B.pop();
				else if(e2.second> curB)
					curB++;
				else
					curB--;
				if(e1.second>curA)
					curA++;
				else if(e1.second!=curA)
					curA--;
			}
		}
		printf("Case #%d: %d\n",test,time);
	}
	return 0;
}
