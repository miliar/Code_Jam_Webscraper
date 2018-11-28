#include <iostream>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;

void process(int A,int B, int& counter)
{
	vector<string> intBtwA_B;
	string buf;
	for(int j = A; j <= B; j++){
		ostringstream ostr;
		ostr << j;
		istringstream str (ostr.str(),istringstream::in);
		str >> buf;		
		intBtwA_B.push_back(buf);
	}
	
	for(size_t j = 0; j < intBtwA_B.size(); j++){
		string n = intBtwA_B.at(j);
		for(size_t i = j+1; i < intBtwA_B.size(); ++i){
			string m = intBtwA_B.at(i);
			//cout << "--------------\n( " << n << "," << m << ")\n";
			string nprocess = n;
			size_t n_len = n.size();
			for(size_t k = 1 ; k < n_len; ++k){
				string end = n.substr(n_len-k,k);
				//cout << " end =" << end << endl;
				nprocess = n.substr(0,n_len - k);
				//cout << " nprocess =" << nprocess << endl;
				nprocess = end + nprocess;
				//cout << nprocess << " == " << m << " : " << (nprocess == m ) << endl;
				if(nprocess == m ){
					counter++;
					//cout << "counter =" << counter << endl;
				}
			}
		}
	}
}

int main(int argc, char** argv)
{
	if(argc < 2){
		cerr  << "\nargument missing.\n"
				<< "\tUsage : "<< argv[0] << " <<inputFile>>\n\n";
	
		exit(-1);
	}
	
	ifstream infile(argv[1],ifstream::in);
	ofstream ofile("output.in", ofstream::out);
	
	if(!infile || !ofile){
		cerr << "Can't open files\n";
		exit(-1);
	}
	int nbCase,A, B;
	string line;
	
	getline(infile,line);
	istringstream str(line);
	str >> nbCase;
	cout << nbCase << endl;
	for(int i = 1; i <= nbCase; ++i){
		getline(infile,line);
		istringstream str1(line);
		//cout << line << endl;
		str1 >> A >> B;
		//cout << "("<< A <<","<< B << ")\n";
		int counter = 0;
		process(A,B,counter);
		ofile << "Case #" << i << ": " << counter << endl;
	}
	infile.close();
	ofile.close();
	
	return 0;
}