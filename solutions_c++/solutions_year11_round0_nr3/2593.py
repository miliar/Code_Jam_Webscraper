#include<iostream>
#include<climits>

using namespace std;
int main() {
int min,x,T,N,i,j,s,a;

cin>>T;
for(i=0;i<T;++i) {
	cin>>N;
	min=INT_MAX; s=0;x=0;
	for(j=0;j<N;++j) {
		cin>>a;
		s+=a;
		if (a<min) min=a;
		x=x^a;
		}
	if (x==0) cout<<"Case #"<<i+1<<": "<<s-min<<endl;
	else cout<<"Case #"<<i+1<<": NO"<<endl;
	}
return 0;
}
