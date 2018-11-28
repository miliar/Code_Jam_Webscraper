#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
using namespace std;
int main()
{
	int tc,i,j,l;
	long long k;
	string s,r="";
	vector<int> x;
	vector<long long> ans;
	long long ansx,ansm;
	cin>>tc;
	for(i=0;i<tc;i++)
	  {
	    cin>>k>>s;
	    x.erase(x.begin(),x.end());
	    for(j=0;j<k;j++)
	      x.push_back(j);
	    ansm=50000;
	    do
	      {
		r="";
		for(l=0;l<s.size();l+=k)
		  for(j=0;j<x.size();j++)
		    r+=s[l+x[j]];
		ansx=1;
		for(j=1;j<r.size();j++)
		  if(r[j]!=r[j-1])
		    ansx++;
		if(ansm>ansx)
		  ansm=ansx;
	      }
	    while(next_permutation(x.begin(),x.end()));
	    ans.push_back(ansm);
	  }
	for(i=0;i<ans.size();i++)
		cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
	return 0;
}
