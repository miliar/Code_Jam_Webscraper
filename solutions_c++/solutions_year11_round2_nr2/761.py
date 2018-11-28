#include<algorithm>
#include<bitset>
#include<cassert>
#include<cmath>
#include<complex>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<fstream>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<vector>
#include<climits>
#define LD long double
using namespace std;

int c,d;
int p[222],v[222];

int good(LD m){
	
	LD pre=-(1e18),l,r;
	for(int i=0;i<c;i++){
		l=max( p[i]-m , pre);
		l+=(LD)(1.0)*d*(v[i]-1); //cout<<i<<" "<<l<<" "<<l-d*(v[i]-1)<<endl;
		if(  l- p[i]  > m ) return 0;
		pre=l+d;
	}
	return 1;
}

int main (){
	int testCase; scanf("%d",&testCase); int iddd=1;
	while( testCase-- ){
		cin>>c>>d;
		for(int i=0;i<c;i++) cin>>p[i]>>v[i];
		LD lo=0.0,hi=1e18;
		
		//cout<<good(2.0)<<endl; return 0;
		while( (hi-lo) > 1e-10 ){
			LD mid=(lo+hi)/2;
			//cout<<mid<<" "<<good(mid)<<endl;
			if( good(mid) ) hi=mid;
			else lo=mid;
		}		
		printf("Case #%d: ",iddd++);
		cout<<(lo+hi)/2<<endl;	
	}
	return 0;
}
//~vish ( vikas.cse.nitt@gmail.com )
