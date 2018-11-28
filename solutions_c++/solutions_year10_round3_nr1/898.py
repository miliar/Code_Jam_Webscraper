#include "stdafx.h"
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <math.h>
#include <map>
#include <list>
#include <set>
#include <queue>
using namespace std;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)

class A
{
public:
	void execute()
	{
		int t, n;
		cin >> t;
		REP(i, t)
		{
			cin >> n;
			vector<int> a;
			vector<int> b;
			int a1, b1;
			REP(j, n)
			{
				cin >> a1 >> b1;
				a.push_back(a1);
				b.push_back(b1);
			}
			int ret = run(a, b);
			cout << "Case #"<< i+1 << ": "<<ret<<endl;
			a.clear();
			b.clear();
		}
	}

	int run(vector<int>& a, vector<int>& b)
	{
		int ret = 0;
		int size = a.size();
		REP(i, size)
		{
			for(int j = i+1; j < size; ++j)
			{
				if(inter(a[i], b[i], a[j], b[j]))
				{
					ret++;
				}
			}
		}
		return ret;
	}

	bool inter(int a1, int b1, int a2, int b2)
	{
		if((a1 > a2 && b1 < b2) || (a1 < a2 && b1 > b2))
		{
			return true;
		}
		return false;
	}



	
};

int main()
{ 
	A t;
	t.execute();
}
