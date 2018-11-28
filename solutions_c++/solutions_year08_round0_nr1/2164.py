#include<iostream>
#include<iomanip>
#include<fstream>
#include<string>
#include <vector>

using namespace std;

//input and output files
ofstream outfile("outp.out");//output file
std::ifstream infile("A-large.in");//input file 

/*
struct path
{
    string engine;        // a word
    string docName;     // a document it appears in
    path(string w, string dn)
     : engine(w), docName(dn)
    {}
};*/

int main()
{
	
	//infile>>num_cases;
	string n;
	std::getline(infile, n);
	int num_cases = atoi(n.data());
	//cout<<num_cases<<endl;
	for(int i = 1; i <= num_cases; i++){
		int q,s;
		int switches = 0;
		
		//get search engines
		string en;
		std::getline(infile, en);
		q = atoi(en.data());
		//cout << q <<endl;
		if (q == 0)
			return 0;
		vector <string> engines;
		int eng[101];
		for (int j = 0; j < q; j++){
			std::string buffer;
			//infile>>buffer;
			std::getline(infile, buffer);
			//cout<<buffer<<endl;
			engines.push_back(buffer);
			eng[j] = 0;
		}
		//get search terms
		//infile>>s;
		std::getline(infile, en);
		s = atoi(en.data());
		//cout<<s<<endl;
		int current = 0;//current engine
		int used = 0; //store the engines used
		for (int j = 0; j < s; j++){//for each query
			int test;			
			string buffer;
			std::getline(infile, buffer);
			for (int k = 0; k < q; k++){
				if (eng[k] == 0){
					//cout<<"buffer "<<buffer<<" and se "<<engines.at(k)<<endl;
					if ( buffer == engines.at(k) ){ //engine matches
						eng[k] = 1;
						used++;
						//cout<<"matches"<<endl;
						if (used >= q){
							switches++;
							//current = k;
							for (int l = 0; l < q; l++){
								eng[l] = 0;
							}
							eng[k] = 1;
							used = 1;
							break;
						}
					}
				}
			}
		}
		//process
		outfile<<"Case #"<<i<<": ";
		outfile<<switches<<endl;
	}
}