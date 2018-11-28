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
#define L long long

using namespace std;

void resuelva(){
	L n,pd,pg;
	cin>>n>>pd>>pg;
	
	bool sw = false;
	for(L d=1;d<=min(100LL,n);d++){
		if(((pd*d)%100)==0)
			sw = true;
	}
	if(!sw){
		printf("Broken\n");
		return;
	}
	if(pd==0LL and pg==100LL){printf("Broken\n");return;}
	if(pd==100LL and pg==0LL){printf("Broken\n");return;}
	if(pg==100LL and pd!=100LL){printf("Broken\n");return;}
	if(pg==0LL and pd!=0LL){printf("Broken\n");return;}
	printf("Possible\n");
}
int main(){
	int q;
	scanf("%d",&q);
	for(int i=1;i<=q;i++){
		printf("Case #%d: ",i);
		resuelva();
	}
}

