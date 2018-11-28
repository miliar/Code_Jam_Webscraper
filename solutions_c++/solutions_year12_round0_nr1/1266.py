#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
char alpha[26];

char translate(const char c){
	if(c == ' ') return c;
	return alpha[c-'a'];
}

using namespace std;
int main(){
	char* g = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
			"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
			"de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char* c ="our language is impossible to understand"
			"there are twenty six factorial possibilities"
			"so it is okay if you want to just give up";
	while(*g!='\0'){
		if(*g !=' ')
			alpha[*g-'a']=*c;
		++g;++c;
	}
	alpha['q'-'a']='z';
	alpha['z'-'a']='q';


	ifstream fin;
	ofstream fout;
	fin.open("inout/A.in");
	fout.open("inout/A.out");
	int T;
	fin >> T;
	string t;
	getline(fin,t);
	//cout << T;
	for(int i=0;i != T ;++i)
	{
		string in;
		getline(fin,in);
		cout << in << endl;
		string out;
		transform(in.begin(),in.end(), back_inserter(out),translate);
		fout << "Case #"<< i+1 << ": " << out << endl;
		//cout << out << endl;
	}
	fout.close();
	fin.close();

}
