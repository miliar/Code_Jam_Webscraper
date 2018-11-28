#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int get_result(string &,vector<string> &);
bool isIn(string &,string &);

int main(){
	ifstream fin;
	fin.open("A-large.in");
	if(!fin.is_open()){
		cout<<"File open failed!"<<endl;
		exit(1);
	}

	int L,D,N;
	fin>>L;
	fin>>D;
	fin>>N;

	string str;
	vector<string> word;
	int i;

	getline(fin,str);
	for(i=0;i<D;i++){
		getline(fin,str);
		word.push_back(str);
	}

	ofstream fout;
	fout.open("A-large.out");
	if(!fout.is_open()){
		cout<<"File open failed!"<<endl;
		exit(1);
	}
	for(i=0;i<N;i++){
		getline(fin,str);
		fout<<"Case #"<<i+1<<": "<<get_result(str,word)<<endl;
	}

	fout.close();
	fin.close();
	return 0;
}

int get_result(string & str,vector<string> & word){
	int result=0;
	vector<string>::iterator iter;
	for(iter=word.begin();iter!=word.end();iter++){
		if(isIn(*iter,str)){
			result++;
		}
	}
	return result;
}

bool isIn(string & str1,string & str2){
	int n1=str1.length();
	int n2=str2.length();
	int i,j;
	for(i=0,j=0;i<n1;i++){
		if(str1[i]==str2[j]){
			j++;
			continue;
		}
		if(str2[j]=='('){
			int loop=0;
			while(str2[j]!=')'){
				if(str2[j]==str1[i]){
					loop=1;
				}	
				j++;
			}
			j++;
			if(loop==1){
				continue;
			}else{
				return false;
			}
		}
		return false;
	}
	return true;
}