#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define FOR(i,n) for( i = 0 ; i<n ; i++)
#define RFOR(i,a,b)  for( i = a ; i<b ; i++)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))
#define i64 __int64
#define eps 1e-11
#define inf (1<<29)

int main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("B.out","w",stdout);
	char a[2020];
	string s;
	int tc,fg = 1,i,j;
	cin>>tc;
	while(tc--)
	{
		cin>>s;
		strcpy(a,s.c_str());
		bool fl = false;
		for(i = 1;i<s.size();i++)
		{
			if(s[i] > s[i-1])
			{
				next_permutation(s.begin(),s.end());
				cout<<"Case #"<<fg++<<": "<<s<<endl;
				fl = true;
				break;
			}

		}
		char minn = 100000;
		int minpos = 1000000;
		if(!fl)
		{
			for(i = s.size() - 1;i>=0;i--)
			{
				if(s[i]!='0')
					break;				
			}
			string ans = "";
			ans+=s[i];
			ans+="0";
			for(j = s.size()-1;j>=0;j--)
			{
				if(j == i)
					continue;
				ans+=s[j];
			}
			cout<<"Case #"<<fg++<<": "<<ans<<endl;

		}
	}
	
	
	return 0;
}