
#include <stdio.h>
#include <iostream>
#include <vector>
#include <list>


using namespace std;

class testcase {
	public :

		testcase();

		~testcase();

	public :
		int evaluate();
		void addOneVal(int val);
		void addSecondVal(int val);

	public :
		list<int> firstList_;
		list<int> secondList_;

};


class testnumber {
	public :
		testnumber(int num);

		testnumber();
};


