#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <cstdio>

using namespace std;

int i,j,k,l,m,n,t,A,B, pow_10,res,a;
set <int> pairs;

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>t;
	for (int ii=1;ii<=t;ii++){
		cout<<"Case #"<<ii<<": ";
		cin>>A>>B;
		a=A;
		n=0;
		while (a>0) {
		  n++;
		  a/=10;
		}
		pow_10=1;
		for (i=0;i<n-1;i++)
		  pow_10*=10;
		res=0;
		for (int cur = A;cur<=B;cur++){
		  int cur1 = cur;
		  pairs.clear();
		  for (j=0;j<n;j++){
		    cur1 = cur1/10 + pow_10 * (cur1%10);
		    if (cur1<=B)
		      if (cur1>cur)
			pairs.insert(cur1);
		  }
		  res=res+pairs.size();
		}
		cout<<res<<'\n';
	}
	return 0;
}
