#include <iostream>
#include <string>
#include <fstream>
using namespace std;

char replace(char x) {
	char rs;
	switch (x) {
		case 'a': rs = 'y'; break;
		case 'b': rs = 'h'; break;
		case 'c': rs = 'e'; break;
		case 'd': rs = 's'; break;
		case 'e': rs = 'o'; break;
		case 'f': rs = 'c'; break;
		case 'g': rs = 'v'; break;
		case 'h': rs = 'x'; break;
		case 'i': rs = 'd'; break;
		case 'j': rs = 'u'; break;
		case 'k': rs = 'i'; break;
		case 'l': rs = 'g'; break;
		case 'm': rs = 'l'; break;
		case 'n': rs = 'b'; break;
		case 'o': rs = 'k'; break;
		case 'p': rs = 'r'; break;
		case 'q': rs = 'z'; break;
		case 'r': rs = 't'; break;
		case 's': rs = 'n'; break;
		case 't': rs = 'w'; break;
		case 'u': rs = 'j'; break;
		case 'v': rs = 'p'; break;
		case 'w': rs = 'f'; break;
		case 'x': rs = 'm'; break;
		case 'y': rs = 'a'; break;
		case 'z': rs = 'q'; break;
	}
	return rs;
}

int main() {
	//int cases;
	//char x;
	//string s;
	//cin>>cases;
	//getchar();
	//for(int i = cases; i!=0; --i) {
	//	getline(cin,s);
	//	int j = 0;
	//	cout<<"Case #"<<cases-i+1<<": ";
	//	while(j != s.length() ){
	//		if(s[j]>=97 && s[j]<=122) {
	//			cout<<replace(s[j++]);
	//		}
	//		else cout<<s[j++];
	//	}
	//	cout<<endl;
	//}
	//return 0;


	ifstream fin("./A-small-attempt1.in");
	ofstream fout("./output.out");
	if(!fin) {
		cerr<<"文件input打开失败"<<endl;
		return -1;
	}
	if(!fout) {
		cerr<<"文件output打开失败"<<endl;
		return -1;
	}

	int cases;
	string s;
	fin>>cases;
	getline(fin,s);
	for(int i = cases; i!=0; --i) {
		getline(fin,s);
		int j = 0;
		fout<<"Case #"<<cases-i+1<<": ";
		while(j != s.length() ){
			if(s[j]>=97 && s[j]<=122) {
				fout<<replace(s[j++]);
			}
			else fout<<s[j++];
		}
		fout<<endl;
	}
}