#include <stdio.h>
#include <vector>
#include <string>
#include <string.h>

using namespace std;

struct Node
{
    string name;
	vector <Node*> son;

	Node()
	{
	    name="";
		son.clear();
	}
};

int main(void)
{
	freopen("A-large.in", "r", stdin);
	freopen("ala.out", "w", stdout);
    int t,n,m;
	string s;
	int k,len,l;
	char str[200];
	bool ok;

	scanf("%d", &t);

	for(int i=1; i<=t; i++)
	{
	    scanf("%d%d",&n,&m);

		Node root;
		root.name="root";
		Node *p,*q;

		for(int j=0; j<n; j++)
		{
		    scanf("%s", str);
			len = strlen(str);
			s="";
			p=&root;
			for(k=0; k<len; k++)
			{
			     if(str[k]=='/'&&s!="")
				 {
					 ok=false;
				     for(l=0; l<(p->son).size(); l++)
					 {
					     if(s==p->son[l]->name)
						 {
							 ok=true;
							 p=p->son[l];
							 break;
						 }
					 }
					 if(!ok)
					 {
						 q=new Node();
						 q->name=s;
					     p->son.push_back(q);
						 p=q;
					 }
					 s="";
				 }
				 else if(str[k]!='/')
				 {
					 s+=str[k];
				 }
			}
			if(s!="")
			{
					 for(l=0; l<(p->son).size(); l++)
					 {
					     if(s==(p->son[l])->name)
						 {
							 break;
						 }
					 }
					 if(l==(p->son).size())
					 {
						 q=new Node();
						 q->name=s;
					     p->son.push_back(q);
					 }
			}
		}

		int ans=0;
		for(j=0; j<m; j++)
		{
		    scanf("%s", str);
			len = strlen(str);
			s="";
			p=&root;
			for(k=0; k<len; k++)
			{
			     if(str[k]=='/'&&s!="")
				 {
					 ok=false;
				     for(l=0; l<(p->son).size(); l++)
					 {
					     if(s==(p->son[l])->name)
						 {
							 ok=true;
							 p=p->son[l];
							 break;
						 }
					 }
					 if(!ok)
					 {
						 q=new Node();
						 ans++;
						 q->name=s;
					     p->son.push_back(q);
						 p=q;
					 }
					 s="";
				 }
				 else if(str[k]!='/')
				 {
					 s+=str[k];
				 }
			}
			if(s!="")
			{
					 for(l=0; l<(p->son).size(); l++)
					 {
					     if(s==p->son[l]->name)
						 {
							 break;
						 }
					 }
					 if(l==(p->son).size())
					 {
						 q=new Node();
						 ans++;
						 q->name=s;
					     p->son.push_back(q);
					 }
			}
		}

		printf("Case #%d: %d\n", i, ans);
	}

	return 0;
}