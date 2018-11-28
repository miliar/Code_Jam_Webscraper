// a.cpp : 定义控制台应用程序的入口点。
//
#include "stdafx.h"
#include <fstream>
#include <iomanip>
#include <math.h>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <map>
#include <set>
using namespace std;


class biNode
{
public:
	int data;
	biNode *lchild;
	biNode *rchild;
	biNode()
	{
		data=false;
		lchild=NULL;
		rchild=NULL;
	}
	biNode(int d)
	{
		data=d;
		lchild=NULL;
		rchild=NULL;
	}
	biNode(int d,int f):data(d)
	{
		lchild=NULL;
		rchild=NULL;
	}
};

void clear(queue<biNode *> &que)
{
	while(!que.empty())
		que.pop();
}


class biTree
{
public:
	biNode *root;
	biTree()
	{
		root=NULL;
	}
	void init(biNode *p)
	{
		root = p;
	}
	void generate(biNode *p)
	{
		if(root==NULL)
		{
			root=p;
		}
	}
	void preOrder(biNode *p)
	{
		if(p)
		{
			cout<<p->data;
		}
		if(p->lchild)
			preOrder(p->lchild);
		if(p->rchild)
			preOrder(p->rchild);
	}
	void levelOrder(queue<biNode *> que)
	{
		if(!que.empty())
		{
			cout<<(que.front())->data;
			if((que.front())->lchild)
				que.push((que.front())->lchild);
			if((que.front())->rchild)
				que.push((que.front())->rchild);
			que.pop();
			levelOrder(que);
		}
	}
	void destory(biNode *p)
	{
		if(p->lchild)
			destory(p->lchild);
		if(p->rchild)
			destory(p->rchild);
		delete p;
	}

};




int main()
{
	fstream in("A-large.in",ios::in),out("A-large.out",ios::out);
	int T;
	int i,j,k,l,N;
	string str;
	int temp;
	int result;

	in>>T;
	for(k=0;k<T;k++)
	{
		result=0;
		in>>N;
		int **p=new int*[N];
		int *q=new int[N];
		for(i=0;i<N;i++)
			p[i]=new int[N];
		for(i=0;i<N;i++)
		{
			in>>str;
			for(j=0;j<N;j++)
			{
				p[i][j]=str[j]-'0';
			}
		}
		for(i=0;i<N;i++)
			for(j=N-1;j>=0;j--)
			{
				if(p[i][j])
				{
					q[i]=j;
					break;
				}
			}
		for(i=0;i<N-1;i++)
		{
			if(q[i]>i)
			{		
				for(j=i+1;j<N;j++)
				{
					if(q[j]<=i)	
					{
						l=j;
						break;
					}
					
				}
				result+=l-i;
				for(j=l;j>i;j--)
				{
					temp=q[j];
					q[j]=q[j-1];
					q[j-1]=temp;
				}
			}
		}
//		for(i=0;i<N;i++)
//			cout<<q[i]<<" ";
//		cout<<endl;
		out<<"Case #"<<k+1<<": "<<result<<endl;
	}


	in.close();
	out.close();
	return 0;
}



