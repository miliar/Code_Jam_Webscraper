#include <iostream>

using namespace std;

int main(){
	int T;
	cin>>T;

	for (int i=0;i<T;i++){
		int N;
		cin>>N;

		int min,sum,xorall;
		cin>>min;
		xorall=sum=min;
		for (int j=1;j<N;j++){
			int c;
			cin>>c;
			xorall=xorall^c;
			if (c<min) min=c;
			sum+=c;
		}

		cout<<"Case #"<<i+1<<": ";
		if (xorall==0) cout<<sum-min<<endl;
		else cout<<"NO"<<endl;
	}

	return 0;
}
