#include<iostream>
#include<algorithm>
using namespace std;

int main(){
	int N;
	cin >> N;
	for(int times = 1; times <= N; times++){
		int NA, NB, T;
		int Adeparture[100];
		int Aarrival[100];
		int Bdeparture[100];
		int Barrival[100];
		cin >> T >> NA >> NB;
		char dummy[100];
		cin.getline(dummy, 100);
		for(int i = 0; i < NA; i++){
			int hour;
			int min;
			char timestamp[6] = "";
			cin >> timestamp;
			hour = (timestamp[0] - '0') * 10 + (timestamp[1] - '0');
			min = (timestamp[3] - '0') * 10 + (timestamp[4] - '0');
			Adeparture[i] = hour * 60 + min;
			cin >> timestamp;
			hour = (timestamp[0] - '0') * 10 + (timestamp[1] - '0');
			min = (timestamp[3] - '0') * 10 + (timestamp[4] - '0');
			Aarrival[i] = hour * 60 + min + T;
		}
		for(int i = 0; i < NB; i++){
			int hour;
			int min;
			char timestamp[6] = "";
			cin >> timestamp;
			hour = (timestamp[0] - '0') * 10 + (timestamp[1] - '0');
			min = (timestamp[3] - '0') * 10 + (timestamp[4] - '0');
			Bdeparture[i] = hour * 60 + min;
			cin >> timestamp;
			hour = (timestamp[0] - '0') * 10 + (timestamp[1] - '0');
			min = (timestamp[3] - '0') * 10 + (timestamp[4] - '0');
			Barrival[i] = hour * 60 + min + T;
		}
		sort(Adeparture, Adeparture + NA);
		sort(Aarrival, Aarrival + NA);
		sort(Bdeparture, Bdeparture + NB);
		sort(Barrival, Barrival + NB);
		int ptr;
		int TA;
		ptr = 0;
		TA = 0;
		if(NB == 0){
			TA = NA;
		}
		else{
			for(int i = 0; i < NA; i++){
				if(ptr >= NB){
					TA++;
					continue;
				}
				if(Barrival[ptr] <= Adeparture[i]){
					ptr++;
				}
				else{
					TA++;
				}
			}
		}
		ptr = 0;
		int TB;
		TB = 0;
		if(NA == 0){
			TB = NB;
		}
		else{
			for(int i = 0; i < NB; i++){
				if(ptr >= NA){
					TB++;
					continue;
				}
				if(Aarrival[ptr] <= Bdeparture[i]){
					ptr++;
				}
				else{
					TB++;
				}
			}
		}
		cout << "Case #" << times << ": " << TA << " " << TB << endl;
		NA = NB = T = 0;
		for(int i = 0; i < 100; i++){
			Adeparture[i] = Aarrival[i] = Bdeparture[i] = Barrival[i] = 0;
		}
	}
	return 0;
}
