#include <iostream>
#include <vector>
using namespace std;
int main(){
	int T,t,x,y;
	int n,k;
	
	cin>>T;
	t = 1;
	while(T--){
		cin>>n>>k;
		
		x = 1<<n;
		y = k%x;
		printf("Case #%d: ",t);
		if(y == (x-1))
			cout<<"ON"<<endl;
		else
			cout<<"OFF"<<endl;
		t++;
	}
	return 0;
}
			
			
		
	

	
	
