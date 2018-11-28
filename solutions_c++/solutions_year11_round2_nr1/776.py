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
char s[111][111]; int n;

LD OWP(int id,int ag){//	cout<<id<<endl;
	int c=0,d=0; 
	
	for(int j=0;j<n;j++) 
		if( j!=ag && s[id][j]!='.' ){ 
			c++; if( s[id][j]=='1' ) d++;
	}
	
	return d*1.0/c;
}

int main (){
	int testCase; scanf("%d",&testCase); int iddd=1;
	while( testCase-- ){
		cin>>n;
		
		for(int i=0;i<n;i++) cin>>s[i];
		
		LD wp[n],owp[n],oo[n];
		//OWP(3); 
		//for(int j=0;j<n;j++) if( s[3][j]!='.' ) cout<<OWP(j,3)<<endl;
		
		//return 0;
		for(int i=0;i<n;i++){
			wp[i]=0.0;
			int c=0,d=0;
			for(int j=0;j<n;j++) if( s[i][j]!='.' ){ 
				c++; if( s[i][j]=='1' ) d++;
			}
			wp[i]=(LD)(d)/c;// cout<<wp[i]<<" ";
			
			c=0; owp[i]=0;
			for(int j=0;j<n;j++) 
				if( s[i][j]!='.' ){
					c++;
					owp[i]+=OWP(j,i);
				}
				
			
			owp[i]/=c;	//cout<<owp[i]<<" : ";
		}
		for(int i=0;i<n;i++){
			oo[i]=0; int c=0;
			for(int j=0;j<n;j++)
			 if( s[i][j]!='.' ){ c++;  oo[i]+=owp[j];}
			oo[i]/=c;
		}
		
		printf("Case #%d:\n",iddd++);
		for(int i=0;i<n;i++) {
			cout<<0.25*wp[i]+0.5*owp[i]+0.25*oo[i]<<"\n";
		}
	}
	return 0;
}
//~vish ( vikas.cse.nitt@gmail.com )
