#include <iostream>
#include <string>
#include <cmath>
#include <ctime>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <numeric>
#include <map>
using namespace std;
#define FOR(i,n) for (long long i=0;i<(long long)n;i++)
#define FORN(i,a,b) for (long long i=a;i<=(long long)b;i++)
#define FORIT(it,m) for (it=m.begin();it!=m.end();it++)




int main()
{
	unsigned long long t,n,k,caseNum=1;
	
	cin>>t;
	FOR(i,t)
	{
		cin>>n>>k;
		if ((1i64<<n)-1==k%(1i64<<n)) cout<<"Case #"<<caseNum<<": ON"<<endl;
		else cout<<"Case #"<<caseNum<<": OFF"<<endl;
		caseNum++;
	}

	return 0;
}