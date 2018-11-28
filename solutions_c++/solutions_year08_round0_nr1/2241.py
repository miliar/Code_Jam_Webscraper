#include <iostream>
#include <fstream>
#include <string.h>
#include <vector>
#include <algorithm>
std::ofstream outputfile;
std::ifstream inputfile;
using std::string;
using std::endl;
using std::cout;
using std::vector;
using std::find;
char temp[1024] = "";
int calculate(vector<string>, vector<string>);
int main(int, char**){
	vector<string> engines;
	vector<string> queries;
	outputfile.open("C:/GCJ/Qualification/test.out");
	inputfile.open("C:/GCJ/Qualification/test.in");
	int N;
	(inputfile >> N).ignore();
	for(int i = 0; i < N; ++i) {
		int S;
		int Q;
		(inputfile >> S).ignore();
		for(int j = 0; j < S; ++j){
			inputfile.getline(temp,1024,'\n');
			engines.push_back(temp);
		}
		(inputfile >> Q).ignore();
		for(int j = 0; j < Q; ++j){
			inputfile.getline(temp,1024,'\n');
			queries.push_back(temp);
		}
		outputfile << "Case #" << i + 1 << ": " << calculate(engines, queries) << "\n";
		engines.clear();
		queries.clear();
	}
	outputfile.close();
	inputfile.close();
}
int calculate(vector<string> e, vector<string> q) {
	int result = 0;
	vector<string> e_original = e;
	string curr;
	while(q.empty() != true){
		e = e_original;
		while (q.empty() != true) {
			curr = *q.begin();
			vector<string>::iterator location;
			for(location = e.begin(); location != e.end(); ++location) {
				if(strcmp(location->c_str(),q.begin()->c_str()) == 0) break;
			}
			if(location != e.end()) {
				e.erase(location);
				if(e.empty() == true){
					++result;
					e = e_original;
					for(location = e.begin(); location != e.end(); ++location) {
						if(strcmp(location->c_str(),q.begin()->c_str()) == 0) break;
					}
					e.erase(location);
					q.erase(q.begin());
					/*if(q.empty()!=true) continue;
					else break;*/
					continue;
				}
			}
			q.erase(q.begin());
		}
	}
	return result;
}