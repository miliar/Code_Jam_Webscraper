#include <iostream>
#include <fstream>
#include <map>
using namespace std;

int main(){
	map<char,char> d;
 	d['a'] = 'y';
       d['b'] = 'h';
       d['c'] = 'e';
       d['d'] = 's';
       d['e'] = 'o';
       d['f'] = 'c';
       d['g'] = 'v';
       d['h'] = 'x';
       d['i'] = 'd';
	d['j'] = 'u';
       d['k'] = 'i';
       d['l'] = 'g';
       d['m'] = 'l';
       d['n'] = 'b';
       d['o'] = 'k';
       d['p'] = 'r';
       d['q'] = 'z';
       d['r'] = 't';
       d['s'] = 'n';
       d['t'] = 'w';
	d['u'] = 'j';
       d['v'] = 'p';
       d['w'] = 'f';
       d['x'] = 'm';
       d['y'] = 'a';
       d['z'] = 'q';
       d[' '] = ' ';
	ifstream infile;
	ofstream outfile;
	char inname[50];
	cout<<"output inname: ";
	cin>>inname;
	infile.open(inname);
	outfile.open("p1Ans.txt");
	int T;
	infile>>T;
	int I=1;
	string line;
	getline(infile,line);
	while(I<=T){
		char out[101]={NULL};
		getline(infile,line,'\n');
		for (int i=0;i<line.length();++i){
			out[i]=d[line[i]];
		}
		outfile<<"Case #"<<I<<": "<<out<<"\n";
		cout<<out<<"\n";
		++I;
	}
return 0;
}
