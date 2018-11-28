#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<fstream>
#include<cmath>
using namespace std;



int main(){
	ifstream in;
	ofstream out;
	in.open("B-small-attempt2.in");
	out.open("out.txt");
	int T;
	in>>T;
	for(int k=0;k<T;k++){
		int N,S,P,count=0;
		in>>N>>S>>P;
		vector<int> googlers;
		for(int j=0;j<N;j++){
			int pivot;
			in>>pivot;
			googlers.push_back(pivot);
		}
		sort(googlers.begin(),googlers.end());
		int f=N-1;
		for(f;f>=0;f--){
			double temp=ceil((googlers[f]+0.0)/3);
			if(temp>=P) count++;
			else if(temp+1>=P && S>0 && temp>0) {count++; S--;}
		}

		out<<"Case #"<<k+1<<": "<<count<<endl;

	}
	return 0;


}