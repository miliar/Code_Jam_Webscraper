
//  main.cpp
//  
//
//  Created by  on 12-3-24.
//  Copyright 2012年 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <map>
#define clr(a) memset(a,0,sizeof(a));
#define LOG(a) cerr<<#a<<"="<<a<<" ";
using namespace std;
const int maxsize=26;

inline int move(const int& a,const int& bit){
	return a%10*bit+a/10;	
}

long long solve(const int& a,const int& b){
	long long ans=0;
	int bit=1;
	while(bit*10<=a) bit*=10;
	for(int i=a;i<=b;++i){
		for(int t=move(i,bit);t!=i;t=move(t,bit)){
			if(a<=t && t<=b){
				ans++;
			}
		}
	}			
	return ans/2;
}


int main(){
    int a,b;
	int t,i=1;
	for(cin>>t;t;--t){
   		cin>>a>>b;
		long long ans=solve(a,b);
		cout<<"Case #"<<i<<": "<<ans<<endl;
		i++;
 	}
    return 0;
}


