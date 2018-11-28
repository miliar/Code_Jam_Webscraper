#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

long get_result(string &);

int main(){
	ifstream fin;
	fin.open("a.in");
	if(!fin.is_open()){
		cout<<"File open failed!"<<endl;
		exit(1);
	}
	ofstream fout;
	fout.open("a.out");
	if(!fout.is_open()){
		cout<<"File open failed!"<<endl;
		exit(1);
	}
	
	int T;
	fin>>T;

	int i;
	string str;
	long result;
	getline(fin,str);
	for(i=0;i<T;i++){
		getline(fin,str);
		result=get_result(str);
		fout<<"Case #"<<i+1<<": "<<result<<endl;
	}

	fin.close();
	fout.close();
	return 0;
}

long get_result(string & str){
	int i;
	int length=str.length();
	int cur=0;
	int * parray=new int[length];
	parray[0]=1;
	for(i=1;i<length;i++){
		int j;
		for(j=0;j<i;j++){
			if(str[i]==str[j]){
				parray[i]=parray[j];
				break;
			}
		}
		if(i==j){
			if(cur==1){
				cur++;
			}
			parray[i]=cur;
			cur++;
		}
	}

	long result=0;
	if(cur==1||cur==0){
		cur=2;
	}
	for(i=0;i<length;i++){
		result=result+parray[i]*pow((double)cur,length-1-i);
	}

	delete[] parray;

	return result;
}