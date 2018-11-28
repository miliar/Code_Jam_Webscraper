#include <iostream>
#include <fstream>
using namespace std;

long long pot[32];

int main(){
	int i;
	ifstream in("gcjs.in");
	ofstream out("gcjs.out");
	pot[0]=1;
	for(i=1; i<32; i++)pot[i]=pot[i-1]*2;
	
	int T, n, k;
	in>>T;
	int tc=1;
	
	while(tc<=T){
		in>>n>>k;
		out<<"Case #"<<tc<<": ";
		long long pw=pot[n];
		k=k%pw;
		if(k+1==pw)out<<"ON"<<endl;
		else out<<"OFF"<<endl;
		tc++;
		}
	
	}	
