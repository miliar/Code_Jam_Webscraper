#include<iostream>
#include<stdlib.h>

using namespace std;

int main() {
int T,N,i,j,a,b,t=0;
int lO,lB,pO,pB;
char c;
cin>>T;
for(i=0;i<T;++i) {
	lO=0;lB=0;pO=1;pB=1;t=0;
	cin>>N;
	for(j=0;j<N;++j) {
		cin>>c;
		cin>>a;
		if (c=='O') {
			b=abs(pO-a)-lO;
			if (b<0) b=0;
			t+=1+b;pO=a;lB+=1+b;lO=0; 
			}
		else {
			b=abs(pB-a)-lB;
			if (b<0) b=0;
			t+=1+b;pB=a;lO+=1+b;lB=0;
			}
		}
	cout<<"Case #"<<i+1<<": "<<t<<endl;
	}
}
