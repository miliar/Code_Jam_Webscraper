#include<iostream>
#include<fstream>

using namespace std;

int main(){
	
	ifstream in;
	ofstream out;
	in.open("input.txt");
	out.open("output.txt");
	
	int T,t=0;

	in>>T;

	while((t++)<T){
		long long int N,pd,pg;
		int br=0;

		in>>N>>pd>>pg;

		if((pd==100) || (pg==100)){
			if(pd!=pg) br=1;
		}
		if((pd==0) || (pg==0)){
			if(pd!=pg) br=1;
		}


		int x=100;
		while(x%2==0 && pd%2==0){ x/=2; pd/=2;}
		while(x%5==0 && pd%5==0){ x/=5; pd/=5;}

		if(N<x) br=1;

		if(!br) out<<"Case #"<<t<<": Possible"<<endl;
		else out<<"Case #"<<t<<": Broken"<<endl;
	}


	return 0;
}