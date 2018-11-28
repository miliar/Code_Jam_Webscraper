#include <iostream>
#include <algorithm>
using namespace std;

int gcd(int a, int b){
	if (b==0) return a;
	else return gcd(b,a%b);

};

int main(){

	int T;
	cin>>T;

	for (int i=0;i<T;i++){
		cout<<"Case #"<<i+1<<": ";

		long long N;
		int Pd,Pg;
		cin>>N>>Pd>>Pg;

		bool broken=true;

		if (((Pg != 100) && (Pg!=0)) || (Pd==Pg)) {
			broken=false;
			int g=gcd(Pd,100);
			g=100/g;
			if (N<g) broken=true;
		}

		if (broken) cout<<"Broken";
		else cout<<"Possible";

		cout<<endl;
	}


	return 0;
}
