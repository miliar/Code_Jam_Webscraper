/*
 * ql_1a.h
 *
 *  Created on: May 21, 2010
 *      Author: root
 */

#ifndef QL_1A_H_
#define QL_1A_H_

#include <string>

using namespace std;

class ql_1a {
public:
	typedef struct _node{
		string name;
		struct _node *adj;
		struct _node *next;
	}NODE;


	ql_1a();
	~ql_1a();

	void quiz1();
	void quiz2();
	void quiz3();

	void quizb1();
	void quizb2();
	void quizb3();
};

#endif /* QL_1A_H_ */
