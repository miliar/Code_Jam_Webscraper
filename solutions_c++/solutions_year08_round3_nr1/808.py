#include <iostream>
#include <fstream>

int N,P,K,L;
int *F;
int result=0;

using namespace std;

void main(){

	fstream in,out;
	in.open("A-small.in",ios::in);
	out.open("A-small.out",ios::out);

	in>>N;

	for(int c=1; c<=N; ++c){		//each case
		
		result=0;
		
		in>>P>>K>>L;

		F= new int[L];

		for(int l=0; l<L; ++l)
			in>>F[l];

		int value,j;

		for(int s=1; s<L; ++s){		//sorting
			value= F[s];
			j= s-1;
			while(j>=0 && F[j]>value){
				F[j+1]= F[j];
				j= j-1;
			}
			F[j+1]= value;
		}
		
		int m=1,i=1;
		for(int k=(L-1); k>=0; --k){
			result += F[k] * m;
			++i;
			if(i>K){
				++m;
				i=1;
			}
		}

		out<<"Case #"<<c<<": "<<result<<endl;;
	}

}

