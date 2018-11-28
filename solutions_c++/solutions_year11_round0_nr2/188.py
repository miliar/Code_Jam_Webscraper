#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main(int argc, char * argv[]) {
	if ( argc < 2)
		cout <<"Enter input";
	
	ifstream input(argv[1]);
	int problem_count ;
	input >> problem_count;

	for (int p = 1; p <= problem_count; p++) {
		vector<char> pool;

		map<string, char> combine;
		multimap< char, char > opposed;

		int c ;
		input >> c;
		for (int i = 0; i < c; i++) {
			char c1, c2, b;
			input >> c1 >> c2 >> b;
			string ss;
			ss += c1;
			ss += c2;
			combine[ss] = b;
			ss.clear();
			ss += c2;
			ss += c1;
			combine[ss] = b;
		}

		input >> c;
		for (int i = 0; i < c; i++) {
			char o1, o2;
			input >> o1 >> o2;
			opposed.insert(pair<char, char>(o1, o2));
			opposed.insert(pair<char, char>(o2, o1));
		}


		input >> c;
		for( int k = 0; k < c; k++) {
			char element;
			input >> element;
			if (pool.empty()) {
				pool.push_back(element);
				continue;
			}
			

			char pre = pool.back();
			string ss ;
			ss += pre;
			ss += element;
			if( combine.count(ss) > 0){
				pool[pool.size()-1] = combine[ss];
				continue;
			}
			
			ss.clear();
			ss += element;
			ss += pre;
			if( combine.count(ss) > 0){
				pool[pool.size()-1] = combine[ss];
				continue;
			}


			pair<multimap<char,char>::iterator,multimap<char,char>::iterator> ret;
			ret = opposed.equal_range(element);
			bool clean = false;
			for (multimap<char,char>::iterator it = ret.first; it != ret.second; it++){
				for (vector<char>::iterator pool_it = pool.begin(); pool_it != pool.end(); pool_it++)
					if( *pool_it == it->second ) {
						clean = true;
						break;
					}
				if (clean) {
					pool.clear();
					break;
				}
			}

			if (!clean)
				pool.push_back(element);

		}
		cout <<"Case #" << p << ": ";
		cout <<"[";
		for ( vector<char>::iterator it = pool.begin(); it !=pool.end(); it++) {
			cout << *it;
			if(it+1 != pool.end()) 
				cout <<", ";
		}
		cout <<"]\n";

	}

	input.close();
	return 0;

}


