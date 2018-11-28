#include <iostream>

using namespace std;
typedef long long llong;

int n;
int c[100];

int main(){
	int NN;cin>>NN;
	for(int MM=1;MM<=NN;MM++){
		cin>>n;
		int x=0;
		int m=1000000000;
		llong sum=0;
		for(int i=0;i<n;i++){
			cin>>c[i];
			x^=c[i];
			m=min(m,c[i]);
			sum+=c[i];
		}
		if(x)
			cout<<"Case #"<<MM<<": NO"<<endl;
		else
			cout<<"Case #"<<MM<<": "<<(sum-m)<<endl;
	}
	return 0;
}