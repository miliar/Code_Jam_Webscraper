#include<iostream>
#include<string>
#include<algorithm>
using namespace std;



struct node
{
	double p;
	string s;
	node *left;
	node *right;
};

int index;
string txt;

void read( node *t )
{
	t->p=0;
	double tt=10;
	while(!isdigit(txt[index]))
		++index;
	while(isdigit(txt[index]))
	{
		t->p*=10;
		t->p+=(double)(txt[index++]-'0');
	}
	if(txt[index]=='.')
	{
		++index;
		while(isdigit(txt[index]))
		{
			t->p+=((double)(txt[index++]-'0'))/tt;
			tt*=10;
		}
	}
	while(!isalpha(txt[index]) && txt[index]!=')' && txt[index]!=')')
		++index;
	while(isalpha(txt[index]))
		t->s+=txt[index++];
	if(txt[index]==')')
		return;
	t->left=new node;
	t->right=new node;
	read(t->left);
	read(t->right);
}

string a[1000];
int n;
node *head;
double p;

void find(node *t)
{
	p*=t->p;
	if(t->s=="")
		return;
	if(binary_search(a,a+n,t->s))
		find(t->left);
	else
		find(t->right);
}

void solve()
{
	
	cin>>n;
	string s;
	int kk;
	char aa[1000];
	txt="";
	int i,j;
	char cccc;
	cin.get(cccc);
	for(i=0;i<n;++i)
	{
		cin.getline(aa,100,'\n');
		kk=strlen(aa);
		for(j=0;j<kk;++j)
			txt+=aa[j];
	}
	int k;
	cin>>k;
	head=new node;
	index=0;
	read(head);
	for(i=0;i<k;++i)
	{
		cin>>s;
		cin>>n;
		for(j=0;j<n;++j)
			cin>>a[j];
		sort(a,a+n);
		p=1;
		find(head);
		printf("%.7lf\n",p);
	}
}

int main()
{
	freopen("output.txt","w",stdout);
	int ttt;
	int i;
	cin>>ttt;
	for(i=0;i<ttt;++i)
	{
		cout<<"Case #"<<i+1<<": \n";
		solve();
	}
}