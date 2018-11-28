#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<fstream>

using namespace std;


int main(){
	string translated[3]={"ejp mysljylc kd kxveddknmc re jsicpdrysi",
						  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
						  "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string original[3]=  {"our language is impossible to understand",
						  "there are twenty six factorial possibilities",
						  "so it is okay if you want to just give up"};
	char map[256],invmap[256];
	for(int i=0;i<3;++i){
		for(int j=0;j<translated[i].size();++j){
			map[translated[i][j]]=original[i][j];
			invmap[original[i][j]]=translated[i][j];
		}
	}
	map['e']='o';
	map['q']='z';
	map['y']='a';
	map['z']='q';
	map[' ']=' ';
	ifstream in;
	ofstream out;
	in.open("A-small.txt");
	out.open("A-small_out.txt");
	int T;

	string str;
	getline(in,str);
	stringstream ss;
	ss<<str;
	ss>>T;	
	//cin>>T;
	for(int C=1;C<=T;++C){
		string line;
		getline(in,line);
		for(int i=0;i<line.size();++i)
			line[i]=map[line[i]];
		out<<"Case #"<<C<<": "<<line<<endl;
	}
	in.close();
	out.close();
	return 0;
}