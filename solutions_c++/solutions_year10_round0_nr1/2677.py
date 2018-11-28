#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main(){

	ifstream ifs("A-large.in");
	ofstream ofs("A-large.out");

	int TOTAL_CASE;
	ifs>>TOTAL_CASE;
	for(int CASE  = 1 ; CASE <= TOTAL_CASE ; CASE++){

		bool isOn = false;
		int N,K;
		ifs>>N>>K;

		int firstOn = 1;
		int interval = pow(2.0,N);

		for(int i = 1 ; i < N ; i++){
			firstOn += pow(2.0,i);
		}
		
		if(firstOn == K) isOn = true;
		if(firstOn < K){
			if((K - firstOn)%interval == 0) isOn = true;
		}

		ofs<<"Case #"<<CASE<<": ";
		if(isOn) ofs<<"ON"<<endl;
		else ofs<<"OFF"<<endl;


	}

	ifs.close();
	ofs.close();
	return 0;

}