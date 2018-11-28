#include <string>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <sstream>

using namespace std;

int main(){
	ifstream ifile;
	ofstream ofile;
	string templine;
	string templine2="";
	ifile.open("input");
	ofile.open("output");
	getline(ifile,templine);
	int t = atoi(templine.c_str());
	for(int i=0;i<t;++i){
		getline(ifile,templine);
		istringstream iss(templine);
		string v;
		int count = 0;
		int N,S,p,tot,surp,tot_count,surp_count;
		while(iss >> v){
			switch(count){
				case 0: N = atoi(v.c_str()); tot_count=0;surp_count=0; break;
				case 1: S = atoi(v.c_str()); break;
				case 2: p = 
						atoi(v.c_str());
						tot=3*p-2;
						surp=3*p-4;
						break;
				default: 
						int current = atoi(v.c_str());
						if(current >= tot && current >= p){
							tot_count++;
							cout << "tot increased for: " << current << endl;
						}
						if(current >= surp && current >= p){
							surp_count++;
						}
			}
			count++;
		}
		cout << "tot: " << tot<< endl;
		cout << "tot_count: " << tot_count<< endl;
		cout << "surp: " << surp<< endl;
		cout << "surp_count: " << surp_count<< endl;
		cout << "N: " <<N << endl;
		cout << "S: " <<S << endl;
		cout << "p: " <<p << endl;
		cout << "Case #" << i+1 << ": " << tot_count + min(surp_count-tot_count,S) << endl;
		cout << "\n\n" << endl;
		ofile << "Case #" << i+1 << ": " << tot_count + min(surp_count-tot_count,S) << endl;
	}
	return 0;
}

