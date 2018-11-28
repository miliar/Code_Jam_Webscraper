#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	int T;
	cin>>T;

	for (int i=0;i<T;i++){
		int N;
		cin>>N;
		int s=0;
		for (int j=0;j<N;j++){
			int k;
			cin>>k;
			k--;
			if (j==k) s++;
		}

                double t=(double)N-s;
                cout<<"Case #"<<i+1<<": "<<fixed<<setprecision(6)<<t<<endl;
	}

	return 0;
}
