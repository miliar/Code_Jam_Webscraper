#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
using namespace std;

int main()
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		string s;
		cin>>s;
		if(!next_permutation(s.begin(),s.end()))
		{
			s+="0";
			sort(s.begin(),s.end());
			if(s[0]=='0')
			{	
			for(int i=0;i<s.size();i++)
			{
				if(s[i]!='0')
				{swap(s[0],s[i]);break;}			
			}
			}
	
		}
		printf("Case #%d: %s\n",i,s.c_str());
	}
	return 0;
}
