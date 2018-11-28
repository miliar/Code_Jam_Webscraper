#include<iostream>
#include<string>
#include<sstream>
#include<map>
#include<iomanip>
using namespace std;

int T,k;
typedef struct tree{string feature;tree *left,*right,*parent;double p;} *ptree;

ptree New()
{
	ptree x = new tree;
	x->feature = "";
	x->left = x->right = x->parent = NULL;
	x->p = 1.0;
	return x;
}

void Clear(ptree root)
{
	if(root == NULL) return;
	Clear(root->left);
	Clear(root->right);
	delete root;
}


string Tree;
char aux[1000];
int n;
ptree root;

void parse(const char *x)
{
	string aux = "";

	root = New();
	ptree cur = root;
	while(*x!='(') ++x;
	++x;
	while(*x!=0)
	{
		if(isdigit(*x))
		{
			aux = "";
			while(isdigit(*x) || *x=='.')
				aux += *x, ++x;
			istringstream sin(aux.c_str());
			sin>>cur->p;
		}
		else
			if(isalpha(*x))
			{
				aux = "";
				while(isalpha(*x))
					aux += *x, ++x;
				cur->feature = aux;
			}
			else
			{
				if(*x == '(')
					if(cur->left == NULL)
					{
						cur->left = New();
						cur->left->parent = cur;
						cur = cur->left;
					}
					else
					{
						cur->right = New();
						cur->right->parent = cur;
						cur = cur->right;
					}
				else
					if(*x==')')
						cur = cur->parent;
				++x;
			}
	}
}

map<string,bool> m;
string str;
int NR;

double cute(ptree root)
{
	if(root==NULL)
		return 1.0;
	double val = root->p;
	if(m[root->feature])
		val *= cute(root->left);
	else
		val *= cute(root->right);
	return val;
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	cin>>T;
	for(k=1;k<=T;++k)
	{
		cout<<"Case #"<<k<<":"<<endl;
		Tree = "";
		cin>>n;
		while(n--){scanf(" "); fgets(aux,999,stdin); Tree+=aux;}
		parse(Tree.c_str());

		cin>>NR;
		while(NR--)
		{
			m.clear();
			cin>>str;
			cin>>n;
			while(n--)
			{
				cin>>str;
				m[str]=1;
			}
			printf("%.7lf\n",cute(root));
		}
	}
	fclose(stdout);
	return 0;
}
