#include <fstream>
using namespace std;

void main(){
	ifstream in;
	ofstream out;
	in.open("A-small.in");
	out.open("A-small.out");
	int T;
	in>>T;
	for(int cases=0;cases<T;cases++){
		int N,PD,PG;
		in>>N>>PD>>PG;
		bool found=false;
		int gcd_found;
		for(int gcd=PD;gcd>0&&found==false;gcd--){
			if(PD%gcd==0&&100%gcd==0){
				found=true;
				gcd_found=gcd;
			}
		}
		bool gcd_exist=found;
		bool test;
		if(gcd_exist){
			int multiples=100/gcd_found;
			if(N<multiples) test=false;
			else{
				test=true;
				if(PG==100&&PD<100) test=false;
				else if(PG==0&&PD>0) test=false;
			}
		}else{
			test=true;
			if(PG==100&&PD<100) test=false;
			else if(PG==0&&PD>0) test=false;
		}
		out<<"Case #"<<(cases+1)<<": ";
		if(test==false) out<<"Broken"<<endl;
		else out<<"Possible"<<endl;
	}
	in.close();
	out.close();
}