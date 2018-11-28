// H.Marihot
// Google Code Jam 2012
// Qualification Round
// 13th April 2012
// Problem C

#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <sstream>
#include <set>

using namespace std;

string shiftRight(string str)
{
	unsigned short strLen;
	strLen = str.length();
	str.insert(0,1,str[strLen-1]);
	return str.substr(0,strLen);
}

unsigned long stringToInt(string str)
{
	unsigned long value;
	return atoi(str.c_str());
}
string intToString(unsigned long value)
{
	stringstream ss;
	ss << value;
	return ss.str();
}

unsigned short numOfRecycledNumber(unsigned long value, unsigned long min, unsigned long max)
{
	unsigned short strLen;
	unsigned long valueInt, shiftedValueInt;
	set<unsigned long> mSet;
	string valueStr, shiftedValueStr;
	unsigned shiftedValue;
	valueStr = intToString(value);
	strLen = valueStr.length();
	shiftedValueStr = valueStr;
	for (unsigned short i = 0; i < strLen-1; i++)
	{
		shiftedValueStr = shiftRight(shiftedValueStr);
		valueInt = stringToInt(valueStr);
		shiftedValueInt = stringToInt(shiftedValueStr);
		if ((shiftedValueInt > valueInt) && (valueInt >= min) && (shiftedValueInt <= max))
		{
			mSet.insert(shiftedValueInt);
		}
	}
	return mSet.size();
}

int main()
{
	unsigned short T, output;
	unsigned long min, max;
	cin >> T;
	for (unsigned short i; i < T; i++)
	{
		output = 0;
		cin >> min; // minimum value
		cin >> max; // maximum value
		for(unsigned long value = min; value <= max; value++)
		{
			output += numOfRecycledNumber(value, min, max);
		}
		cout << "Case #" << i + 1 << ": " << output << endl;
	}
	return 0;
}
