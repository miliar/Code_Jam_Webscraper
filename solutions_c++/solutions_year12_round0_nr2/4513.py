#include<iostream>
#include<cstdlib>
using namespace std;

int main(){
	int T;
	cin>>T;
	int i=0;
	while(i<T){
		int N,S,p;
		int c1=0; // >=3p-2
		int c2=0; // <3p-2 and >3p-5
		cin>>N>>S>>p;
		int x=0;
		for(int k=0; k<N; k++){
			cin>>x;
			if(x>=3*p-2) c1++;
			else if(x<3*p-2 && x>3*p-5 && p==1 && x==0) {}
			else if (x<3*p-2 && x>3*p-5) c2++;
		}
		int ans=0;
		ans+=c1;
		if(S>0 && S>=c2) ans+=c2;
		else if(S>=0 && S<c2) ans+=S;
		else{}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
		i++;
	}
	return 0;
}
