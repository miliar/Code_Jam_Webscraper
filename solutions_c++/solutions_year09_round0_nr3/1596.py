#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
using namespace std;

int findRest(string line,int k, int start);

int main(){
	fstream inputf,outputf;	
	string inputFile;
	cin >> inputFile;
	inputf.open(inputFile.c_str(),fstream::in);
	if (!inputf){
		cout<<"No file!";
		return -1;
	}
	outputf.open("output.out",fstream::out);
	int N;
	inputf >> N;
	string str;
	getline(inputf,str);
	for (int cntN=0;cntN<N;cntN++){
		getline(inputf,str);
		int result=findRest(str,1,0);
		outputf<<"Case #"<<cntN+1<<":"<<setfill('0') << setw(4)<<result<<endl;
	}
	
	inputf.close();
	outputf.close();
	return 0;
}

int findRest(string line,int k, int start){
	string src="welcome to code jam";
	if (k>src.length()){
		return 1;
	}
	char look=src[k-1];
	int sum=0;
	while(start!=line.length()){
		if (line[start]==look){
			sum+=findRest(line,k+1,start+1);
			if (sum>10000)
				sum-=10000;
		}
		start++;
	}
	return sum;
}