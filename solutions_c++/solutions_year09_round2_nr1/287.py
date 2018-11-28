#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
using namespace std;
#define PI 3.14159265358979323846264338327950288
#define SIZE 200

char in[SIZE];
string str;
string name;
int si;
struct Node
{
	double p;
	string fea;
	Node *lcd,*rcd;
};

void gotoP()
{
	while(str[si] != '.') si++;
}
void jumpW()
{
	while(str[si] == ' ') si++;
}
set<string> st;
Node * create()
{
	while(str[si] != '(') si++;
	Node *tree = new Node;
	tree->lcd = tree->rcd = NULL;
	gotoP();
	double tp = str[si-1]-'0';
	double base = 10;
	int i;
	si++;
	while(str[si] >= '0' && str[si] <= '9')
	{
		tp += (str[si++]-'0')/base;
		base *=10;
	}
	tree->p = tp;
	jumpW();
	if(str[si] == ')')
		return tree;
	else
	{
		i = 0;
		while(str[si] >= 'a' && str[si] <= 'z')
			in[i++] = str[si++];
		in[i] = '\0';
		tree->fea = in;
		tree->lcd = create();
		tree->rcd = create();
		while(str[si] != ')') si++; 
	}
	return tree;
}
double ans;
void find(Node *tree)
{
	ans *= tree->p;
	if(tree->lcd != NULL)
	{
		if(st.find(tree->fea) != st.end())
			find(tree->lcd);
		else find(tree->rcd);
	}
}
int main()
{
	freopen("D:\\A-large.in","r",stdin);
	freopen("D:\\A-large.out","w",stdout);
	int T,no = 0,L,i,j,A,m;
	Node *tree;
	scanf("%d",&T);
	while(T--)
	{
		no++;
		scanf("%d",&L);
		str = "";
		gets(in);
		while(L--)
		{
			gets(in);
			str += in;
			str += " ";
		}
		L = str.length();
		for(i = 0; i < L; i++)
		{
			if(str[i] == '\n' || str[i] == '\t')
				str[i] = ' ';
		}
		si = 0;	
		tree = create();
		scanf("%d",&A);
		printf("Case #%d:\n",no);
		for(i = 0; i < A; i++)
		{
			scanf("%s",in);
			scanf("%d",&m);
			st.clear();
			for(j = 0; j < m; j++)
			{
				scanf("%s",in);
				name = in;
				st.insert(name);
			}
			ans = 1;
			find(tree);
			printf("%.7lf\n",ans);
		}
	}
	return 0;
}