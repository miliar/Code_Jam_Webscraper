#include<iostream>
#include<string>
#include<algorithm>
#include<sstream>

using namespace std;



int main(){
	
	
	int c, n, s, p, q;
	int above, maybe;
	cin>>c;

	for(int i=0; i<c;i++){
		cin>>n>>s>>p;
		above=0; 
		maybe=0;
		for(int j=0; j<n; j++){
			cin>>q;
			
			if(q>=(3*p-2)){
				above++; 
			}
			else if(q>=max((3*p-4),1)){
				maybe++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<above + min(maybe,s)<<endl;
	}	
	
}
