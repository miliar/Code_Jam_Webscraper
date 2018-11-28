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

int fre[100];

bool check(int a, int N){
	
	int i;
	
	for( i=0; i<N; i++ )
		if( fre[i]%a==0 || a%fre[i]==0 )
			continue;
		else
			return false;
			
	return true;
	
}


int main(){
	
	freopen("input.txt","rt",stdin);
	freopen("out.txt","wt",stdout); 
    
    string temp;
	int i,j,k,l;
	int t,N,L,H;
	int flag=1;
	cin>>t;

	for ( k=1; k<=t; k++){
		
		cin>>N;
		cin>>L;
		cin>>H;
		
		for( i=0; i<N; i++ )
			cin>>fre[i];
			
		for ( i=L; i<=H; i++ )
			if ( check(i,N) ){
				cout<<"Case #"<<k<<": "<<i<<endl;
				i=20000;
				flag=0;
			}
				
	
		if(flag)
			cout<<"Case #"<<k<<": NO"<<endl;

		flag=1;

	}
	
	return 0;
	
}
		
			
			
			
			
			
			

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
