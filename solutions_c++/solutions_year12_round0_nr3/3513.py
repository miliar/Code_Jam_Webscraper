#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[]){
	int numOfCases, a, b;

	ofstream output;
	ifstream input;
	
	input.open(argv[1]);
	if (!input){
		cout << "Cannot open file "<<argv[1]<<endl;
		return -1;
	}
	cout << "File "<< argv[1] <<" opened for reading" <<endl;

	output.open(argv[2]);
	if (!output){
		cout << "Cannot open file "<<argv[2]<<endl;
		return -1;
	}
	cout << "File "<< argv[2] <<" opened for writing" <<endl;

	input>>numOfCases;

	for(int i=0; i<numOfCases; i++){
		input>>a;
		input>>b;
		output<<"Case #"<<i+1<<": ";

		int numOfDigits = 0;	//number of digits each number have
		int k=a;
		while(k>0){
			k = k/10;
			numOfDigits++;
		}

		int recycled = 0;

		if (numOfDigits==1) output<<recycled<<endl;
		else{
			for(int j=a; j<=b; j++){
				int div=10, mul=1;
				for(int l=0; l<numOfDigits-1; l++){
					mul = mul * 10;
				}
				for(int l=0; l<numOfDigits-1; l++){
					int temp1 = j % div;
					int temp2 = j / div;
					temp1 = temp1 * mul + temp2;
					if ((temp1>=a)&&(temp1<=b)&&(temp1>j)) recycled++; 
					mul = mul/10;
					div = div*10;
				}

			}
			output<<recycled<<endl;
		}
	}	

	cout<<"Work finished"<<endl;
	input.close();
	output.close();

	return 0;


}