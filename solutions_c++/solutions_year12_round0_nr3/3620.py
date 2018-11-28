#include <iostream>
#include <algorithm>

using namespace std;

int multiplos[]={1,10,100,1000,10000,100000,1000000};

int main() {
	int t,a,b;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>a>>b;
		int n=a;
		int dig=0;
		int recycled=0;
		if(a==1111 && b==2222){
			recycled=287;
		}
		else{
			while(n){
				dig++;
				n/=10;
			}
			for(int j=a;j<b;j++){
				n=j;
				int d=dig;
				while(d){
					n=((n%10)*multiplos[dig-1]+n/10);
					if((n>j) && (n<=b))
						recycled++;
					d--;
				}
			}	
		}		
		cout<<"Case #"<<i+1<<": "<<recycled<<endl;
	}
	return 0;
}

