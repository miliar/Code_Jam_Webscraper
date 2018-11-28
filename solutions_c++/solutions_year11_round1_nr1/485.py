#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

long long gcd(long long a, long long b)
{
	if(b==0) return a;
	if(a==0) return b;
    while( 1 )
    {
        a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

        if( b == 0 )
			return a;
    }
}

int main()
{
	bool pos;
	long long t, caseN, n, p1, p2, k, l;
	fin>>t;
	for(caseN=1; caseN<=t; ++caseN)
	{
		pos = true;
		fin>>n>>p1>>p2;
		k = gcd(100, p1);
		l = 100 / k;
		if(l > n )
			pos = false;
		if(p2 == 100 && p1 !=100)
			pos = false;
		if(p2 == 0 && p1 != 0)
			pos = false;
		if(pos)
			fout<<"Case #"<<caseN<<": "<<"Possible"<<endl;
		else
			fout<<"Case #"<<caseN<<": "<<"Broken"<<endl;
	}
	return 0;
}