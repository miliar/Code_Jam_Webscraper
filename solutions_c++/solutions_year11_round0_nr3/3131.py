/*	Author       :	Muntasir Muzahid Chowdhury
	Problem Name :
	Algorithm    :
	Complexity   :	*/

//HEADERFILE
#include<iostream>
#include<stack>
#include<queue>
#include<list>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<cstring>
#include<ctime>
#include<cassert>
#include<string>
#include<algorithm>

using namespace std;

int N,sum,ar[20];

int MAX(int a,int b){	return a>b?a:b; }

int f(int i,int s1,int s2,int realsum){
	if(i==N){
		if(s1==s2){
			if(realsum==sum || realsum==0) return -1;
			else return MAX(realsum,sum-realsum);
		}
		else return -1;
	}
	return MAX(f(i+1,s1^ar[i],s2,realsum),f(i+1,s1,s2^ar[i],realsum+ar[i]));
}

int main(){
		//freopen("C-small-attempt0.in","r",stdin);
		//freopen("C-small-attempt0.out","w",stdout);
	int cases,caseno=0,i,j,result;
	scanf("%d",&cases);
	while(cases--){
		scanf("%d",&N);
		sum=0;
		for(i=0;i<N;i++) scanf("%d",&ar[i]),sum+=ar[i];
		result=f(0,0,0,0);
		if(result==-1) printf("Case #%d: NO\n",++caseno);
		else printf("Case #%d: %d\n",++caseno,result);
	}
	return 0;
}

