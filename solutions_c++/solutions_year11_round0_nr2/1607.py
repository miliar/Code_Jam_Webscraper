
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;
/*
int main()
{
	int t;
	int n,i;
	long long a,b;
	freopen("A.out","w",stdout);
	scanf("%d",&t);
	int d = 1;
	while(t--)
	{
		long long Min;
		scanf("%d",&n);
		scanf("%lld",&a);
		Min = a;
		long long sum = a;
		for(i=1;i<n;i++)
		{
			scanf("%lld",&b);
			sum += b;
			if(Min > b)
				Min = b;
			a ^= b;
		}
		if(a != 0)
		{
			printf("Case #%d: NO\n",d++);
		}
		else
			printf("Case #%d: %lld\n",d++,sum-Min);
	}
	return 0;
}
*/

int main()
{
	int t,n,i,k,j,a,b;
	freopen("A.out","w",stdout);
//	freopen("","r",stdin);
	string str,st,s;
	string ans,temp;
	scanf("%d",&t );
	{
		int d = 1;
		while(t--)
		{
			temp = ans = "";
			scanf("%d",&a);
			if(a) cin>>s;
			scanf("%d",&b);
			if(b) cin>>st;
			scanf("%d",&n);
			cin>>str;
			int flag = 1;
			int len = 0; 
			for(i=0;i<n;i++)
			{
				if(a&&len>=1 && ((str[i]==s[0]&&temp[len-1]==s[1]) ||(str[i]==s[1]&&temp[len-1]==s[0])))
				{
					temp[len-1] = s[2];
				}
				else if(b)
				{
					if(str[i]==st[0])
					{
						j=0;
						while(temp[j]!=st[1] && j<len)j++;
						if(j!=len){temp="";len=0;}
						else temp += str[i],len++;
					}
					else if(str[i]==st[1])
					{
						j=0;
						while(temp[j]!=st[0] && j<len)j++;
						if(j!=len){temp="";len=0;}
						else temp += str[i],len++;
					}
					else
					{
						temp += str[i],len++;
					}
				}
				else 
				{
					temp += str[i];
					len++;
				}
					
			}
			temp += '\0';
			if(len == 0) ans = "[]";
			else
			{
				ans = "[";
				ans += temp[0];
				for(i=1;i<len;i++)
					ans += ", ",ans +=  temp[i];
				ans += "]";
			}
			cout<<"Case #"<<d++<<": "<<ans<<"\n";
		}
	}
	return 0;
}
/*
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW

*/