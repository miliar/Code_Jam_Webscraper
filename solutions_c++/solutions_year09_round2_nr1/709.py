#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>

using namespace std;

typedef __int64 ll;

char s[100][1010];
struct node
{
	int isl;
	node *l,*r;
	double p;
	string s;
};
int h;
char s2[10000];
void dfs(node *ft)
{
	int i,k,len=strlen(s[h]),cc=0;
	for(i=0;i<len;i++) 
	{
		if(s[h][i]=='(') k=i;
		if(s[h][i]==')') cc=1;
	}
	stringstream ss;ss<<(s[h]+k+1);
	double p;ss>>p;
	h++;
	if(cc)
	{
		ft->isl=1;ft->l=0;ft->r=0;ft->p=p;return ;
	}
	ss>>s2;
	ft->isl=0;ft->l=new node();ft->r=new node();ft->p=p;
	ft->s=s2;
	dfs(ft->l);
	dfs(ft->r);
	h++;
}
double ans=0;
int a;
string st[100];
void find(node *now,double p)
{
	int i,k;
	if(now->isl) {ans=p*now->p;return ;}
	for(i=0;i<a;i++) 
	{
		if(now->s==st[i]) break;
	}
	if(i<a) 
	{
		find(now->l,p*now->p);
	}
	else find(now->r,p*now->p);
}

int main()
{
	int i,j,k,ca,l,n;
	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	scanf("%d",&ca);
	int kk=1;
	while(ca--)
	{
		scanf("%d",&l);getchar();
		for(i=0;i<l;i++) gets(s[i]);
		node *ft;ft=new node();
		h=0;
		dfs(ft);
		scanf("%d",&n);
		printf("Case #%d:\n",kk++);
		for(i=0;i<n;i++)
		{
			scanf("%s",s2);
			scanf("%d",&a);
			for(j=0;j<a;j++) cin>>st[j];
			find(ft,1);
			printf("%.7lf\n",ans);
		}
	}
	return 0;
} 