#include<iostream>
#include<fstream>
#include<string>

#include<sstream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<map>
using namespace std;
map<char, char> gmap;
void initialize(){
	gmap[' '] = ' ';
	gmap['a'] = 'y';
	gmap['b'] = 'h';
	gmap['c'] = 'e';
	gmap['d'] = 's';
	gmap['e'] = 'o';
	gmap['f'] = 'c';
	gmap['g'] = 'v';
	gmap['h'] = 'x';
	gmap['i'] = 'd';
	gmap['j'] = 'u';
	gmap['k'] = 'i';
	gmap['l'] = 'g';
	gmap['m'] = 'l';
	gmap['n'] = 'b';
	gmap['o'] = 'k';
	gmap['p'] = 'r';
	gmap['q'] = 'z';
	gmap['r'] = 't';
	gmap['s'] = 'n';
	gmap['t'] = 'w';
	gmap['u'] = 'j';
	gmap['v'] = 'p';
	gmap['w'] = 'f';
	gmap['x'] = 'm';
	gmap['y'] = 'a';
	gmap['z'] = 'q';
}
string translation(string g){
	string a="";
	int len = g.length();
	for(int i=0;i<len;i++){
		a=a+gmap.find(g[i])->second;
	}

	return a;
}
int main(){
	int testcase;
	ifstream infile;
	ofstream outfile;
	initialize();
	infile.open("A-small-attempt0.in"); //filename//
	outfile.open("result.txt");
	
	infile>>testcase;
	string temp;
	getline(infile, temp);

	for(int i=0;i<testcase;i++){
		//do something
		string g;
		getline(infile, g);

		//do something end
		string result=translation(g);
		outfile<<"Case #"<<i+1<<": "<<result<<"\n";
	}
	infile.close();
	outfile.close();
	return 0;
}