#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <cmath>

using namespace std;

int main(){
	ifstream in;
	ofstream out;
	
	in.open("A-large.in");
	out.open("output.txt");

	

	int T;
	in>>T;
	cout<<T<<endl;

	for(int i=0;i<T;i++){
		long long N;
		in>>N;

		int pd;
		in>>pd;

		int pg;
		in>>pg;

		

		if(pd==0&&pg!=100){
			out<<"Case #"<<(i+1)<<": Possible"<<endl;
			continue;
		}
		else if(pd==0){
			out<<"Case #"<<(i+1)<<": Broken"<<endl;
			continue;
		}

			int count=0;
			for(long long j=N;j>=1;j--){
				double D = (pd*j)/100.0;
				long long Dexact=D;
				//cout<<D<<" "<<Dexact<<endl;
				if(abs((double)(D-Dexact))<=1e-9){
					count++;
					if(pg==pd){
						out<<"Case #"<<(i+1)<<": Possible"<<endl;
						break;
					}
					else if(pg!=100&&pg!=0){
						out<<"Case #"<<(i+1)<<": Possible"<<endl;
						break;
					}
					else{
						out<<"Case #"<<(i+1)<<": Broken"<<endl;
						break;
					}
				}
			}
			if(count!=1){
				out<<"Case #"<<(i+1)<<": Broken"<<endl;
			}
			cout<<i<<endl;

	}

	in.close();
	out.close();

	return 0;
}