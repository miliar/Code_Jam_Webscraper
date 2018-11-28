#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
ifstream in("easy.in");
ofstream out("easy.out");

int main()
{
	long long test_count;
	long t;
	long long n, ans=0,m;
	long long l,p,c;

	in >> test_count;
	for(t = 0;t < test_count;t++)
	{
		ans = 0;
		in >> l >> p >> c;
		l*=c;
		while(l<p)
		{
			l*=c;
			ans++;
		}
		long long sol;
		sol = 0;
		while(ans>0)
		{
			sol++;
			ans/=2;
		}
		out<<"Case #"<<t+1<<": "<<sol<<endl;
	}
	return 0;
}