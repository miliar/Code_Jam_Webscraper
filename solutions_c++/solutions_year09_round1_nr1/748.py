#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <functional>
#include <queue>
#include <stack>
#include <ctime>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <cassert>
#include <stack>
#include <limits>
#include <cstring>
using namespace std;


typedef long long int64;
typedef unsigned long long uint64;
#define pause system("pause");
#define set0(x) memset(x, 0, sizeof(x))

clock_t __time;
#define retime __time = clock();
#define outtime cout<<clock()-__time<<endl;
const double pi = acos(-1.0);
const double eps = 1e-11;

template<class T> T gcd(const T &a, const T &b) {return (b == 0) ? a : gcd ( b, a%b);}
template<class T> T lcm(const T &a, const T &b) {return a*(b/gcd(a,b));}

int toInt(string s) { istringstream sin(s); int t; sin>>t; return t;}
int64 toInt64(string s) { istringstream sin(s); int64 t; sin>>t; return t;}
string toString(int v ){ ostringstream sout; sout<<v; return sout.str();}
string toString(int64 v){ ostringstream sout; sout<<v; return sout.str();}

bool bd[500000];

int main()
{
	int n,m,sum;
	cin>>n;
	getchar();
	vector<int> base;
	for(int i = 0; i < n; i++)
	{
		base.clear();
		string s;
		int t;
		getline(cin,s);
		istringstream sin(s);
		while(sin>>t)
			base.push_back(t);
		t = 2;
		while(true)
		{
			int j = 0;
			for(j = 0; j < base.size(); j++)
			{
				int tt = t;
				set0(bd);
				while(true)
				{
					if(bd[tt] == true)
						break;
					else
						bd[tt] = true;
					m = tt;
					sum = 0;
					while(m > 0)
					{
						sum += (m%base[j])*(m%base[j]);
						m /= base[j];
					}
					tt = sum;
				}
				if(tt != 1)
					break;
			}
			if(j == base.size())
				break;
			t++;
		}
		cout<<"Case #"<<i+1<<": "<<t<<endl;
	}
	return 0;
}