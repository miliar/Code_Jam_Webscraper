#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <memory.h>
using namespace std;
struct tree
{
	double pr;
	string a;
	tree *left, *rigth,*parent;
};
tree *el,*pp;
char s[20];
void READ()
{
	string a;
	char c;
	double prob;
	int i;
	scanf("%c",&c);
	while ((c!='(')&&(c!=')'))
		scanf("%c",&c);
	if (c=='(')
	{
		scanf("%lf%s",&prob,&s);
		a=string(s);
		el->pr=prob;
		if ((a[0]>=97)&&(a[0]<=122))
		{
			el->a=a;
			pp=new(tree);
			el->left=pp;
			pp->parent=el;
			pp->a="";
			pp->left=0;
			pp->pr=0;
			pp->rigth=0;
			el=pp;
		} else
		{
			el->a="";
			for (i=0;i<a.length();i++)
			{
				if (a[i]==')')
				{
					el=el->parent;

					if ((el!=0)&&(el->rigth==0))
					{
						pp=new(tree);
						el->rigth=pp;
						pp->parent=el;
						pp->a="";
						pp->left=0;
						pp->pr=0;
						pp->rigth=0;
						el=pp;
					}
				}
			}
		}
	} else
	if (c==')')
	{
		el=el->parent;
		if ((el!=0)&&(el->rigth==0))
		{
			pp=new(tree);
			el->rigth=pp;
			pp->parent=el;
			pp->a="";
			pp->left=0;
			pp->pr=0;
			pp->rigth=0;
			el=pp;
		}
	}
}
int main(void)
{
	vector<string> v;
	string a,b;
	tree *st;
	int n,i,j,kl,k,A,l,tru;
	double p;
	freopen("r2.in","r",stdin);
	freopen("r2.out","w",stdout);
	scanf("%d",&n);
	for (i=0;i<n;i++)
	{
		printf("Case #%d:\n",i+1);
		scanf("%d",&l);
		el=new(tree);
		el->a="";
		el->left=0;
		el->pr=0;
		el->rigth=0;
		el->parent=0;
		st=el;
		for (j=0;j<l;j++)
		{
			READ();
		}
		scanf("%d",&A);
		for (j=0;j<A;j++)
		{
			v.clear();
			scanf("%s",&s);
			a=string(s);
			scanf("%d",&kl);
			for (k=0;k<kl;k++)
			{
				scanf("%s",&s);
				b=string(s);
				v.push_back(b);
			}
			p=1;
			el=st;
			while (el->a!="")
			{
				p*=el->pr;
				tru=0;
				for (k=0;k<kl;k++)
					if (v[k]==el->a)
					{
						tru=1;
						el=el->left;
						break;
					}
				if (!tru)
					el=el->rigth;
			}
			p*=el->pr;
			printf("%.7lf\n",p);
		}
	}
	fclose(stdout);
	return 0;
}

			


