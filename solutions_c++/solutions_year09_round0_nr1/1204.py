#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string>
#include<fstream>

using namespace std;

#define N 10000

string data[N];

int t,l,d;
int answer=0;

void init(){
	answer=0;
}

void input(){
	string ss;
	cin >> ss;

	for(int i=0;i<d;i++){
		int type=0;
		int now=0;
		for(int j=0;j<ss.length();j++){			
			if (data[i][now]==ss[j]){
				if (type==1) 
					type=2;
				else
					now++;
				continue;
			}
			if (ss[j]=='('){
				type=1;
			}
			else if (ss[j]==')'){
				if (type==2) {
					type=0;
					now++;
				}
				else 
					break;
			}
		}
		if (now==l) answer++;
	}
}


void process(){

}

void output(){
	cout << answer <<endl;
}

int main(){
	int i=0;
	cin >> l >> d >> t;
	for(int i=0;i<d;i++){
		cin >> data[i];
	}
	for(int i=1;i<=t;i++){		
		cout <<"Case #"<<i <<": ";
		init();		
		input();
		process();
		output();
	}
	return 0;
}