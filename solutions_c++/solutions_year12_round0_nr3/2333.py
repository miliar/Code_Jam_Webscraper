#include <iostream>
#include <fstream>
#include <sstream>
#include <list>
#include <vector>

using namespace std;

int main(){
	ifstream infile("/home/hawkwing/Desktop/C-large.in");
	int cases;
	infile >> cases;
	int A[cases];
	int B[cases];
	for(unsigned int i=0;i<cases;i++){
		infile >> A[i] >> B[i];
	}
	infile.close();
	
	ofstream outfile("/home/hawkwing/Desktop/Problem 3-output-large");
	stringstream ss;
	string n_s;
	int m;
	list<string> nm;
	for(unsigned int i=0;i<cases;i++){
		nm.clear();
		for(unsigned int n=A[i];n<=B[i];n++){
			ss << n;
			n_s=ss.str();
			ss.str("");
			for(unsigned int k=1;k<n_s.length();k++){
				if(n_s[k]!='0'){
					ss << n_s.substr(k,n_s.length()) << n_s.substr(0,k);
					stringstream(ss.str()) >> m;
					if(n<m and m<=B[i]){
						stringstream nm_ss;
						nm_ss << n_s << ", " << m;
						nm.push_back(nm_ss.str());
					}
					ss.str("");
				}
			}
		}
		nm.sort();
		nm.unique();
		outfile << "Case #" << i+1 << ": " << nm.size();
		if(i<cases-1){
			outfile << endl;
		}
	}
	outfile.close();
	
	return 0;
}