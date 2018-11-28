#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

long long v,i,j,t,x;
string s;
long long ans,q,k;
long long a[100],mark[100];

int main()
{
	freopen("a.in","rt",stdin);
	freopen("a.out","wt",stdout);
	cin >> t;
	for (v = 1;v<=t;v++)
	{
	        cin >> s;
	        memset(mark,0,sizeof(mark));
	        k = 0;
	        for (i = 0;i<s.length();i++)
	        	if (s[i] == s[0])
	        	{
	        		a[i] = 1;
	        		mark[i] = 1;
	        	}
	       	for (i = 1;i<s.length();i++)
	       		if (mark[i] == 0)
	       		{
	       			for (j = 1;j<s.length();j++)
	       				if ((s[j] == s[i])&&(mark[j] == 0))
	       				{
	       					a[j] = k;
	       					mark[j] = 1;	
	       				}
	       			k++;
	       			if (k == 1) k++;
	       		}
	       	ans = 0;
	       	if (k<=1) k = 2;
	       	for (i = 0;i<s.length();i++)
	       	{
	       		q = 1;
	       		for (j = 1;j<=s.length()-i-1;j++)
	       			q = q*k;
	       		ans += a[i]*q;	
	       	}		
		cout << "Case #" << v << ": " << ans << endl;
	}
	return 0;
}



