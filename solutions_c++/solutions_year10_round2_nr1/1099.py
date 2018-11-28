#include "stdafx.h"
#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
using namespace std;
struct node
{
	string dir;
	vector<struct node *> child;
};
int main()
{
	int t,n,m;
	int i,j,k,h;
	string str,dir;
	struct node *p,*q,*root;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>n>>m;
		p= new struct node ;
		root=p;
		for(i=0;i<n;i++)
		{
			cin>>str;
			str=str.substr(1);
			p=root;
			j=str.find('/');
			while(j!=string::npos)
			{
				dir=str.substr(0,j);
				str=str.substr(j+1);
				bool flag=false;
				for(h=0;h<p->child.size();h++)
				{
					if(p->child[h]->dir==dir)
					{
						flag=true;
						p=p->child[h];
						break;
					}
				}
				if(flag==false)
				{
					q=new struct node;
					q->dir=dir;
					p->child.push_back(q);
					p=q;
				}
				j=str.find('/');
			}
			bool flag=false;
			for(h=0;h<p->child.size();h++)
			{
				if(p->child[h]->dir==str)
				{
					flag=true;
					p=p->child[h];
					break;
				}
			}
			if(flag==false)
			{
				q=new struct node;
				q->dir=str;
				p->child.push_back(q);
				p=q;
			}
		}
		int c=0;
		for(i=0;i<m;i++)
		{
			cin>>str;
			str=str.substr(1);
			p=root;
			j=str.find('/');
			while(j!=string::npos)
			{
				dir=str.substr(0,j);
				str=str.substr(j+1);
				bool flag=false;
				for(h=0;h<p->child.size();h++)
				{
					if(p->child[h]->dir==dir)
					{
						flag=true;
						p=p->child[h];
						break;
					}
				}
				if(flag==false)
				{
					q=new struct node;
					q->dir=dir;
					p->child.push_back(q);
					p=q;
					c++;
				}
				j=str.find('/');
			}
			bool flag=false;
			for(h=0;h<p->child.size();h++)
			{
				if(p->child[h]->dir==str)
				{
					flag=true;
					p=p->child[h];
					break;
				}
			}
			if(flag==false)
			{
				q=new struct node;
				q->dir=str;
				p->child.push_back(q);
				p=q;
				c++;
			}
		}
		cout<<"Case #"<<k<<": "<<c<<endl;
	}
}