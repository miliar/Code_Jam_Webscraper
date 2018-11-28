#ifndef GORO_H
#define GORO_H

#include <fstream>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>

using namespace std;

class goro
{
public:
	double prob( double, int);
	double hits( int);
	int fact( int);
	void permute( int N, vector<vector<int> >* perms, vector<int> s);
};

#endif