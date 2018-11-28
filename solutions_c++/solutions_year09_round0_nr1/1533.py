#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

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
	int L,D,N;
	inputf >> L >> D >> N;
	string* words=new string[D];
	for (int i=0;i<D;i++)
		inputf >> words[i];
	for (int cntN=0;cntN<N;cntN++){
		string input;
		inputf >> input;
		int result=0;
		string *sets= new string[L];
		int next=0;
		for (int i=0;i<L;i++){
			if (input[next]=='('){
				next++;
				while (input[next]!=')'){
					sets[i].push_back(input[next]);
					next++;
				}
				next++;
			}
			else{
				sets[i].push_back(input[next]);
				next++;
			}
		}
		for (int i=0;i<D;i++){
			bool flag=true;
			for (int j=0;j<L;j++){
				const char* current=sets[j].c_str();
				char curCh=words[i][j];
				int len=sets[j].length();
				if (find(current,current+len,curCh)==current+len){
					flag=false;
					break;
				}
			}
			if (flag)
				result++;
		}
		outputf<<"Case #"<<cntN+1<<": "<<result<<endl;
	}
	inputf.close();
	outputf.close();
	return 0;
}
