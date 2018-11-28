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

int ebob(int a, int b){
    
    int temp;
    
    if(a<b){
    temp=a;
    a=b;
    b=temp;
}
    
    while((b)!=0){
       temp=b;
       b=a%b;
       a=temp;
}

	return a;

}

int main(){
	
	freopen("input.txt","rt",stdin);
	freopen("out.txt","wt",stdout); 
    
    string temp;
	int i,j,k,l;
	int t,N,Pd,Pg,g_today;
	int flag=0;
	cin>>t;

	for ( k=1; k<=t; k++){
		
		cin>>N;
		cin>>Pd;
		cin>>Pg;
		
		g_today=100/ebob(Pd,100);
		
		if ( g_today > N )
			flag=1;
			
		if ( Pd != 0 && Pg == 0 )
			flag=1;
			
		if ( Pd !=100 && Pg == 100 )
			flag=1;
	
		if (flag)
			cout<<"Case #"<<k<<": Broken"<<endl;
		else
			cout<<"Case #"<<k<<": Possible"<<endl;
		
		flag=0;

	}
	
	return 0;
	
}
		
			
			
			
			
			
			

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
