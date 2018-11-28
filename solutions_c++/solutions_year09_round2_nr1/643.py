#include <iostream>

using namespace std;

struct tnode{
	char name[15];
	int lch, rch;
	double p;
};
struct tanimal{
	string name;
	int n;
	char f[100][15];
};
tnode a[1000];
tanimal animal[100];
char token[1000][100];
char delim[10]="() \n";
int n, tp, ap;
int flag;

int build()
{
	if (flag+1==tp || token[flag+1][0]=='0')
	{
		int id = ap++;
		a[id].lch = a[id].rch = -1;
		a[id].p = atof(token[flag++]);
		return id;
	}
	else {
		int id = ap++;
		a[id].p = atof(token[flag++]);
		strcpy(a[id].name,token[flag++]);
		a[id].lch=build();
		a[id].rch = build();
		return id;
	}
}
void init()
{
	int l;
	cin>>l;
	char s[100000];
	cin.getline(s,10000);
	int len = 0;
	for (int i=0;i<l;i++)
	{
		cin.getline(s+len,1000);
		len = strlen(s);
	}
	tp = 0;
	char* temp= strtok(s,delim);
	while (temp!=NULL)
	{
		strcpy(token[tp++],temp);
		temp = strtok(NULL,delim);
	}
	ap = 0;
	flag = 0;
	build();
	cin>>n;
	cin.getline(s,100);
	for (int i=0;i<n;i++)
	{
		cin>>animal[i].name>>animal[i].n;
		for (int j=0; j<animal[i].n; j++)
			cin>>animal[i].f[j];
	}
}
bool hasFeature(tanimal &a, char s[])
{
	for (int i=0;i<a.n;i++)
		if (strcmp(a.f[i],s)==0)
			return true;
	return false;
}
double calc(int x)
{     
	double r = a[x].p;
    if (a[x].lch>=0) //has feature
    {
		if (hasFeature(animal[flag],a[x].name))
			r*=calc(a[x].lch);
		else r*=calc(a[x].rch);		
    }
	return r;
}
int main()
{
	int t;
	cin>>t;
	for (int i=0;i<t;i++)
	{
		init();
		cout<<"Case #"<<i+1<<":\n";
		for (flag=0;flag<n;flag++)
		    printf("%.7lf\n",calc(0));
	}
}
