#include <iostream>

using namespace std;
typedef long long llong;

int n;

int main(){

	int NN;cin>>NN;
	for(int MM=1;MM<=NN;MM++){
		cin>>n;
		int cc=0;
		for(int i=0;i<n;i++) {
			int c;
			cin>>c;
			if(c==i+1)
				cc++;
		}
		cout<<"Case #"<<MM<<": "<<(n-cc)<<".000000"<<endl;
	}
	return 0;
}