#ifndef TEST_CASE_H
#define TEST_CASE_H

#include <string>
#include <fstream>
using namespace std;

class test_case{
public:
	int engine_num;
	int query_num;
	string* engines;
	string* queries;

	test_case(ifstream& fin);
	void print_test_case();
	int min_switch(string* p, int size);
	int query_map(string name);
};


#endif