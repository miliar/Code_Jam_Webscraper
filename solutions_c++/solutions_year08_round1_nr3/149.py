// program.cpp : Defines the entry point for the console application.
//

// BEGIN CUT HERE
#pragma warning(disable:4786)
#include <stdafx.h>
// END CUT HERE
#include <string>
#include <map>
#include <set>
#include <vector>
#include <deque>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <numeric>
using namespace std;

string s[100]={"027","143","751","935","607","903","991","335","047",
"943","471","055","447","463","991","095","607","263","151",
"855","527","743","351","135","407","903","791","135","647"};

void process(int num)
{
	int n;
	cin>>n;
	cout<<"Case #"<<num<<": "<<s[n-2]<<endl;
}

int main(void)
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++) process(i);
	return 0;
}

