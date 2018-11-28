/*
 * calyNum.h
 *
 *  Created on: 2010-5-8
 *      Author: xhd
 */

#ifndef CALYNUM_H_
#define CALYNUM_H_

#include <vector>

namespace std {

class calyNum {
public:
	calyNum();
	virtual ~calyNum();

	int gcd(int a, int b);
	int gcd(vector<int>& differenceVector);
	int run(vector<int>& tVec);

private:
	vector<int> diffVec;
};

}

#endif /* CALYNUM_H_ */
