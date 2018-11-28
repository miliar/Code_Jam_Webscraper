/**
* @author Gareve
* @problem
* @judge
*/
#define DEBUG
#ifndef NDEBUG	
	#define DBG(a) cout<<__LINE__<<": "<<#a<<"= "<<a<<endl;
#else
	#define DBG(a) ;
#endif
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <map>
using namespace std;

void resuelva(){
	int n,sum=0,xx=0;
	scanf("%d",&n);
	int vc[n];
	int mn=-1;
	for(int i=0;i<n;i++){
		scanf("%d",&vc[i]);
		sum += vc[i];
		xx^=vc[i];
		if(mn==-1 or vc[i]<mn)
			mn = vc[i];
	}
	if(xx==0)
		printf("%d\n",sum-mn);
	else
		printf("NO\n");
}
int main(){
	int q;
	scanf("%d",&q);
	for(int i=1;i<=q;i++){
		printf("Case #%d: ",i);
		resuelva();
	}
}

