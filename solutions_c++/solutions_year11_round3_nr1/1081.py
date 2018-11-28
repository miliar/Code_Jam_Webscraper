#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;

char pic[51][51];



int main(){
	
	freopen("input.txt","rt",stdin);
	freopen("out.txt","wt",stdout); 
    
    string temp;
	int i,j,k,l;
	int t,R,C;
	int flag=0;
	cin>>t;

	for ( k=1; k<=t; k++){
		
		for ( i=0; i<51; i++ )
			for ( j=0; j<51; j++ )
					pic[i][j]='a';
		cin>>R;
		cin>>C;
		
		for ( i=0; i<R; i++ )
			for ( j=0; j<C; j++ )
				cin>>pic[i][j];
				
		for ( i=0; i<R; i++ )
			for ( j=0; j<C; j++ ){
				//cout<<"i="<<i<<" j="<<j<<endl;
				if( pic[i][j] == '#' ){
					if( pic[i+1][j] == '#' && pic[i+1][j+1] == '#' && pic[i][j+1] == '#' ){
						pic[i][j] = '/';
						pic[i+1][j] = 92;
						pic[i+1][j+1] = '/';
						pic[i][j+1] = 92;
					 }
					 else {flag=1; j=100; i=100;}
				 }
			 }
		
					 
		if (flag)
		cout<<"Case #"<<k<<":"<<endl<<"Impossible"<<endl;
		else{
		cout<<"Case #"<<k<<":"<<endl;
		for ( i=0; i<R; i++ ){
			for ( j=0; j<C; j++ ){
				cout<<pic[i][j];
				}
			cout<<endl;
			}
		}
		
		flag=0;



	}
	
	return 0;
	
}
		
			
			
			
			
			
			

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
