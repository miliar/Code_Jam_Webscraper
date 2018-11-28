// a.cpp, Stefan Veis Pennerup, kumuluzz@gmail.com
// Description: Program for the qualification round, google code jam 2012

#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main(){
	int T,t; //test cases
	int A,B; //The limits
	int y; //number of recycled pairs
	int n,m; //the pairs in between A and B
	int D,d; //number of digits
	int f,x; 

	ifstream input ("small.in");
	ofstream output ("small-output.txt");

	if(!input.is_open())
		cout << "Error" << endl;
	else{
	
	input >> T;
		for(t=0;t<T;t++){
			y=0; D=0;
	
			input >> A;
			input >> B;
			x=A;

			while(x){
				x /= 10;
				D++;
			}	

			if(D==1 || A==B)
				y=0;
			else{
				for(n=A;n<B;n++){
					for(m=n+1;m<=B;m++){
						for(d=1,f=10;d<D;d++,f*=10){
							x = n%f;
							x *= pow(10,(D-d));
							x += n/f;
							if(x==m)
								y++;
						}
					}
				}
			}
		
			output << "Case #" << t+1 << ": " << y << endl;
		}
	}
	return 0;
}
