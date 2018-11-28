/*
 *  problem1a.cpp
 *  codejam1
 *
 *  Created by Rohit Bansal on 7/26/08.
 *  Copyright 2008 __MyCompanyName__. All rights reserved.
 *
 */

#include "problem1a.h"
#ifdef __GNUC__
#include <ext/hash_map>
#else
#include <hash_map>
#endif
#include <iostream>
#include <ctime>
#include <algorithm>
#include <string>
#include <cstdio>
#include <vector>
namespace __gnu_cxx
{
        template<> struct hash< std::string >
        {
                size_t operator()( const std::string& x ) const
                {
                        return hash< const char* >()( x.c_str() );
                }
        };
}
namespace std
{
 using namespace __gnu_cxx;
}
using namespace std;
int main (int argc, char * const argv[]) 
{
	long nCases;
	cin >> nCases;
	for (int nCase=0; nCase < nCases; nCase++)
	{
		int nCoordinates;
		cin >> nCoordinates;
		string str;
		vector<int> v1,v2;
		int val,i,j;
		for (i=0 ; i < nCoordinates; i++)
		{
				cin >> val;
				v1.push_back(val);
		}
		for (int i =0 ; i < nCoordinates; i++)
		{
			cin >> val;
			v2.push_back(val);
		}
		std::sort(v1.begin(),v1.end());
		std::sort(v2.begin(),v2.end());
		int sum = 0;
		for(i=0,j=v2.size()-1;i<v1.size();i++,j--)
		{
			sum += (v1[i]*v2[j]);
		}
		cout << "Case #"<<nCase+1<<": " << sum << endl;
	}
}