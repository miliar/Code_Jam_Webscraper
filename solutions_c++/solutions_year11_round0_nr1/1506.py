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
#define P pair<string,int>
#define X first
#define Y second


using namespace std;

const int MAX = 109;
P vc[MAX];
int a,b,ta,tb;

int f(int k){
	if(vc[k].X=="B"){
		int d = abs(b-vc[k].Y);
		if(vc[k-1].X=="B"){
			b = vc[k].Y;
			tb += d+1;
			return tb;
		}else{
			b = vc[k].Y;
			tb = max(tb+d+1,ta+1);
			return tb;
		}
	}else{
		int d = abs(a-vc[k].Y);
		if(vc[k-1].X=="O"){
			a = vc[k].Y;
			ta += d+1;
			return ta;
		}else{
			a = vc[k].Y;
			ta = max(ta+d+1,tb+1);
			return ta;
		}
	}
}
void resuelva(){
	int n;
	int res=0;
	ta=0;tb=0;
	a=1;b=1;
	cin>>n;
	vc[0]=P("@",0);
	for(int i=1;i<=n;i++)
		cin>>vc[i].X>>vc[i].Y;
	for(int i=1;i<=n;i++)
		res = f(i);
	printf("%d\n",res);
}
int main(){
	int q;
	cin>>q;
	for(int i=1;i<=q;i++){
		printf("Case #%d: ",i);
		resuelva();
	}
}

