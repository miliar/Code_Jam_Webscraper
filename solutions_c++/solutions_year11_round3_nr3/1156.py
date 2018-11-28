// Sai
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


inline int LCM(int a,int b)
{
	return a*b/__gcd(a,b);
}

int main()
{
//	freopen("harmony.in","r",stdin);
//	freopen("harmony.out","w",stdout);
	int no_of_testcases;
	cin>>no_of_testcases;
	for(int tcase=1;tcase<=no_of_testcases;++tcase)
	{
		int n,l,h;
		cin>>n>>l>>h;
		int a[n];
		for(int i=0;i<n;i++) cin>>a[i];
		bool ans_found=false;
		int ans;
		for(int ns=l;ns<=h && !ans_found;ns++)
		{
			ans_found=true;
			for(int i=0;i<n;i++)
				if(ns%a[i]!=0 && a[i]%ns!=0)
					ans_found=false;
			ans=ns;
		}
		cout<<"Case #"<<tcase<<": ";
		if(ans_found)	cout<<ans;
		else			cout<<"NO";
		cout<<endl;
	}
}
