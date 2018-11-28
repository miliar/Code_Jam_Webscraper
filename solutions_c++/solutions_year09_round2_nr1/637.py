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

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define pi acos(-1.0)
#define inf (1<<30)
#define clr(a,b) memset(a,b,sizeof(a))
#define pb push_back

struct nd
{
	string atr;
	double w;
	nd *l,*r;
};
struct ani
{
	string nm;
	map<string,int> mp;
	int n;
}b;

string a,tmp;
char s[1000];
nd *root;
string ar[1000];

void build(nd *ob,int i,int j)
{
	if(ar[i]==")")
		return;
	double val;
	sscanf(ar[i].c_str(),"%lf",&val);
	ob->w=val;
	ob->l= NULL;
	ob->r= NULL;
	if(i==j)
		return;
	int cnt=0,k;
	for(k=i+2;k<=j;k++)
	{
		if(ar[k]=="(")
			cnt++;
		if(ar[k]==")")
			cnt--;
		if(cnt==0)
			break;
	}
	if(k>i)
	{
		ob->l=new nd();
		ob->l->atr=ar[i+1];
		build(ob->l,i+3,k-1);
	}
	if(k+1<j)
	{
		ob->r=new nd();
		build(ob->r,k+2,j-1);
	}
}
double func(nd *ob)
{
	double r;
	r=ob->w;
	if(ob->l == NULL && ob->r == NULL)
		return r;
	if(b.mp[ob->l->atr])
	{
		r*=func(ob->l);
	}
	else
	{
		r*=func(ob->r);
	}
	return r;
}
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cs,t=1,i,j,k,n,l;
	double p;
	cin>>cs;
	while(cs--)
	{
		cin>>l;
		getchar();
		a="";
		for(i=0;i<l;i++)
		{
			gets(s);
			for(j=0;s[j];j++)
			{
				if(s[j]==')')
					a+=' ';
				a+=s[j];
				if(s[j]=='(')
					a+=' ';
			}
		}
		stringstream kin(a);
		k=0;
		while(kin>>tmp)
		{
			ar[k++]=tmp;
		}
		root=new nd();
		build(root,1,k-2);
		cin>>n;
		printf("Case #%d:\n",t++);
		while(n--)
		{
			cin>>b.nm>>b.n;
			b.mp.clear();
			for(i=0;i<b.n;i++)
			{
				cin>>tmp;
				b.mp[tmp]=1;
			}
			p=func(root);
			printf("%.7lf\n",p);
		}
	}
	return 0;
}


