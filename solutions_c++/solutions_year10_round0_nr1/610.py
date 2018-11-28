/**
* @author Gareve
* @problem A
* @judge Google Code Jam 10
*/
#define DEBUG
#ifndef NDEBUG	
	#define DBG(a) cout<<__LINE__<<": "<<#a<<"= "<<a<<endl;
#else
	#define DBG(a) ;
#endif
#include <iostream>
#include <cassert>
#include <cstdio>
#include <cstring>
#define ON  1
#define OFF 0
#define L long long

using namespace std;
L k,x,n;
bool ok(){
	x=1LL<<n;
	x--;
	if(k==x)return true;
	if(k<x)return false;
	k-=x;
	x++;
	return k%x==0;
}
void resuelva(int c){
	scanf("%lld %lld",&n,&k);



	printf("Case #%d: ",c);
	if(ok())printf("ON\n");
	else
		printf("OFF\n");
}
int main(){
	int q;
	scanf("%d",&q);
	for(int i=1;i<=q;i++)
		resuelva(i);
}

