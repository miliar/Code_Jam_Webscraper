// codejam1B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
using namespace std;

long c,d,n;
class Stack{
private:
	int i,j,k,pr,pm,pe,po;
	char a[100000];
	char r[100000][3];
	char m[100000][2];
public:
	void empty();
	void rule(char r1, char r2, char r3);
    void clear(char m1, char m2);
    void push(char);
	bool sth();
    char pop();
};

void Stack::empty(){
	i=0;
	pr=0;
	pm=0;
	pe=0;
	po=0;
	a[0]='.';
};

void Stack::rule(char r1, char r2, char r3){
	pr++;
    r[pr][1]=r1;
	r[pr][2]=r2;
	r[pr][3]=r3;
};

void Stack::clear(char m1, char m2){
	pm++;
    m[pm][1]=m1;
	m[pm][2]=m2;
};

void Stack::push(char value){
	j=0;
    for (i=1;i<=c;i++){
		if(((a[pe]==r[i][1])&&(value==r[i][2]))||((a[pe]==r[i][2])&&(value==r[i][1]))){
			a[pe]=r[i][3];
			j=1;
			break;
		}
	}
	if (j==0){
     for (i=1;i<=d;i++){
 	 for (k=1;k<=pe;k++){
		if(((a[k]==m[i][1])&&(value==m[i][2]))||((a[k]==m[i][2])&&(value==m[i][1]))){
			pe=0;
			j=2;
			break;
		}
	 }  
	 }
	}  
    if (j==0){
		a[++pe]=value;
	}
};

bool Stack::sth(){
    if (pe>po){
		return 1;
	}else{
		return 0;
	}
};

char Stack::pop(){
	return a[++po];
};

int main(int argc, char* argv[]){

    ifstream fin("B-large.in");
	ofstream fout("B-large.out");
    
    long i,j,k,t,sum,min,bit;
    char r,ru[3],ma[2];
    Stack s;

	fin >> t;
	for (i=1;i<=t;i++){
      s.empty();

      fin >> c;
      for (j=1;j<=c;j++){
	    fin >> ru[1] >> ru[2] >> ru[3];
		s.rule(ru[1],ru[2],ru[3]);
	  }

	  fin >> d;
      for (j=1;j<=d;j++){
	    fin >> ma[1] >> ma[2];
		s.clear(ma[1],ma[2]);
	  }

	  fin >> n;
      for (j=1;j<=n;j++){
	    fin >> r;
		s.push(r);
	  }	  
	  
	  fout << "Case #" << i << ": [";
	  while (s.sth()){
		  fout << s.pop();
		  if (s.sth()){
             fout << ", ";
		  }
	  }
	  fout << "]" << endl;
	}
	fin.close();
	fout.close();
	return 0;
}