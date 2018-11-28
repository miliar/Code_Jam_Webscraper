// g++-mp-4.6 -I /opt/local/include -Wall -std=gnu++0x
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <utility>
#include <algorithm>

#include <boost/algorithm/string.hpp>
#include <boost/lambda/lambda.hpp>

using namespace std;
using namespace boost;
using namespace boost::lambda;

int main (int argc, char * const argv[]) {
	ifstream fin(argv[1]);
	unsigned long T;
	fin >> T;
	
	for(unsigned long i = 0; i != T; ++i) {
		unsigned long N;
		fin >> N;
		
		vector<pair <unsigned long,unsigned long> > wires;
		for(unsigned long j = 0; j != N; ++j){
			unsigned long A,B;
			fin >> A >> B;
			wires.push_back(pair <unsigned long,unsigned long> (A,B));
		}
		
		unsigned long pairs= 0;
		for (unsigned long j = 0; j != wires.size(); ++j) {
			for (unsigned long k = 0; k != j; ++k) {
				if ((wires[j].first > wires[k].first && wires[j].second < wires[k].second)
					|| (wires[j].first < wires[k].first && wires[j].second > wires[k].second)) {
					++pairs;
				}
			}
		}
	
		
		
		
		cout << "Case #"<< i+1 << ": " << pairs << endl;
	}

	
	
	return 0;
}