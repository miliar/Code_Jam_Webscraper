#include <iostream>
#include <vector>
#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;
struct node{
	string name;
	node* l,*r;
}SP[100000];
int ind=0;
char buff[1010];
int process()
{
	int len=strlen(buff);
	node* p=&SP[0];
	int i=0;
	int ret=0;
	for(i=0;i<len;)
	{
		if(buff[i]=='/')
		{
			string s="";
			i++;
			while(i<len && buff[i]!='/'){
				s+=buff[i];
				i++;
			}
			node* ptr=p->l;
			while(ptr){
				if(ptr->name==s)
					break;
				ptr=ptr->r;
			}
			if(!ptr)
			{
				ret++;
				if(!p->l){
					p->l=&SP[++ind];
					p->l->l=p->l->r=NULL;
					p->l->name=s;
					ptr=p->l;
				}else{
					ptr=p->l;
					while(ptr->r)
						ptr=ptr->r;
					ptr->r=&SP[++ind];
					ptr->r->l=ptr->r->r=NULL;
					ptr->r->name=s;
					ptr=ptr->r;
				}
			}
			p=ptr;
		}
	}
	return ret;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		int n,m;
		scanf("%d%d",&n,&m);
		//memset(&SP[0],0,sizeof(node));
		SP[0].l=SP[0].r=NULL;
		node* root=&SP[0];
		SP->name="/";
		ind=0;
		int i,j;
		getchar();
		for(i=1;i<=n;i++){
			gets(buff);
			int ret=process();
		}
		int ans=0;
		for(i=1;i<=m;i++){
			gets(buff);
			ans+=process();
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}

