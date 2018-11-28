#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <sstream>

using namespace std;

unsigned solveQ1()
{
	unsigned numServers;
	cin >> numServers;
	map<string, unsigned> servers;
	
	cin.ignore();
	string s;
	for(unsigned i = 0; i < numServers; ++i) {
		getline(cin, s);
		servers[s] = i;
	}
	
	vector<bool> seen = vector<bool>(numServers, false);
	
	unsigned sequenceLength;
	cin >> sequenceLength;
	vector<unsigned> sequence;
	sequence.reserve(sequenceLength);
	
	cin.ignore();
	for(unsigned i = 0; i < sequenceLength; ++i) {
		getline(cin, s);
		sequence.push_back(servers[s]);
	}
	unsigned switches = 0;
	unsigned unseen = numServers;
	for(unsigned i = 0; i < sequenceLength; ++i) {
		if(!seen.at(sequence.at(i))) {
			seen[sequence.at(i)] = true;
			--unseen;
			if(unseen == 0) {
				seen = vector<bool>(numServers, false);
				seen[sequence.at(i)] = true;
				unseen = numServers-1;
				switches++;
			}
		}
	}
	return switches;
}

int main()
{
	unsigned iterations;
	cin >> iterations;
	
	for(unsigned i = 0; i < iterations; ++i)
		cout << "Case #" << i+1 << ": " << solveQ1() << endl;
}
