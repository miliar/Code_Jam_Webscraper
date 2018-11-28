#include <iostream>
#include <cstring>
using namespace std;

struct node
{
	char ft[100];
	double v;
	node * ls,* rs;
}* root;
char f[200][100];
int k;

double getval(char & c)
{

	cin>>c;
	double k,j;
	j=1;
	k=0;
	while('0'<=c && c<='9')
	{
		k=k*10+c-'0';
		cin>>c;
	}
	if (c=='.')
	{
		cin>>c;
		while ('0'<=c && c<='9')
		{
			j=j/10;
			k=k+(c-'0')*j;
			cin>>c;
		}
	}
	return k;
};
void build(node *  & root)
{
	char c;
	root=new node;
	root->v=getval(c);
	if (c==')')
	{
		root->ft[0]=0;
		root->ls=NULL;
		root->rs=NULL;
		return;
	}
	else 
	{
		int i;
		i=1;
		root->ft[0]=c;
		do
		{
			cin>>c;
			if ('a'<=c && c<='z' || 'A'<=c && c<='Z')
			{
				root->ft[i]=c;
				i++;
			} else break;
		} while (true);
		root->ft[i]=0;
		while(c!='('){cin>>c;};
		build(root->ls);
		do{cin>>c;} while(c!='(');
		build(root->rs);
	}
	do{cin>>c;} while(c!=')');
}
void init()
{
	int l;
	cin>>l;
	char c;
	do 
	{cin>>c;} 
	while (c!='(');
	build(root);
}

double search(node * g)
{
	if (g->ft[0]==0) return g->v;
	int i;
	for (i=1;i<=k;i++)
		if (strcmp(f[i],g->ft)==0)
		{
			return g->v*search(g->ls);
		}
	return g->v*search(g->rs);
}
void make()
{
	int n,i,j;
	cin>>n;
	char name[500];
	for (i=1;i<=n;i++)
	{
		cin>>name;
		cin>>k;
		for (j=1;j<=k;j++) cin>>f[j];
		printf("%.7lf\n",search(root));
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cs;
	int i;
	cin>>cs;
	for (i=1;i<=cs;i++)
	{
		init();
		cout<<"Case #"<<i<<":"<<endl;
		make();
	}
	return 0;
}