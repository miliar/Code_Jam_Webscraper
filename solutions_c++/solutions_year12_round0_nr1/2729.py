#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main() {

	int t;
	char a[26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char b[26]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d',
					'r','j','g','t','h','a','q'};
	string line;
	string word;
	ifstream in("input.in");
	ofstream out("output.txt");
	in >> t;
	getline(in, line);
	for (int i = 1; i <= t; i++) {
		getline(in, line);
		istringstream iss(line);
		out<<"Case #"<<i<<": ";
		while (!iss.eof()) {
			iss >> word;
			for(unsigned int j=0;j<word.length();j++){
				for(int k=0;k<26;k++){
					if(word[j]==b[k]){
						word[j]=a[k];
						break;
					}
				}
			}
			out<<word<<' ';
		}
		 out<<endl;
	}
}
