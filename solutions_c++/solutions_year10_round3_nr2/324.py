#include <iostream>
#include <cmath>
using namespace std;

int main()
{   
	int t; 
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>t;
	for(int i=1;i<=t;i++)    
	{        double P,L,C;        
				cin>>L>>P>>C;        
				double tmp=log(P/L);       
				tmp/=log(C);            
				 tmp=log(tmp)/log(2.0); 
       
				tmp=ceil(tmp);      
				int res = tmp;
				if( res < 0 )res=0;
				cout<<"Case #"<<i<<": "<<res<<endl;    
	}    
	return 0;
} 
