#include <cstdio>
#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <complex>
#include <cmath>
#include <vector>
#include <list>
#include <sstream>
#include <vector>
#include <cstdlib>
#include <set>
#include <map>
#include <ctime>
using namespace std;
int T,casenum;
long long n,pd,pg,k1,k2,a,b;
long long gcd(long long x,long long y)
{
	if (y==0) return x;
	return gcd(y,x%y);
}
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	cin>>T;
	for (casenum=1;casenum<=T;casenum++)
	{
		cout<<"Case #"<<casenum<<": ";
		cin>>n>>pd>>pg;
		if (pd==0&&pg==0||pd==100&&pg==100)
		{
			cout<<"Possible"<<endl;
			continue;
		}
		if (pd!=0&&pg==0||pd!=100&&pg==100)
		{
			cout<<"Broken"<<endl;
			continue;
		}
		a=100/gcd(100,pd);
		b=100/gcd(100,pg);
		if ((a*pd)%(b*pg)==0) k1=(a*pd)/(b*pg);
		else k1=(a*pd)%(b*pg)+1;
		if ((a*(100-pd))%(b*(100-pg))==0) k2=(a*(100-pd))/(b*(100-pg));
		else k2=(a*(100-pd))%(b*(100-pg))+1;
		//cout<<a<<" "<<k1<<" "<<b<<" "<<k2<<endl;
		if (a>n) cout<<"Broken"<<endl;
		else cout<<"Possible"<<endl;
	}
	return 0;
}
