#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int main(){
	ofstream out("out.txt");
	int N;
	cin>>N;
	for(int i=0;i<N;i++){
		int P,K,L;
		cin>>P>>K>>L;
		int a[L];
		for(int j=0;j<L;j++)
			cin>>a[j];
		sort(a,a+L,greater<int>() );
		int min=0;
		for(int j=0;j<L;j++)
			min+=(j/K+1)*a[j];
		out<<"Case #"<<i+1<<": "<<min<<endl;
	}
}
