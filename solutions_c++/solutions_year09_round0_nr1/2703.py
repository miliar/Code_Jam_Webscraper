#include <vector>
#include <cmath>
#include <queue>
#include <string>
#include <sstream>
#include <fstream>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <cctype>
#include <stack>
 
using namespace std;
 
#define fe(i,a,n) for(int i = a, __n = n; i < __n; i++)
#define fi(i,a,n) for(int i = a, __n = n; i <= __n; i++)
#define LL long long
#define ULL unsigned long long
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define SI stack<int>
#define SS stack<string>
#define SD stack<double>
#define ERRO 1e-10
#define INF 1e+99
#define tr(i,s) for(typeof(s.begin()) i = s.begin(); i != s.end(); i++)
#define all(v) v.begin(), v.end()
#define pb push_back

bool checkPossibility(string a, char b)
{
	if (a[0] == '(')
	{
		fe(i,1,a.size())
		{
			if (b == a[i])
				return true;
			else if (a[i] == ')')
				return false;
		}
	}
	else return (a[0] == b);
}

int main()
{
	int a,b,c;
	cin >> a >> b >> c;
	string x;
	getline (cin,x);
	VS dic;
	
	fe(j,0,b)
	{
		string x;
		getline (cin,x);
		dic.pb(x);
	}
	
	fe(i,0,c)
	{
		int ret=0;
		
		string y,z;
		getline (cin,y);
		
		fe(k,0,b)
		{
			z = y;
			int l;
			for (l=0; l<a; l++)
			{
				if (!checkPossibility(z,dic[k][l]))
					break;
				if (z[0] == '(')
				{
					int pos = z.find(')');
					z = z.substr(pos+1,z.length()-1-pos);
				}
				else
					z = z.substr(1,z.length()-1);
			}
			if (l == a)
				ret++;
		}
		
		if (i!=c-1)
  		   cout << "Case #" << i+1 << ": " << ret << endl;
		else
  		   cout << "Case #" << i+1 << ": " << ret;

	}
	return 0;
}
