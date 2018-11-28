#ifndef TEST_CASE_H
#define TEST_CASE_H

#include <fstream>
#include <string>
#include <vector>
using namespace std;


class test_case{
public:
	int turnround_time;
	int na;
	int nb;
	vector<int>* departa, *departb, *arrivea, *arriveb;

	test_case(ifstream& fin);
	int str2int(string str);
	void insert_tripA(string str);
	void insert_tripB(string str);
	void insert_vector(vector<int>* v, int data);
	void print_vector(vector<int>* v);
	int necessary_a();
	int necessary_b();
};


#endif