#include <iostream>
using namespace std;

int main(){
	int t, a, b, count, c1, c2;
	cin>>t;
	for(int ti=1; ti<=t; ti++){
		cin>>a>>b;
		count=0;
		for(int i=a; i<=b; i++){
			if(i/10==0);
			else{
				if((i/10)/10==0){
					if( i/10<i%10 && b>= ((i%10)*10 + i/10) && i%10!=0)
						count++;
				}
				else{
					c1 = (i%100)*10 + i/100;
					c2 = (i%10)*100 + i/10;
					if(c1>i && c1<=b)
						count++;
					if(c2>i && c2<=b)
						count++;
				}
			}
		}
		cout<<"Case #"<<ti<<": "<<count<<"\n";
	}
	return 0;
}