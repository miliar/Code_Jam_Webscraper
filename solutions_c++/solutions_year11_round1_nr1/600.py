#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <stack>
#include <cassert>
using namespace std;
typedef long long LL;

LL gcd(LL a,LL b)
{
	if(a==0LL)
		return b;
	return gcd(b%a,a);
}

int main (int argc, char * const argv[]) {
	int T;
	LL N,PD,PG;
	cin >> T;
	for(int c=1;c<=T;++c)
	{
		cin >> N >> PD >> PG ;
		LL minD=0,minG=0,minDL=0,minDW=0, minGL=0,minGW=0;
		if(PD==0)
			minD=1;
		else 
			minD=100/gcd(PD,100);
		minDW=(PD*minD)/100;
		minDL=minD-minDW;
		if(PG==0)
			minG=1;
		else 
			minG=100/gcd(PG,100);
		minGW=(PG*minG)/100;
		minGL=minG-minGW;
		if(minD<=N && minGW*100>=minDW && minGL*100>=minDL)
			cout << "Case #" << c << ": Possible"  << endl;
		else 
			cout << "Case #" << c << ": Broken"  << endl;
	}
	return 0;
}
