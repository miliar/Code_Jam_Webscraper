#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;



int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int min=1000001;
		int xors=0;
		int sum=0;
		int n;
		cin>>n;
		for(int j=0;j<n;j++){
			int v;
			cin>>v;
			if(v<min)
				min=v;
			sum+=v;
			xors^=v;
		}
		if(xors)
			cout<<"Case #"<<i<<": NO"<<endl;
		else
			cout<<"Case #"<<i<<": "<<(sum-min)<<endl;
		
	}
	return 0;
}
