#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip.h>
#include <string>
using namespace std;

int GCD(int a, int b){
		        if (b==0) return a;
				        return GCD(b, a%b);
}

int LCM(int a, int b){
		        return b*a/GCD(a, b);
}

int main(int argc, char *argv[]){
		ifstream ins;
		ins.open(argv[1]);
		int Ncase;
		ins>>Ncase;
		int the_case = 0;
		while (the_case++ < Ncase){
				int N, low, high;
				ins>>N>>low>>high;
				vector<int> freq;
				for (int i=0; i<N; ++i){
						int temp;
						ins>>temp;
						freq.push_back(temp);
				}
				//first find the LCM
				int the_freq=0;
				bool jump=false;
				for (int k=low; k<=high; ++k){
						bool divide=true;
						for (int i=0; i<N; ++i){
								if (k%freq[i]!=0 && freq[i]%k!=0){
										divide=false;
										break;
								}	
						}
						if (divide==false){
								continue;
						} else {
								the_freq=k;
								jump=true;
								break;
						}
				}
				cout<<"Case #"<<the_case<<": ";
				if (jump){
						cout<<the_freq<<endl;
				} else {
						cout<<"NO"<<endl;
				}

		}
		ins.close();
		return 0;
}

