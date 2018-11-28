/*
 * calMoney.h
 *
 *  Created on: 2010-5-7
 *      Author: xhd
 */

#ifndef CALMONEY_H_
#define CALMONEY_H_

#include <vector>

namespace std {

class calMoney {
public:
	calMoney(int rr, int kk, vector<int>& NGrpNumVec);
	virtual ~calMoney();

	int run();
	int step(int startPos, int& totalSum);

	vector<int> grpNumVec;
	int R;
	int k;
};

}

#endif /* CALMONEY_H_ */
