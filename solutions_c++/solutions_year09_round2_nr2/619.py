#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;
int a[10];
int b[10];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int i, j, k, n, m;
	int t, T;
	scanf("%d\n", &T);
	char ch[22];
	string s, p;
	for (t=1;t<=T;t++)
	{
		gets(ch);
		s=ch;
		p="";
		n=s.size();
		for (i=0;i<10;i++)
			a[i]=0;
		int type=1;
		for (i=0;i<n-1;i++)
			if (s[i+1]>s[i])
				type=0;
		if (type)
		{
			sort(s.begin(), s.end());
			i=0;
			while(s[i]=='0')
				i++;
			p+=s[i];
			p+='0';
			for (j=0;j<n;j++)
				if (i!=j)
					p+=s[j];
		}
		else
		{
			p=s;
			for (j=n-2;j>=0;j--)
			{
				for (i=0;i<10;i++)
					a[i]=0;
				for (i=0;i<n;i++)
					a[s[i]-'0']++;
				for (i=0;i<j;i++)
				{
					p[i]=s[i];
					a[p[i]-'0']--;
				}
				k=0;
				for (i=s[j]-'0'+1;i<10;i++)
					if (a[i]>0)
					{
						k=1;
						a[i]--;
						p[j] = i+'0';
						break;
					}
				if (k)
				{
					for (i=j+1;i<n;i++)
					{
						for (int u=0;u<10;u++)
						{
							if (a[u]>0)
							{
								a[u]--;
								p[i]=u+'0';
								break;
							}
						}
					}
					break;
				}
			}
		}
		printf("Case #%d: %s\n",t,p.c_str());
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
