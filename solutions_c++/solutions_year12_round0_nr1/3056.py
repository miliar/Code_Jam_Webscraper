#include <iostream>
#include <fstream>
#include <map>

using namespace std;

map<char, char> initialize_mapping() {
	string s1 = "y qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv z";
	string s2 = "a zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up q";

	map<char, char> result;
	for(size_t i = 0; i < s1.length(); i++){
		if(result.find(s1[i]) == result.end())
			result.insert(make_pair(s1[i], s2[i]));
	}

	return result;
}

int main(int argc, char** argv) {
	map<char, char> mapping = initialize_mapping();

	ifstream in("input.txt");
	size_t T;
	in>>T;
	in.get();

	ofstream out("out.txt");
	for(size_t i = 0; i < T; i++) {
		string G;
		getline(in, G);

		out<<"Case #"<<(i+1)<<": ";

		for(size_t c = 0; c < G.length(); c++) {
			if(mapping.find(G[c]) != mapping.end())
				out<<mapping.at(G[c]);
			else
				cout<<"ERROR: "<<G[c]<<" not mapped!"<<endl;
		}

		out<<endl;
	}

	in.close();
	out.close();

	return 0;
}
