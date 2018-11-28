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

void binary(int number, deque<int> &num) {
	
	int remainder;
	
	if(number <= 1) {
		num.push_back(number);
		return;
	}

	remainder = number%2;
	binary( (number >> 1) , num);    
	num.push_back(remainder);
	
}

int padd(int a, int b){
	
	int i,j,tmp;
	deque<int> abin,bbin;
	int sum=a+b;
	int nsum=0;
	binary(a, abin);
	binary(b, bbin);
	
	if ( abin.size()<bbin.size() ){
		tmp=(int)bbin.size()-(int)abin.size();
		for ( i=0; i<tmp ; i++ )
			abin.push_front(0);
		}
	else if ( bbin.size()<abin.size() ){
		tmp=(int)abin.size()-(int)bbin.size();
		for ( i=0; i<tmp; i++ )
			bbin.push_front(0);
		}
	/*
	for( i=0; i<((int)abin.size()); i++ )  {
			cout<<abin[i];}
	cout<<endl;
	for( i=0; i<((int)bbin.size()); i++ )  {
			cout<<bbin[i];}
	cout<<endl;
	*/
	for( i=(int)abin.size()-1, j=0; i>=0; i--,j++ )
		if(abin[i]==1 && bbin[i]==1)
			nsum+=(int)pow(2.0, (double)j+1);
	
	
	return sum-nsum;
}
	
/*	
int main(){
	

	
	cout<<"5+4="<<p_add(5,4)<<endl;
	cout<<"7+9="<<p_add(7,9)<<endl;
	cout<<"50+10="<<p_add(50,10)<<endl;


return 0;

}
*/

int add( int sum, deque<int> pile ){
	
	int a;
	
	if ( pile.size() == 0)
		return sum;
		
	a=pile.front();
	pile.pop_front();
	
	return add( padd(sum,a), pile );
	
}

int add2( int sum, deque<int> pile ){
	
	int a;
	
	if ( pile.size() == 0)
		return sum;
		
	a=pile.front();
	pile.pop_front();
	
	return add2( sum+a, pile );
	
}


int main(){
	
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout); 
    
	int i,j,k,l;
	int t,n,c;
	deque <int> pile;
	deque <int> sean, pat;
	cin>>t;
	int flag=0;

	for ( k=1; k<=t; k++){
		cin>>n;
		
		for( i=0; i<n; i++ ){
			cin>>c;
			pile.push_back(c);
		}
		
		sort( pile.begin(), pile.end() );
		
		for( i=0; i<n; i++ ){
			pat.resize(i+1);
			sean.resize( (n-1)-i );
			copy( pile.begin(), pile.begin()+i+1, pat.begin() );
			copy( pile.begin()+i+1, pile.end(), sean.begin() );
			/*
			cout<<"pat=";
			for( i=0; i<((int)pat.size()); i++ )  {
			cout<<pat[i];}
			cout<<endl;
			
			cout<<"sean=";
			for( i=0; i<((int)sean.size()); i++ )  {
			cout<<sean[i];}
			cout<<endl;
			cout<<"apat="<<add(0,pat)<<" asean="<<add2(0,sean)<<endl;
*/
			if ( add(0,pat) == add(0,sean) ){
				flag=1;
				break;
			}
			pat.clear();
			sean.clear();
		}
			
		if (flag)
			cout<<"Case #"<<k<<": "<<add2(0,sean)<<endl;
		else
			cout<<"Case #"<<k<<": "<<"NO"<<endl;
			
		flag=0;
		
		pat.clear();
		sean.clear();
		pile.clear();
	}
	
	
		
			
			
			
		

		

			
		



	return 0;
}
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
