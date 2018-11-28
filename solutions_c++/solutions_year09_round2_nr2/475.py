#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;
string intToS(long long n) { char p[100];sprintf(p,"%lld",n);return string(p);}
int main()
{
	string n;
	int T;
	cin >> T;
	for(int k = 1; k<= T; ++k)
	{
		cin >> n;
		string p = n;
		string q = p;
		next_permutation(p.begin(),p.end());
		if( p <= q) 
		{
			p = "0" + p;
			int t = 0; 
			while(p[t] == '0') t++;
			swap(p[0],p[t]);
		}
		cout << "Case #" << k << ": " << p << endl;
	}
}