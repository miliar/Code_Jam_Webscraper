#include <iostream>
#include <fstream>
using namespace std;

int main(){
	fstream file("C-large.in",ios::in);
	fstream file_out("C-large.out",ios::out);
	
	

	int T,N;
	file>>T;
	for(int i=0 ; i<T ;i++){
		file>>N;
		long int a,b,small,total=0;
		file>>a;
		total+=a;
		small=a;

		for(int j=0 ; j<N-1 ; j++){
			file>>b;
			a^=b;
			small>b ? small=b : 0;
			total+=b;
		}


		if(a!=0)
			file_out<<"Case #"<<i+1<<": "<<"NO"<<endl;
		else
			file_out<<"Case #"<<i+1<<": "<<total-small<<endl;
	}

}