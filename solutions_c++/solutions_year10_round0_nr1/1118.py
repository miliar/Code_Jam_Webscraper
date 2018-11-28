// Theme_Park.cpp : Defines the entry point for the console application.
//

#include<iostream>
#include<fstream>

using namespace std;
int T,N,K;
bool *answers;
int main() {
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	fin>>T;
	answers = new bool[T+1];
	for(int i = 1; i <= T; i++) {
		fin>>N>>K;
		unsigned int temp = 1;
		temp = temp << N;
		if(K % temp == temp -1)
			answers[i] = true;
		
		else answers[i] = false;
		//cout<<K<<" "<<temp << " "<<K % temp<<endl;
	}
	for(int i = 1; i <= T; i++)		{
		fout<<"Case #"<<i<<": ";
		if(answers[i])
			fout<<"ON";
		else fout <<"OFF";
		fout<<endl;
	}
	fout.close();
	delete []answers;
	return 0;

}