//google jam 3
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <list>

using namespace std;

string convertInt(int number){
	stringstream ss;
	ss << number;
	return ss.str();
}

int convertString(string s){
	int value;
	istringstream(s) >> value;
	return value;
}

int main(){
	ifstream input("C-small-attempt0.in");
	ofstream output("output.txt");

	int T;
	input >> T;
	
	for (unsigned int i=0;i<T;i++){
		int flag=0;
		int A,B,n;
		input >> A >> B;
		for (unsigned int j=A;j<B;j++){
			n=j;
			string SN=convertInt(n);
			list <int> exist;			
			for (unsigned int k=1;k<SN.length();k++){
				string SM="";
				for (unsigned int l=k;l<SN.length();l++){
					SM+=SN[l];
				}
				for (unsigned int l=0;l<k;l++){
					SM+=SN[l];
				}
				int m=convertString(SM);
				if (m<=B && n<m && find(exist.begin(),exist.end(),m)==exist.end()) {
					flag++;
				}
				exist.push_back(m);
			}
		}
		output << "Case #"<<i+1<<": " << flag << endl; 
	}
	return 0;
}
