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

int main()
{
	int c;
	cin >> c;
	string x;
	getline (cin,x);
	
	fe(i,0,c)
	{
		int ret=0;
		
		string in = "welcome to code jam";
		
		string test;
		getline (cin,test);
		
		int a[in.size()+1][test.size()+1];
		
		fe (j,0,test.size()+1)
		{
			a[0][j] = 0;
		}
		
		fe (j,0,in.size()+1)
		{
			a[j][0] = 0;
		}
		fe (j,1,in.size()+1)
		{
			fe (k,1,test.size()+1)
			{
				if (test[k-1] == in[j-1])
				{
					if (j==1)
					{
						a[j][k] = a[j][k-1] + a[j-1][k] + 1;
						//cout << j << " " << k << " " << a[j][k] << endl;
					}
					else
					{
						a[j][k] = a[j][k-1] + a[j-1][k];
						//cout << j << " " << k << " " << a[j][k] << endl;
					}
				}
				else
				{
					a[j][k] = a[j][k-1];
					//cout << j << " " << k << " " << a[j][k] << endl;
				}
				if (a[j][k] > 10000)	a[j][k] -= 10000;
			}
		}
		ret = a[in.size()][test.size()];
		
		if (ret < 10)
			cout << "Case #" << i+1 << ": 000" << ret;
		else if (ret < 100)
			cout << "Case #" << i+1 << ": 00" << ret;
		else if (ret < 1000)
			cout << "Case #" << i+1 << ": 0" << ret;
		else
			cout << "Case #" << i+1 << ": " << ret;
		
		if (i!=c-1)
			cout << endl;
	}
	return 0;
}
