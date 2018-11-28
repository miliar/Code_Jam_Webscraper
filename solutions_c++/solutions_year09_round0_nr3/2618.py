/*
 * Input.h
 *
 *  Created on: 2009/09/03
 *      Author: minami
 */

#ifndef INPUT_H_
#define INPUT_H_

#include <iostream>
#include <fstream>

class Input
{
public:
	Input();
	~Input();

	bool open(const std::string& path);

	long count_cases() const;
	const std::string get_next_case() const;

private:
	long count;
	mutable std::ifstream in;
};

#endif /* INPUT_H_ */
