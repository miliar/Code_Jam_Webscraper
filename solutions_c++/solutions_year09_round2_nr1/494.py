#include "iostream"
#include "algorithm"
#include "cstring"
#include "string"
#include "stack"
#include "queue"
#include "set"
#include "map"
#define N 101
#define M 21
using namespace std;
char x[N];
int cnt,l,i,animal;
map<string,set<string>> yy;
bool isnumber(char a)
{
	switch (a)
	{
		case '0':case '1':case '2':case '3':case '4':case '5':
		case '6':case '7':case '8':case '9':case '.':
			return true;
		default:
			return false;
	}
}
struct node {
	char feature[M];
	double p;
	node *left,*right;
	node(){
		feature[0]=0;
		p=0;
		left=NULL;right=NULL;
	}
};
struct tree{
	node *root;
	node *current;
	int n;
	void add(node &now);
	double qsearch(string ani);
	void clear();
}T;
void tree::add(node &now){
	if(x[i]!='\0'){
		n++;
		while(!isnumber(x[i])&&x[i]!='\0')
		{
			i++;
		}
		char w[N];
		int j=0;
		while(isnumber(x[i])&&x[i]!='\0')
		{
			w[j++]=x[i++];
		}
		w[j]='\0';
		now.p=atof(w);
		while(x[i]==' '&&x[i]!='\0')
		{
			i++;
		}
		if(x[i]=='\0'&&cnt<l)
		{
			gets(x);
			cnt++;
			i=0;
			add(now);
		}
		else if(x[i]!=')'){
			j=0;
			while(x[i]!=')'&&x[i]!='\0')
			{
				now.feature[j++]=x[i++];
			}
			now.feature[j]='\0';
			now.left=new node();
			add(*now.left);
			now.right=new node();
			add(*now.right);
		}
	}
	else
	{
		if(cnt<l)
		{
			gets(x);
			cnt++;
			i=0;
			add(now);
		}
	}
}
void tree::clear(){
	root=new node();
	current=NULL;
	n=0;
	i=0;
	x[0]='\0';
	cnt=0;
}

double tree::qsearch(string ani){
	queue<node*> q;
	node *p;
	int j,k;
	double ans=1;
	q.push(T.root);
	while(!q.empty()){
		p=q.front();
		q.pop();
		ans*=p->p;
		string f=p->feature;
		set<string> &ss=yy[ani];
		if(p->feature[0]=='\0')
			return ans;
		if(ss.find(f)==ss.end())
			q.push(p->right);
		else
			q.push(p->left);
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int ncase=1;ncase<=t;ncase++)
	{
		printf("Case #%d:\n",ncase);
		scanf("%d\n",&l);
		T.clear();
		T.add(*T.root);
		while(cnt<l)
		{
			gets(x);
			cnt++;
		}
		yy.clear();
		scanf("%d\n",&animal);
		for(int j=0;j<animal;j++)
		{
			string name,f;
			int n;
			cin>>name>>n;
			set<string> &ss=yy[name];
			for(int k=0;k<n;k++)
			{
				cin>>f;
				ss.insert(f);
			}
			printf("%.7lf\n",T.qsearch(name));
		}
	}
	return 0;
}