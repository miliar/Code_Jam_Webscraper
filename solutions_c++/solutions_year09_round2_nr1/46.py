#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <vector>

using namespace std;

class Node 
{
public:
	long double p;
	string s;
	Node *l, *r;

	void Free()
	{
		if (l) 
		{	
			l->Free();
			delete(l);
		}
		if (r) 
		{
			r->Free();
			delete(r);
		}
	}
};

int l, a;

Node *root;


void Parse(Node *&v)
{
	char c;

	v = new (Node);
	cin >> (v->p);
	v->l = v->r = NULL;
	v->s = "";
	
//	cerr << v->p << " ";

	c = getchar();
	while (c == ' ' || c == '\n' || c == '\t')
		c = getchar();
   	
//   	cerr << c;

   	if (c == ')') return;
    while (c != ' ' && c != '\t' && c != '\n' && c != '(')
    {
	    v->s += c;
	    c = getchar();
    }


//	cerr << "parse " << v->s << "\n";
	
   	while (c != '(')
   		c = getchar();

   	Parse(v->l);
   
	c = getchar();
   	while (c != '(')
   		c = getchar();
	Parse(v->r);

	c = getchar();
	while (c != ')')
		c = getchar();
}

void Load()
{
	cin >> l;
	char c = getchar();
	while (c != '(')
		c = getchar(); 
	Parse(root);
}

set<string> feat;


long double Calc(Node *v)
{
//	cerr << "calc " << v->s << "\n";
	if (v->s == "")
		return v->p;
   	long double res;
   	if (feat.find(v->s) != feat.end())
   		res = Calc(v->l);
   	else
   		res = Calc(v->r);

   	return res * v->p;
}


void Solve()
{
	int i, k, j;
	cin >> a;
	string s;
	for (i = 0; i < a; i++)
	{
		cin >> s;
		feat.clear();
		cin >> k;
		for (j = 0; j < k; j++)
		{
			cin >> s;
			feat.insert(s);
		}
		cout << Calc(root) << "\n";
	}


	root->Free();
	delete(root);

}

int main()
{
	cout.setf(ios::fixed | ios::showpoint);
	cout.precision(7);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ":\n";
		Solve();
	}
	return 0;
}
