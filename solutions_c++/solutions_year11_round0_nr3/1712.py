
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int t;
	int n,i,a,b;
	freopen("A.out","w",stdout);
	scanf("%d",&t);
	int d = 1;
	while(t--)
	{
		int Min;
		scanf("%d",&n);
		scanf("%d",&a);
		Min = a;
		int sum = a;
		for(i=1;i<n;i++)
		{
			scanf("%d",&b);
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
			printf("Case #%d: %d\n",d++,sum-Min);
	}
	return 0;
}

/*
int main()
{
	int t,n,i,k,j,a,b;
	freopen("A.out","w",stdout);
//	freopen("","r",stdin);
	string str,st,s;
	string ans;
	scanf("%d",&t );
	{
		int d = 1;
		while(t--)
		{
			ans = "[";
			scanf("%d",&a);
			if(a) cin>>s;
			scanf("%d",&b);
			if(b) cin>>st;
			scanf("%d",&n);
			cin>>str;
			int flag = 1;
			for(i=0;i<n;i++)
			{
				if(a && i!=n-1&&((str[i]==s[0] && str[i+1]==s[1]) || (str[i]==s[1] && str[i+1]==s[0])))
				{
					if(flag){flag--;}
					else
						ans += ", ";
					ans += s[2];
					i++;
				}
				else if(b && i!=n-1 &&((str[i]==st[0] && str[i+1]==st[1]) || (str[i]==st[1] && str[i+1]==st[0])))
				{
					i++;
					ans = "[";
					flag = 1;
				}
				else if(b && i!=n-1 && ((str[i]==st[0] && str[i+2]==st[1]) || (str[i]==st[1] && str[i+2]==st[0])) )
				{
					i+=2;
					ans = "[";
					flag = 1;
				}
				else 
				{
					if(flag){flag--;}
					else
						ans += ", ";
					ans += str[i];
				}
					
			}
			ans += "]";
			cout<<"Case #"<<d++<<": "<<ans<<"\n";
		}
	}
	return 0;
}*/
/*
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW

*/