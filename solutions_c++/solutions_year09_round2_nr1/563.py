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

struct node{
	double w;
	string s;
	int l,r;
	int prev;
};

node a[1000000];
char ch[10000];
string s;
vector<string> v;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int i, j, k, n, m, next;
	int type;
	int t, T;
	string p;
	scanf("%d", &T);
	for (t=1;t<=T;t++)
	{
		scanf("%d\n",&n);
		s="";
		for (i=0;i<10000;i++)
			a[i].l=a[i].r=-1;
		for (i=0;i<n;i++)
		{
			gets(ch);
			p=ch;
			s+=p;
		}
			k=0;
			a[k].prev = -1;
			i=0;
			next=1;
			while(s[i]!='(')
				i++;
			i++;
			type=0;
			while(i<s.size())
			{	
				if (s[i]!=' ' && s[i]!=')' && s[i]!='(')
				{
					if (s[i]>='a' && s[i]<='z')
					{
						if (type!=1)
						{
							type = 1;
							p="";
						}
						p+=s[i];
					}
					else
					{
						if (type!=2)
						{
							type = 2;
							p="";
						}
						p+=s[i];
					}
					i++;
				}
				else
				{
					if (type==1)
					{
						type = 0;
						a[k].s=p;
					}
					if (type==2)
					{
						istringstream ss(p);
						ss>>a[k].w;
						type = 0;
					}
					if (s[i]=='(')
					{
						int pre = k;
						if (a[k].l==-1)
							a[k].l=next++;
						else
							a[k].r=next++;
						k=next-1;
						a[k].r=a[k].l=-1;
						a[k].s="";
						a[k].prev=pre;
					}
					if (s[i]==')')
					{
						k=a[k].prev;
					}
					i++;
				}
			}
			scanf("%d",&m);
			printf("Case #%d:\n",t);
			for (j=0;j<m;j++)
			{
				scanf("%s",&ch);
				p=ch;
				scanf("%d",&n);
				vector<string> v;
				for (i=0;i<n;i++)
				{
					scanf("%s",&ch);
					p=ch;
					v.push_back(p);
				}
				k=0;
				double res=1.0;
				while(k!=-1)
				{
					res*=a[k].w;
					int kk=1;
					for (i=0;i<n;i++)
						if (v[i]==a[k].s)
							kk=0;
					if (kk==0)
						k=a[k].l;
					else
						k=a[k].r;
				}
				printf("%.7lf\n",res);
			}
		
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
