#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;
int main(){
	char a[26];
	a[0]='y';	//a
	a[1]='h';	//b
	a[2]='e';	//c
	a[3]='s';	//d
	a[4]='o';	//e	
	a[5]='c';	//f
	a[6]='v';	//g
	a[7]='x';	//h
	a[8]='d';	//i
	a[9]='u';	//j
	a[10]='i';	//k
	a[11]='g';	//l
	a[12]='l';	//m
	a[13]='b';	//n
	a[14]='k';	//o
	a[15]='r';	//p
	a[16]='z';	//q
	a[17]='t';	//r
	a[18]='n';	//s
	a[19]='w';	//t
	a[20]='j';	//u
	a[21]='p';	//v
	a[22]='f';	//w
	a[23]='m';	//x
	a[24]='a';	//y
	a[25]='q';	//z
	int T;
	cin>>T;
	string str;
	getline(cin,str);
	for(int i=0;i<T;i++){		
		int j=0;
		getline(cin,str);
		cout<<"Case #"<<i+1<<": ";
		
		while(j!=str.size()){
			if(str[j]==' ')
				cout<<" ";
			else
				cout<<a[str[j]-97];
		j++;
		}
		cout<<endl;	
	}
}
