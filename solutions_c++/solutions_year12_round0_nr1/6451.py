#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main(){
	int X;
	string Y,Z;
	char A;
	cin>>X;
	for(unsigned i=0;i<=X;i++){
	  getline(cin,Y);
	  for(unsigned j=0;j<Y.size();j++){
			  if(Y[j]=='y'){
				  A='a';
				  Z.push_back(A);}
			  else if(Y[j]=='n'){
				  A='b';
				  Z.push_back(A);}
			  else if(Y[j]=='f'){
				  A='c';
				  Z.push_back(A);}
			  else if(Y[j]=='i'){
				  A='d';
				  Z.push_back(A);}
			  else if(Y[j]=='c'){
			          A='e';
				  Z.push_back(A);}
			  else if(Y[j]=='w'){
				  A='f';
				  Z.push_back(A);}
			  else if(Y[j]=='l'){
				  A='g';
				  Z.push_back(A);}
			  else if(Y[j]=='b'){
				  A='h';
				  Z.push_back(A);}
			  else if(Y[j]=='k'){
				  A='i';
				  Z.push_back(A);}
			  else if(Y[j]=='u'){
				  A='j';
				  Z.push_back(A);}
			  else if(Y[j]=='o'){
				  A='k';
				  Z.push_back(A);}
			  else if(Y[j]=='m'){
				  A='l';
				  Z.push_back(A);}
			  else if(Y[j]=='x'){
				  A='m';
				  Z.push_back(A);}
			  else if(Y[j]=='s'){
				  A='n';
				  Z.push_back(A);}
			  else if(Y[j]=='e'){
				  A='o';
				  Z.push_back(A);}
			  else if(Y[j]=='v'){
				  A='p';
				  Z.push_back(A);}
			  else if(Y[j]=='z'){
				  A='q';
				  Z.push_back(A);}
			  else if(Y[j]=='p'){
				  A='r';
				  Z.push_back(A);}
			  else if(Y[j]=='d'){
				  A='s';
				  Z.push_back(A);}
			  else if(Y[j]=='r'){
				  A='t';
				  Z.push_back(A);}
			  else if(Y[j]=='j'){
				  A='u';
				  Z.push_back(A);}
			  else if(Y[j]=='g'){
				  A='v';
				  Z.push_back(A);}
			  else if(Y[j]=='t'){
				  A='w';
				  Z.push_back(A);}
			  else if(Y[j]=='h'){
				  A='x';
				  Z.push_back(A);}
			  else if(Y[j]=='a'){
				  A='y';
				  Z.push_back(A);}
			  else if(Y[j]=='q'){
				  A='z';
				  Z.push_back(A);}
			  else if(Y[j]==' '){
				  A=' ';
				  Z.push_back(A);
				  }
			  else{
				  A=Y[i];
				  Z.push_back(A);}
			  }
			if(i>0){
			cout<<"Case #"<<i<<": "<<Z<<endl;
			Z.clear();}
		  }
	  }


