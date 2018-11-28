#include <stdio.h>
#include <string.h>
#include <string>
#include <set>
#include <iostream>
#include <cassert>
#include <stdlib.h>
using namespace std;

typedef struct Node
{
	Node *l,*r;
	string para;
	double p;
}Node;
Node *root;
Node stack[128];
int used_stack;
Node node[110];

set<string> S;

Node *NewNode()
{
	Node *ret = &node[used_stack++];
	ret->l = ret->r = 0;
	ret->para = "";
	return ret;
}
Node *AddNode()
{
	bool have_left = false;
	char buf[256];
	int i,top;
	Node *me = NewNode();
	scanf("%lf",&me->p);
	while (scanf("%c",buf))
	{
		if (buf[0]==')') return me; 
		if (isalpha(buf[0]))
		{
			top = 1;
			while (isalpha(buf[top++] = getchar()) );
			buf[top-1] = 0;
			me->para += buf;
			while (getchar()!='(') ;
			me->l = AddNode();
			while (getchar()!='(') ;
			me->r = AddNode();
		}
	}
	
/*	
	
	gets(temp);
	for (i=0;temp[i]==' ';++i);
	strcpy(buf,temp+i);
	if (buf[0]=='(')
	{
		sscanf(buf+1,"%lf%c",&me->p,&tag);
		if (tag==')') return me;
		sscanf(buf+1,"%*lf %s",temp);
		me->para += temp;
		me->r = AddNode();
		gets(buf);
		return me;
	}
	else
	{
		assert(false);
		printf("Build Error!!~");
		return 0;
	}*/
}


double Cul(Node *index,double p)
{
	double ret = p* index->p;
	if (index->l || index->r)
	{
		if (S.find(index->para) != S.end())
		{
			return Cul(index->l,ret);
		}
		else
		{
			return Cul(index->r,ret);
		}
	}
	else return ret;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("ALargeout.txt","w",stdout);
	int st,t,i,N;
	int m,j;
	char buf[1024];
	scanf("%d",&st);
	for (t=0;t<st;++t)
	{
		scanf("%d%*c",&N);
		used_stack = 0;
		while (getchar()!='(') ;
		root = AddNode();
		scanf("%d",&N);
		printf("Case #%d:\n",t+1);
		for (i=0;i<N;++i)
		{
			scanf("%*s%d",&m);
			S.clear();
			for (j=0;j<m;++j)
			{
				string temp;
				cin>>temp;
				S.insert(temp);
			}
			printf("%.7lf\n",Cul(root,1));
		}
	}
	return  0;
}




