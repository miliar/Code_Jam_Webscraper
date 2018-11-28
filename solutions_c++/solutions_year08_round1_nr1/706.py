#include <stdio.h>
#include <iostream>
#include"algorithm"
#include <string>
#include <vector>
#include <map>
#include <math.h>
#include <functional>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
  	freopen("A-small-attempt0.out","w",stdout);
	int i,Case,num,ans,n;
	VI va,vb;
	cin>>Case;
	num=1;
	while (Case--)
	{
		cin>>n;
		va.resize(n);
		vb.resize(n);
		for(i=0;i<n;i++)
			cin>>va[i];
		for(i=0;i<n;i++)
			cin>>vb[i];
		sort(va.begin(),va.end(),greater<int>());
		sort(vb.begin(),vb.end(),less<int>());
		ans=0;
		for(i=0;i<n;i++)
			ans+=va[i]*vb[i];
		printf("Case #%d: %d\n",num++,ans);	
	}
	return 0; 
}