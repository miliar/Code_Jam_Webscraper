// Google1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;
vector <int> s;
typedef vector <int> vi;
int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int num;
	in>>num;
	for (int isd=0;isd<num;isd++)
	{
		int p,k,l;
		in>>p>>k>>l;
		for (int i=0;i<l;i++)
		{
			int ks;
			in>>ks;
			s.push_back(ks);
			
		}
		
		sort(s.begin(),s.end(),greater<int>());
		vector <vi> ksa(k);
		int nums=0;
		int is=0;
		while (s.size()!=0)
		{
			int i=is%k; 
			nums+=(ksa[i].size()+1)*(*max_element(s.begin(),s.end()));
			ksa[i].push_back(*max_element(s.begin(),s.end()));
			s.erase(max_element(s.begin(),s.end()));
			is++;

		}
		out<<"Case #"<<isd+1<<": "<<nums<<endl;
	}
	return 0;
}

