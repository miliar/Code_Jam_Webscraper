
#ifndef TESTCASE_H_INCLUDED
#define TESTCASE_H_INCLUDED

#include <string>
#include <iostream>

using namespace std;
class TestCase {
    public:
        TestCase() {};
        TestCase(string en[], string qu[], int x, int y);
        void save(ostream& output, int result[], int n);
        void load(istream & file, int n, TestCase result[]);
        string engines[100];
        int nEngines;
        string queries[1000];
        int nQueries;
};


#endif // TESTCASE_H_INCLUDED
