#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

typedef struct dir
{
	string name;
	vector<dir*> child;
	dir* have(string name)
	{
		for(int i = 0;i < (int)child.size(); i++)
			if(name.compare(child[i]->name) == 0)
				return child[i];
			return NULL;
	}
} dir;

int n, m;
dir root;

int construct(string name)
{
	dir* cur = &root;
	int n;
	size_t i;
	name = name.substr(1);
	while((i = name.find_first_of('/')) != string::npos)
	{
		string dirname = name.substr(0, i);
		
		name = name.substr(i+1);
		dir* t = cur->have(dirname);
		
		if(t == NULL)
		{
			t = new dir;
			t->name = dirname;
			t->child = vector<dir*>();
			cur->child.push_back(t);
			n++;
		}
		cur = t;
	}
	dir* tt = cur->have(name);
	if(tt == NULL)
	{
		tt = new dir;
		tt->name = name;
		cur->child.push_back(tt);
		n++;
	}
	return n;
}

void deletee(dir* d, int rooot = 0)
{
	
	for(int i = 0; i < (int)d->child.size(); i++)
		deletee(d->child[i], 0);
	d->child.clear();
	if(rooot == 0 && d != &root)
	{
		//cerr << d->name << endl;
		delete d;
	}
}
int main()
{
	freopen("example.in.txt", "r", stdin);
	root.name = "/";
	int nbCases, c = 0;
	scanf("%d", &nbCases);
	while(c != nbCases)
	{
		
		scanf("%d%d", &n, &m);
		int res = 0;
		for(int i = 0; i < n; i++)
		{
			string b;
			cin >> b;
			res = construct(b);
		}
		
		res = 0;
		for(int i = 0; i <m; i++)
		{
			string b;
			cin >> b;
			res += construct(b);
		}
		printf("Case #%d: %d\n", ++c, res);
		deletee(&root, 1);
	}
	
	return 0;
}