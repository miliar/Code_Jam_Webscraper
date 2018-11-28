#include <iostream>
#include<string.h>
using namespace std;
struct node
{
	char name[100];
	node *next[100];
	int num;
};
	int sum;
node *insert(node *p,char na[101])
{
	int i;
	node *q;
	bool find=0;
	for(i=0;i<p->num;i++)
		if(strcmp(p->next[i]->name,na)==0)
		{
			find=1;
			return p->next[i];
		}
	if(find==0)
	{
		sum++;
		q=new node;
		q->num=0;
		strcpy(q->name,na);
		p->next[p->num++]=q;
	}
	return q;
}

int main()
{
	freopen("out.txt","w",stdout);
	int t,i,j;
	cin>>t;
	int n,m;
	node *root,*p;
	int cnt,ca=0;
	char ch[101],name[101];
	while(t--)
	{
		root=new node;
		root->num=0;
		cin>>n>>m;
		sum=0;
		for(j=0;j<n;j++)
		{
			cin>>ch;
			i=1;
			p=root;
			while(ch[i]!='\0')
			{
				cnt=0;
				while(ch[i]!='/' && ch[i]!='\0')
				{
					name[cnt++]=ch[i++];
				}
				name[cnt]='\0';
				p=insert(p,name);
				
				if(ch[i]=='\0')break;
				i++;
			}
		}
		sum=0;
		for(j=0;j<m;j++)
		{
			cin>>ch;
			i=1;
			p=root;
			while(ch[i]!='\0')
			{
				cnt=0;
				while(ch[i]!='/' && ch[i]!='\0')
				{
					name[cnt++]=ch[i++];
				}
				name[cnt]='\0';
				p=insert(p,name);
				
				if(ch[i]=='\0')break;
				i++;
			}
		}
		printf("Case #%d: %d\n",++ca,sum);
	}
	return 0;
}




