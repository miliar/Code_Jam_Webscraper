#include<iostream>
#include<string>
#include<fstream>
using namespace std;

void main(){
	ofstream cout ("test.txt");
	int triple = 3;
	int T,N,S,p;
	cin >> T;
	for(int i = 0; i < T; i++){
		int count = 0;
		cin >> N >> S >> p;
		for(int j = 0; j < N; j++){
			int ti = 0;cin >> ti;
			if(p==1){
				if(ti>=p)count++;
			}
			else if((ti/triple)>=p)count++;
			else if(ti<(triple*p-(triple-1)*2))continue;
			else if(ti>=(triple*p-(triple-1)*2)&&ti<(triple*p-(triple-1))){
				if(S){
					count++;
					S--;
				}
				else continue;
			}
			else count++;
		}
		cout << "Case #"<<i+1<<": "<<count<<endl;
	}
	system("pause");
}