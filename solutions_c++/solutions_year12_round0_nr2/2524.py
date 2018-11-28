#include <iostream>
#include <math.h>
using namespace std;


int main() {
	int T;
	cin >>T;
	for (int t=1; t<=T; t++){	
		cout<<"Case #"<<t<<": ";
		int N,S,p;
		int maxBest = 0;
		cin>>N>>S>>p;
//		cout<<"|"<<N<<" "<<S<<" "<<p<<": ";
		int score[N];
		for (int n=0; n<N; n++)
			cin>>score[n];
	//do work here
		for(int n=0; n<N; n++){
		//	cout<<score[n]<<" ";
			if (score[n] < p) continue;
			int foo = score[n] - p*3;
			if (foo >= -2)
				maxBest++;
			else if (foo >= -4 && S!=0){
				S--;
				maxBest++;
			}
		
		}


		cout<<maxBest<<endl;
	}
}
