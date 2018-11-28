#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
#include <cassert>
#include <complex>
using namespace std;

int A,B;

int cycle(int k) {
	int mul=1, st=1, l=k;
	while (mul<=k) {
		mul*=10;
		st++;
	}
	mul/=10;
	st--;
	vector<int> res0,res1;
	for (int i=1;i<st;i++) {
		int r=k%10;
		k/=10;
		k+=mul*r;
		res0.push_back(k);
	}
	sort(res0.begin(),res0.end());
	for (int i=0;i<res0.size();i++) {
		if (res0[i]<=l) continue;
		else if (i>0&&res0[i]==res0[i-1]) continue;
		else if (res0[i]<A||res0[i]>B) continue;
		res1.push_back(res0[i]);
	}
	return res1.size();
}

int main()
{
    //freopen("in.in","rt",stdin);
    //freopen("out.out","wt",stdout);

	int n;
	cin>>n;
	for (int i=0;i<n;i++) {
		long long res=0;
		cin>>A>>B;
		for (int j=A;j<=B;j++) {
			int k=j;
			int r=cycle(k);
			res+=r;
		}
		printf("Case #%d: ",i+1);
		cout<<res;
		if (i!=n-1) cout<<endl;
	}
    return 0;
} 