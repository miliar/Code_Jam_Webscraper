#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

struct NODE{
	double val;
	string name;
	NODE *l;
	NODE *r;
	NODE():val(0.0),name(""),l(NULL),r(NULL){};
};

int L;

NODE* build(bool &g)
{
	NODE *root = new NODE();
	char line[100];
	gets(line);
	L--;
	int i;
	bool in=false;
	for(i=0;i<strlen(line);i++)
	{
		if(!in && line[i]==' ')
			continue;
		if(!in && line[i]=='(')
		{
			in = true;
			stringstream ss(line+i+1);
			ss>>root->val;
		}
		if(in && line[i]==' ')
		{
			root->name=string(line+i+1);
			for(int k=0;k<root->name.length();k++)
				if(root->name[k]==')')
					root->name.erase(k);
		}
		if(in && line[i]==')')
		{
			if(line[i+1]==')')
				g=false;
			else
				g=true;
			return root;
		}
	}
	bool b=true;
	root->l = build(b);
	root->r = build(b);
	if(b && L>0)
	{
		gets(line);
		L--;
	}
	return root;
}
int main()
{
	freopen("ain.txt","r",stdin);
	freopen("aout.txt","w",stdout);
	int N;
	scanf("%d",&N);
	getchar();
	int i;
	NODE *troot;
	for(i=1;i<=N;i++)
	{
		
		scanf("%d",&L);
		getchar();
		troot=NULL;
		bool g=false;
		troot=build(g);
		printf("Case #%d:\n",i);
		int A;
		scanf("%d",&A);
		getchar();
		int j;
		for(j=1;j<=A;j++)
		{
			char fu[100];
			scanf("%s",fu);
			int n=0;
			scanf("%d",&n);
			set<string>fus;
			while(n--)
			{
				scanf("%s",fu);
				fus.insert(fu);
			}
			double ret=1.0;
			NODE *root = troot;
			while(root!=NULL)
			{
				ret*=root->val;
				if(fus.find(root->name)!=fus.end())
					root = root->l;
				else 
					root = root->r;
			}
			cout<<ret<<endl;
		}	
		
	}	
}