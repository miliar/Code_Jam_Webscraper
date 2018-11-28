#include<iostream>
#include<fstream>

using namespace std;

int main(){
	ifstream in;
	ofstream out;

	in.open("input.txt");
	out.open("output.txt");
	int T;
	int cs=0;
	in>>T;
	while(cs++<T){
		int n,min=1000000;
		int inc=0;
		int sum=0;

		in>>n;

		for(int i=0;i<n;i++){
			int t;
			in>>t;
			inc^=t;
			if(min>t) min=t;
			sum+=t;
		}
		if(inc==0) out<<"Case #"<<cs<<": "<<sum-min<<endl;
		else out<<"Case #"<<cs<<": "<<"NO"<<endl;
		
	}

	
	
}