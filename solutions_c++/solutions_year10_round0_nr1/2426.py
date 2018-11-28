#include<iostream>
#include<fstream>
using namespace std;
int T;
int* N;
int* K;
int ref[31];

void calcRef(){
	ref[0] = 0;
	for(int i=1; i<31; i++)
		for(int j=i-1; j>=0; j--)
			ref[i] += ref[j]+1;
}
int main(){
	ifstream fin;
	fin.open("A-large.in");
	

	ofstream fout;
	fout.open("out.large");
	if(!fin || !fout)
		cout<<"Error!"<<endl;
	calcRef();
	
	fin>>T;
	N = new int[T];
	K = new int[T];

	//cout<<f(4);
	for(int i=0; i<T; i++){
		fin>>N[i];
		fin>>K[i];
		int fn = ref[N[i]];
		if(K[i]%(fn+1) == fn)
			fout<<"Case #"<<i+1<<":	ON\n";
		else
			fout<<"Case #"<<i+1<<":	OFF\n";


	}
}