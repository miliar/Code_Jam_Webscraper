#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

int main (int argc, char * const argv[]) {
	
	char str[20];
	fstream file1;
	fstream file2;
	file1.open("A-large.in",ios::in);
	file2.open("output.in", ios::out);
	file1>>str;
	int i = 0 , numberOfTimes=0;
	while(str[i]){
		numberOfTimes += (str[i]-48);
		i++;
		numberOfTimes*=10;
	}
	numberOfTimes/=10;
	 
	long divisor;int rem;
	int N,K;
	for (int k = 0; k < numberOfTimes; k++) {
		
		//Get N
		file1>>str;
		i = 0 , N=0;
		while(str[i]){
			N += (str[i]-48);
			i++;
			N*=10;
		}
		N/=10;
		
		//Get K
		file1>>str;
		i = 0 , K=0;
		while(str[i]){
			K += (str[i]-48);
			i++;
			K*=10;
		}
		K/=10;
		K++;
		
		divisor = 1;
		for(int j = 0; j < N; j++)
			divisor *= 2;
		
		rem = K%divisor;
		if(rem == 0)
		file2 << "Case #" << (k + 1) << ": ON" << "\n";
		else
		file2 << "Case #" << (k + 1) << ": OFF" << "\n";
	}
	file2.close();
	file1.close();
    return 0;
}
