#include <iostream>
#include <fstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

int main(){
	int T;
	ifstream infile("c.in");
	ofstream outfile("c.out");
	ifstream strfile("str.txt");
	vector<string> p;
	int n;

	infile>>T;
	string temp;
	for (int i=2;i<=30;i++){
		strfile>>temp;
		if (temp.length()==2) temp="0"+temp;
		p.push_back(temp);
	}
	for (int i=1;i<=T;i++){
		infile>>n;
		outfile<<"Case #"<<i<<": "<<p.at(n-2)<<endl;
	}
}