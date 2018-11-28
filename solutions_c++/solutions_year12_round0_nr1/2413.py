#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream in;
	ofstream out;

	in.open("in.txt");
	out.open("out.txt");

	int T;

	in >> T;

	char map2[]={
		'y','n','f','i','c',
		'w','l','b','k','u',
		'o','m','x','s','e',
		'v','e','p','d','r',
		'j','g','t','h','a','q'
	};

	char map[]={
		'y','n','f','i','c',
		'w','l','b','k','u',
		'o','m','x','s','e',
		'v','e','p','d','r',
		'j','g','t','h','a','q'
	};

	for(int i=0;i<26;i++){
		map[map2[i]-'a']='a'+i;
	}
	map['e'-'a']='o';

		char c[10000];
		in.getline(c,9000);
	for (int i=0;i<T;i++){
		out << "Case #" << i+1 << ": ";
		in.getline(c,9000);
		for(int j=0;;j++){
			if (!c[j]) break;

			if (c[j]>='a' && c[j]<='z') {
				out <<map[c[j]-'a'];
			} else {
				out <<c[j];
			}
		}
		out<<endl;
	}
}
