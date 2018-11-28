
#include <iostream>
#include <fstream>
#include <set>
using std::cin;
using std::cout;
using std::set;
using std::pair;
using std::endl;
using std::fstream;

#define MAX_NAME_LEN 101

struct eqstr
{
  bool operator()(const char* s1, const char* s2) const
  {
    return strcmp(s1, s2) < 0;
  }
};

class SE_Man {
	unsigned int num_switches;
	unsigned int num_engines;
	unsigned int num_visited;
	set<char*, eqstr> engines;
	SE_Man(); //private constructor
	void clear() {
		for each (char* buf in engines) {
			delete[] buf;
		}
		engines.clear();
	}
public:
	SE_Man(unsigned int qty) {
		num_switches = 0;
		num_engines = qty;
		num_visited = 0;
		//cout << "num engines: " << num_engines << endl;
	}
	~SE_Man() {
		clear();
	}
	void visitSE(char* name) {
		char* str = strdup(name);
		pair<set<char*, eqstr>::iterator, bool> insert_ret = engines.insert(str);
		if (insert_ret.second) {
			num_visited++;
			//cout << "inserting " << str << endl;
		} else {
			delete[] str;
		}
		if (num_visited == num_engines) {
			num_switches++;
			//cout << "switching engine " << num_switches << endl;
			clear();
			str = strdup(name);
			engines.insert(str);
			num_visited = 1;
		}
	}
	unsigned int getNumSwitches() { return num_switches; }
};

void main(unsigned int argc, char** argv) {
	//if (argc != 2) {
	//	printf("usage: <appname> <inputfile>\n");
	//}
	//char* filename = argv[1];
	//read input, of form:
	/*
Input

The first line of the input file contains the number of cases, N. N test cases follow.
Each case starts with the number S -- the number of search engines. The next S lines each contain the name of a search engine. Each search engine name is no more than one hundred characters long and contains only uppercase letters, lowercase letters, spaces, and numbers. There will not be two search engines with the same name.
The following line contains a number Q -- the number of incoming queries. The next Q lines will each contain a query. Each query will be the name of a search engine in the case. 

N
S
name1
name2
nameS
T
name1
nameT
*/
	unsigned int num_cases = 0;
	//fstream fin(filename, std::ios_base::in);
	cin >> num_cases;
	//cout << num_cases << endl;
	for (unsigned int case_num = 0; case_num < num_cases; case_num++) {
		unsigned int num_engines = 0;
		unsigned int num_switches = 0;
		cin >> num_engines;
		//cout << num_engines << endl;
		//char** engine_name = new char*[num_engines];
		char buf[MAX_NAME_LEN];
		cin.getline(buf, MAX_NAME_LEN);
		for (unsigned int engine_num = 0; engine_num < num_engines; engine_num++) {
			cin.getline(buf, MAX_NAME_LEN);
			//cout << buf << endl;
			//engine_name[engine_num] = new char[MAX_NAME_LEN];
			//cin.getline(engine_name[engine_num], MAX_NAME_LEN);
		}
		//solve this problem here...
		unsigned int num_searches = 0;
		cin >> num_searches;
		//cout << num_searches << endl;
		SE_Man seman(num_engines);
		cin.getline(buf, MAX_NAME_LEN);
		for (unsigned int search_num = 0; search_num < num_searches; search_num++) {
			cin.getline(buf, MAX_NAME_LEN);
			//cout << buf << endl;
			seman.visitSE(buf);
		}
		//print output
		cout <<"Case #" << case_num+1 << ": " << seman.getNumSwitches() << endl;
	}
	int bob;
	//cin >> bob;	
	//cout << bob << endl;
}