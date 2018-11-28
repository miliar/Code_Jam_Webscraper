#include<set>
#include<iostream>
using namespace std;
#define MAXL 110
#define MAXS 110
#define MAXQ 1010
#define P 1250235352
bool dbg=0;

int engines[MAXS];
set<int> used;
int queries[MAXQ];
int s,q;
char str[MAXL];

int hash()
{
    long long int h=0;
    for(int i=0;str[i]!='\0';i++)
    {
	h<<=8;
	h+=str[i];
	h%=P;
    }
    return (int)h;
}

void readCase()
{
    scanf("%d",&s);
    if(dbg)printf("s:%d\n",s);
    cin.getline(str,MAXL);
    for(int i=0;i<s;i++)
    {
	cin.getline(str,MAXL);
	engines[i]=hash();
	if(dbg)printf("%d:(%s) %d\n",i,str,engines[i]);
    }
    scanf("%d",&q);
    cin.getline(str,MAXL);
    if(dbg)printf("q:%d\n",q);
    for(int i=0;i<q;i++)
    {
	cin.getline(str,MAXL);
	queries[i]=hash();
	if(dbg)printf("%d:(%s) %d\n",i,str,queries[i]);
    }
}

void solveCase(int cas)
{
    used.clear();
    int no=0;
    int res=0;
    for(int i=q-1;i>=0;i--)
    {
	if(used.find(queries[i])==used.end())
	{
	    no++;
	    used.insert(queries[i]);
	    if(no==s)
	    {
		res++;
		used.clear();
		used.insert(queries[i]);
		no=1;
	    }
	}
    }
    printf("Case #%d: %d\n",cas,res);
}
int main()
{
    int n;
    scanf("%d",&n);
    if(dbg)printf("n:%d\n",n);
    for(int i=0;i<n;i++)
    {
	readCase();
	solveCase(i+1);
    }
    return 0;
}

