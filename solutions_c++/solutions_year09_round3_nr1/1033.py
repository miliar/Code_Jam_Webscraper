// Problem A:

#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
using namespace std;

int solve(string num);

int main()
{
  int T;

	cin >> T;
    cin.ignore();
	
	for(int i = 0; i < T; ++i)
	{
		string num;
		cin >> num;
		cin.ignore();
	    cout << "Case #" << (i+1) << ": " << solve(num) << endl;
	}
	
  return 0;	
}


bool isGreater(pair<char, int> a, pair<char, int> b)
{
	return a.second > b.second;
}


int solve(string num)
{
	unsigned long n = 0;
	int base = 1;
	
//	cout << "Num = " << num << endl;
	
	int diff = 0;
	string hash = "";
	for(int i = 0; i < num.size(); ++i)
	{
		char c = num[i];
		
		if( hash.find(c) == string::npos ) //not found
		{
		  ++diff;	
		  hash.push_back(c);
		}
	}
	
	base = (diff == 1 ) ? 2 : diff;
	
	//cout << "base = " << base << endl;
	
	map<char, int> groups;
	unsigned long pbase = 1;
	
 	for(int i = num.size()-1; i >= 0; --i)
	{
	  char c = num[i];
	
	  if( groups.find(c) == groups.end() )
			groups.insert( pair<char,int>(c, 0) );
		
		groups[c] += pbase;
		pbase *= base;
		
	//	cout << "@ groups " << (char)c << "  " << groups[c] << " "  << pbase << endl;
	}
	
	map<char, int> dig;
	vector< pair<char, int> > vec;
	
	for(map<char,int>::iterator iter = groups.begin(); iter != groups.end(); ++iter)
		vec.push_back(*iter);	
	
	sort( vec.begin(), vec.end(), isGreater);
	
	dig[num[0]] = 1;
	
	int dcount = 0;
	
	for(int i = 0; i < vec.size(); ++i)
	{
	   pair<char, int> p = vec[i];
	
		//cout << "Pair: " << p.first << " -> " << p.second << endl;
	   if( dig.find(p.first) == dig.end() ) // not found
	   {
		   if( dcount == 1 )
		   {   dig[p.first] = 2; dcount = 2; }
		   else
			   dig[p.first] = dcount; 
		   
		   ++dcount;
	   }
	//	cout << "dip[pfirst] = " << dig[p.first] << endl;
		n += p.second * dig[p.first];	
	}
	
	return n;	
}

