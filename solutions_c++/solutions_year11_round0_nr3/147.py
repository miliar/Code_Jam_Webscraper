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
int T,casenum,n,x,m,s,t,i;
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	cin>>T;
	for (casenum=1;casenum<=T;casenum++)
	{
		cout<<"Case #"<<casenum<<": ";
		s=0;m=0x3FFFFFFF;t=0;
		cin>>n;
		for (i=1;i<=n;i++)
		{
			cin>>x;
			t^=x;
			s+=x;
			if (x<m) m=x;
		}
		if (t!=0) cout<<"NO"<<endl;
		else cout<<s-m<<endl;
	}
	return 0;
}
