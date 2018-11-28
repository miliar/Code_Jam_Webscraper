#include "HH.h"

ifstream input("C:/Users/Yeqi SUN/Desktop/A-large.in");
ofstream output("C:/Users/Yeqi SUN/Desktop/test.out");



void main(){
	long long T, N, K;
	input >> T;
	FOR(i, T){
		input >> N >> K;
		vector<long long > time(100,0);
		for(int j=1;j<= N;j++ ){
			if( j == 1)
				time[j] = 1;
			else{
				time[j]=time[j-1]*2+1;
			}
		}
		output << "Case #" << i+1 << ": ";
		if( K % (time[N]+1) == time[N]   )
			output<<  "ON";
		else
			output << "OFF";
		output<<endl;
	}



	system("pause");
}