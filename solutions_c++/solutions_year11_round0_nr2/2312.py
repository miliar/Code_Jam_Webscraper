
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <map>

using namespace std;
int main (int argc, char * const argv[]) {
    
	ifstream input(argv[1], ifstream::in);
	
	int testsNb;
	string s;
	getline(input, s);
	istringstream stream(s);
	stream >> testsNb;
	
	ofstream outfile(argv[2]);
	
	cout << "Testing " << testsNb << " cases..." << endl;
	
	int cases = 0;
	while (input.good() && getline(input, s) && !input.eof()) {
		char *tmp = strdup(s.c_str());
		const char *token = strtok(tmp, " ");
		int combined, opposed, invok;
		map<pair<char, char>, char> combined_pairs;
		map<pair<char, char>, char>::iterator it;
		vector<pair<char, char> > opposed_pairs;
		string invocation_string;
		list<char> final_list;
		list<char>::iterator it_list;
		while (token != NULL) {
			// Read combined strings
			combined = atoi(token);
			//cout << combined << endl;
			int count = 0;
			while (count < combined) {
				token = strtok(NULL, " ");
				combined_pairs[make_pair(token[0], token[1])] = token[2];
				//for (it = combined_pairs.begin(); it != combined_pairs.end(); it++)
					//cout << "[" << (*it).first.first << "," << (*it).first.second << "] -> " << (*it).second << endl;
				count++;
			}
			
			// Read opposed strings
			token = strtok(NULL, " ");
			opposed = atoi(token);
			//cout << opposed << endl;
			count = 0;
			while (count < opposed) {
				token = strtok(NULL, " ");
				opposed_pairs.push_back(make_pair(token[0], token[1]));
				//for (int i = 0; i < opposed_pairs.size(); i++)
					//cout << "[" << opposed_pairs[i].first << "," << opposed_pairs[i].second << "]" << endl;
				count++;
			}

			
			// Read invok sequence
			token = strtok(NULL, " ");
			invok = atoi(token);
			//cout << invok << endl;
			// Read invocation string
			token = strtok(NULL, " ");
			invocation_string = string(token);
			//cout << invocation_string << endl;
			token = strtok(NULL, " ");
			
			
			
		
		}
		free(tmp);
		cases++;
		
		// Calculate
		for (int i = 0; i < invocation_string.length(); i++) {
			char current = invocation_string[i];
			// Add element if empty and continue
			if (final_list.empty()) {
				//cout << "Adding " << current << endl;
				final_list.push_back(current);
				continue;
			}
			// Combined?
			if (combined_pairs.end() != (it = combined_pairs.find(make_pair(current, final_list.back()))) ||
				combined_pairs.end() != (it = combined_pairs.find(make_pair(final_list.back(), current)))) {
				//cout << "Found combined pair [" << (*it).first.first << "," << (*it).first.second << "]" << endl;
				final_list.pop_back();
				final_list.push_back(it->second);
				continue;
			}
			// Opposed?
			else {
				bool clear = false;
				for (it_list = final_list.begin(); it_list != final_list.end() && !clear; it_list++) {
					vector<pair<char, char> >::iterator it2;
					//cout << "Looking for " << *it_list << " and " << current << endl;
					// Clear list if occurrence is found
					if (opposed_pairs.end() != (it2 = find(opposed_pairs.begin(), opposed_pairs.end(), make_pair(*it_list, current))) ||
						opposed_pairs.end() != (it2 = find(opposed_pairs.begin(), opposed_pairs.end(), make_pair(current, *it_list)))) {
						//cout << "Found " << *it_list << " and " << current << endl;
						clear = true;
						continue;
					}
				}
				if (clear) {
					final_list.clear();
					continue;
				}
			}
			 
			final_list.push_back(current);
			
		}
		// Output results
		outfile << "Case #" << cases << ": [";
		int tt = final_list.size() - 1;
		for (it_list = final_list.begin(); it_list != final_list.end(); it_list++, tt--) {
			outfile << *it_list;
			if (tt > 0)
				outfile << ", ";
		}
		outfile << "]" << endl;
	}	
	
	input.close();
	outfile.close();
    return 0;
	
}
