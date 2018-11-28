#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class dtree
{
public:
	double weight;
	bool leaf;
	string feature;
	dtree* son[2];	

	dtree(){};
	~dtree()
	 {
		if (!leaf)
		{
			delete son[0];
			delete son[1];
		}
	}
	void xscanf()
	{
		char c;
		char t[100];
		do 
		{
			c = getc(stdin);
		} while (c!='(');
		scanf("%lf",&weight);
		do 
		{
			c = getc(stdin);
		} while (c==' ' || c=='\n');
		if (c == ')')
		{
			leaf = true;
			return;
		}
		leaf = false;
		int i;
		for (i=0; c>='a' && c<='z'; i++)
		{
			t[i] = c;
			c = getc(stdin);
		}
		t[i] = 0;
		feature = t;
		son[0] = new dtree;
		son[1] = new dtree;
		son[0]->xscanf();
		son[1]->xscanf();
		do 
		{
			c = getc(stdin);
		} while (c!=')');

	}
	double prob(vector<string> &vs)

	{
		if (leaf)
			return weight;	

		for(unsigned int i=0; i<vs.size(); i++)
		{
			if(vs[i]==feature)
			{
				return weight*son[0]->prob(vs);
			}
		}
		return weight*son[1]->prob(vs);
	}
};

int main()
{
	int t;
	scanf("%d",&t);

	for(int i=0; i<t; i++)
	{
		printf("Case #%d:\n",i+1);
		int l;
		scanf("%d",&l);
		dtree root;
		root.xscanf();
		int a;
		scanf("%d",&a);
		for(int j=0; j<a; j++)
		{
			char animal[100];
			int n;
			scanf("%s %d",animal,&n);
			vector<string> features;
			for (int k=0; k<n; k++)
			{
				char feature[100];
				scanf("%s",feature);
				features.push_back(feature);
			}
			printf("%.7lf\n",root.prob(features));
		}
	}

	return 0;
}
