// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <stdlib.h>
#include <string.h>

using namespace std;

string Calc()
{
	int num, val, min = -1;
	cin >> num;
	int xor = 0, totalVal = 0;
	for(int i = 0; i < num; i++)
	{
		cin >> val;
		xor ^= val;
		totalVal += val;
		if(min == -1)
			min = val;
		else
			min = val < min ? val : min;
	}
	if(xor != 0)
		return "NO";
	else
	{
		char buf[33];
		sprintf(buf,"%d", totalVal - min);
		return buf;
	}
}
int main(int argc, char* argv[])
{
	int cases;
	cin >> cases;
	for(int i =0 ; i < cases; i++)
	{
		string ans = Calc();
		cout << "Case #" << i+1<< ": " << ans.c_str() << endl;
	}
}

