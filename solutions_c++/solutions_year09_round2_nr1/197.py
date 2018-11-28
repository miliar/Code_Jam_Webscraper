//#include <string>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void eat (char c)
{
	int x;
	do
	{
		x=getc(stdin);
		if (x==EOF) return; 
	}while (x!=c);
}
class animal
{
	int id;
public:
	int traits;
	char **tstr;
	
	animal()
	{
		tstr=NULL;
	}
	
	void setTrait(int i)
	{
		traits = i;
		id=0;
		int j;
		if (i>0)
		{
			tstr = (char**)malloc(sizeof(char*) * (i+1)); // new char* [i];
			for (j=0; j<i; ++j)
			{
				tstr[j]=NULL;
			}
		}
	}
	
	void addTrait(char *buf)
	{
		if (id>=traits) abort();
		tstr[id] = (char*) malloc((strlen(buf)+5)*sizeof(char));// new char[strlen(buf)];
		strcpy(tstr[id], buf);
		++id; 
	}
	
	~animal()
	{
		if (tstr)
		{
			for (int i=0; i<traits; ++i)
			{
				if (tstr[i])
					free(tstr[i]);//delete (tstr[i]);
			}
			free( tstr);
		}
	}
};

class node
{
public:
	double weight;
	node *left, *right;
	char trait[20];
	
	void build(void)
	{
		char buf[200];
		eat('(');
		int res=scanf ("%lf %[a-z]", &weight, buf);
		if (buf[0]==')' || res==1) {trait[0]='\0'; left=NULL; right=NULL; eat(')'); return;}
		
		strcpy(trait, buf);
		left = new node;
		right = new node;
		left->build();
		right->build();
		eat(')');
	}
	
	node()
	{
		left=NULL; right=NULL;
	}
	~node()
	{
		if (left)
			delete left;
		if (right)
			delete right;
	}
	
	double eval (animal &a)
	{
		double ret=weight;
		
		if (trait[0])
		{
			int i;
			for (i=0; i<a.traits; ++i)
			{
				if (!strcmp(trait, a.tstr[i]))
					break;
			}
			if (i<a.traits)
			{
				ret*=left->eval(a);
			} else
			{
				ret*=right->eval(a); 
			}
		}
		
		return ret; 
	}
	
};


int main (void)
{
	int n,c;
	int l;
	int anim;
	int cnt;
	char buf[50];
	scanf ("%d", &n);
	for (c=1; c<=n; ++c)
	{
		node root;
		scanf ("%d", &l);
		root.build();
		
		printf ("Case #%d:\n", c);
		scanf ("%d", &anim);
		while (anim-->0)
		{
			scanf ("%s", buf);
			scanf ("%d", &cnt);
			animal test;
			test.setTrait(cnt);
			while (cnt-->0)
			{
				scanf ("%s", buf);
				test.addTrait(buf);
			}
			printf ("%.8lf\n", root.eval(test));
		}
		
		
		
	}
	return 0; 
}