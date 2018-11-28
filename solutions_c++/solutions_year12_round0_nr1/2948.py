#include <iostream>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <string>

using namespace std;
string translate(string googlerese,string english, string line)
{
	string lineTrans;
	for(size_t i = 0; i < line.size(); ++i){
		size_t pos = googlerese.find(line[i]);
		if(pos != -1){
			lineTrans.push_back(english[pos]);
		}
	}
	return lineTrans;
}
int main(int argc, char** argv)
{
	if(argc < 2){
		cerr  << "\nargument missing.\n"
				<< "\tUsage : "<< argv[0] << " <<inputFile>>\n\n";
	
		exit(-1);
	}
	string googlerese("abcdefghijklmnopqrstuvwxyz ");
	string    english("yhesocvxduiglbkrztnwjpfmaq ");
	ifstream infile(argv[1],ifstream::in);
	ofstream ofile("output.in", ofstream::out);
	
	if(!infile || !ofile){
		cerr << "Can't open files\n";
		exit(-1);
	}
	int nbCase;
	string line;
	
	getline(infile,line);
	istringstream str(line);
	str >> nbCase;
	cout << nbCase << endl;
	for(int i = 1; i <= nbCase; ++i){
		getline(infile,line);
		ofile << "Case #" << i << ": "<< translate(googlerese,english,line) << endl;
	}
	infile.close();
	ofile.close();
	
	return 0;
}