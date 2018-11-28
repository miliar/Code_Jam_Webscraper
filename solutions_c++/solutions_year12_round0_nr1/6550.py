#include<iostream>
#include<conio.h>
#include<string>
#include<fstream>
using namespace std;
void main() {
	int t;
	string temp;
	ifstream in;
	ofstream out;
	in.open("ahmed.in",ios::binary);
	out.open("output.in",ios::out);
	in>>t;
	getline(in,temp);
	for(int i=0;i<t;i++) {
		getline(in,temp);
		for(int j=0;j<temp.size();j++) {
			if(temp[j]=='a')
				temp[j] = 'y';
			else if(temp[j]=='b')
				temp[j] = 'h';
			else if(temp[j]=='c')
				temp[j] = 'e';
			else if(temp[j]=='d')
				temp[j] = 's';
			else if(temp[j]=='e')
				temp[j] = 'o';
			else if(temp[j]=='f')
				temp[j] = 'c';
			else if(temp[j]=='g')
				temp[j] = 'v';
			else if(temp[j]=='h')
				temp[j] = 'x';
			else if(temp[j]=='i')
				temp[j] = 'd';
			else if(temp[j]=='j')
				temp[j] = 'u';
			else if(temp[j]=='k')
				temp[j] = 'i';
			else if(temp[j]=='l')
				temp[j] = 'g';
			else if(temp[j]=='m')
				temp[j] = 'l';
			else if(temp[j]=='n')
				temp[j] = 'b';
			else if(temp[j]=='o')
				temp[j] = 'k';
			else if(temp[j]=='p')
				temp[j] = 'r';
			else if(temp[j]=='r')
				temp[j] = 't';
			else if(temp[j]=='s')
				temp[j] = 'n';
			else if(temp[j]=='t')
				temp[j] = 'w';
			else if(temp[j]=='u')
				temp[j] = 'j';
			else if(temp[j]=='v')
				temp[j] = 'p';
			else if(temp[j]=='w')
				temp[j] = 'f';
			else if(temp[j]=='x')
				temp[j] = 'm';
			else if(temp[j]=='y')
				temp[j] = 'a';
			else if(temp[j]=='q')
				temp[j] = 'z';
			else if(temp[j]=='z')
				temp[j] = 'q';
		}
		out<<"Case #"<<i+1<<": "<<temp<<endl;
	}
	in.close();
	out.close();
}
