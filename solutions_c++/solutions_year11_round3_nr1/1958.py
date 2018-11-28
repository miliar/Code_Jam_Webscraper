//============================================================================
// Name        : CodeJam_Round1.cpp
// Author      : Gerry
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "io_handler.h"
using namespace std;

int main() {
	io_handler *iohdlr = new io_handler();

	//read input and process
	iohdlr->read_input_file("A-small-practice.txt");

	return 0;
}
