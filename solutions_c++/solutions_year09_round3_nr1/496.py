#include <vector>
#include <string>
#include <iostream>
#include <memory.h>
#include <algorithm>
#include <stack>
#include <fstream>
#include <sstream>
#include <map>

using namespace std;


#define All(v) (v).begin(), (v).end()
#define ffor(i,n) for(int i=0; i<n; i++)
#define LL long long
#define LD long double
#define psh push_back
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))


int main()
{
	int c;
	cin >> c;

	for(int i = 0; i < c; i++)
	{
		vector<int> num;
		string t;

		cin >> t;

		ffor(j,t.size())
		{
			if(t[j] >= 48 && t[j] <= 57)
				num.psh(t[j]-48);
			else
				num.psh(t[j] - 87);
		}

		vector<int> sp;
		bool zerof	= false;

		map<int,int> val;
		int cval	= 1;

		ffor(j,num.size())
		{
			if(val.find(num[j]) == val.end())
			{
				if(j != 0 && !zerof)
				{
					val[num[j]]	= 0;
					zerof	= true;
				}
				else
					val[num[j]]	= cval++;
			}
		}


		int base	= (val.size() < 2) ? 2 : val.size();

		long long res	= 0;
		long long mul	= 1;
		for(int j = num.size() -1; j >= 0; j--)
		{
			res	+= val[num[j]]*mul;
			mul	*= base;
		}


		cout << "Case #" << i+1 << ": " <<  res <<     endl;
	}
}
