#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

int main (int argc, char * const argv[]) {
	
	char str[20];
	fstream file1;
	fstream file2;
	file1.open("C-small-attempt0.in",ios::in);
	file2.open("output.in", ios::out);
	
	int T = 0,i=0;
	file1>>str;
	while(str[i]){
		T += (str[i]-48);
		i++;
		T*=10;
	}
	T/=10;
	
	int R;int K;int N;
	long totalCost;
	for(int t = 0 ; t<T ; t++){
		totalCost = 0;
		//Get R - No of time s in the day
		file1>>str;
		i = 0 ; R=0;
		while(str[i]){
			R += (str[i]-48);
			i++;
			R*=10;
		}
		R/=10;
		
		//Get K - Capacity
		file1>>str;
		i = 0 , K=0;
		while(str[i]){
			K += (str[i]-48);
			i++;
			K*=10;
		}
		K/=10;	
		
		//Get N - No of groups
		file1>>str;
		i = 0 , N=0;
		while(str[i]){
			N += (str[i]-48);
			i++;
			N*=10;
		}
		N/=10;
		
		cout<<"Input 1: "<<R<<K<<N<<"\n";
		int noInGroup[N];
		for(int j = 0 ; j < N ; j++){
			file1>>str;
			i = 0 , noInGroup[j]=0;
			while(str[i]){
				noInGroup[j] += (str[i]-48);
				i++;
				noInGroup[j]*=10;
			}
			noInGroup[j]/=10;	
		}
		
		for(int timesToGo=0; timesToGo<R ; timesToGo++){
			int sum = noInGroup[0];
			int noOftimesToShift = 1;
			while (sum<=K&&noOftimesToShift<=N) {
				sum+=noInGroup[noOftimesToShift];
				noOftimesToShift++;
			}
			noOftimesToShift--;
			sum-=noInGroup[noOftimesToShift];
			int tempVal=0;
			for(int j = 0 ; j < noOftimesToShift; j++){
				tempVal = noInGroup[0];
				for(int k = 0 ; k < N-1 ; k++){
					noInGroup[k] = noInGroup[k+1];
				}
				noInGroup[N-1] = tempVal;
			}
			totalCost+=sum;
		}
		file2 << "Case #" << (t + 1) << ": " <<totalCost<< "\n";
	}
	
	file2.close();
	file1.close();
    return 0;
}
