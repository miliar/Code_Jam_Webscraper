#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	int d,a,b;
	string s;
	cin>>d;
	for(int i=1;i<=d;i++){
		cin>>a>>b;
		if(b==0){
			cout<<"Case #"<<i<<": OFF\n";		
			continue;
		}
		
		if(a==1 && b==1){
			cout<<"Case #"<<i<<": ON\n";
			continue;
		}
		int tmp=a;
		int j=0;
		while(a>0 || b>0){
			if(b%2==0){
				break;
			}			
			b/=2;
			j++;
			--a;
		}
		if(j<tmp){
			printf("Case #%d: OFF\n",i);
			continue;
		}
		printf("Case #%d: ON\n",i);
	}	

}

