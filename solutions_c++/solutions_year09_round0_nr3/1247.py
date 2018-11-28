#include<iostream>
#include<stdio.h>
#include<string>

using namespace std;

string inp;
string data="welcome to code jam";
int table[10000];

void init(){

}

void input(){
	getline(cin,inp);	
}

void process(){
	for(int i=0;i<inp.size();i++){
		table[i]=1;
	}
	for(int i=0;i<data.size();i++){
		for(int j=0;j<inp.size();j++){
			int more =0;
			if (data[i]==inp[j]){
				more = table[j];
			}
			table[j]=table[j-1]+more;
			table[j]%=10000;
		}
	}

}
void output(){
	printf("%04d\n",table[inp.size()-1]);	
}

int main(){
	int t;
	cin >> t;
	cin.get();
	for(int i=0;i<t;i++){
		init();
		input();
		process();
		printf("Case #%d: ",i+1);		
		output();
	}
	return 0;
}