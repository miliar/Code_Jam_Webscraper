/*
 * main.cc
 *
 *  Created on: May 7, 2010
 *      Author: elden
 */

#include <iostream>
#include <fstream>
#include <deque>
using namespace std;


int main()
{
	ifstream inFile("C-small.in");
	ofstream outFile("C-small.out");
	int T;
	inFile >> T;
	for (int i=0;i<T;i++) {
		// read each test case
        int R,k,N;
		inFile >> R >> k >> N;
		deque<int> waitList;
        for (int j=0;j<N;j++) {
        	int gj;
        	inFile >> gj;
        	waitList.push_back(gj);
        }

        // start roller coaster
        long count = 0;
        for (int j=0;j<R;j++) {
        	int countRound = 0;
        	deque<int>::iterator it1=waitList.begin();
        	deque<int>::iterator it2=waitList.end();
        	for (;it1!=it2;it1++) {
        		if (countRound + (*it1) <= k) {
        			countRound += *it1;
        			waitList.push_back(*it1);
        		} else
        			break;
        	}
        	for (deque<int>::iterator it3=waitList.begin();it3!=it1;it3++)
        		waitList.erase(it3);
//        	waitList.erase(waitList.begin(),it1);
        	count += countRound;
        }
		outFile << "Case #" << i+1 <<": " << count <<endl;
	}
	return 0;
}
