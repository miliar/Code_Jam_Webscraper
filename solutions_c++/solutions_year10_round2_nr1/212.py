#include<iostream>
#include<string>
#include<map>
using namespace std;
const int MAXN=100010;
char buf[MAXN];
char str[MAXN];
struct node
{
    map<string,int> dic;
}tire[MAXN];
int COUNT;
int insert(int root,string str)
{
    if(tire[root].dic.count(str)==0)
    {
        tire[COUNT].dic.clear();
        tire[root].dic[str]=COUNT++;
    }
    return tire[root].dic[str];
}
void auto_insert()
{
    int root=0,p=0,i;
    while(buf[p]=='/')
    {
		i=0;
		while(isalnum(buf[++p]))
		{
			str[i++]=buf[p];
		}
		str[i]=0;
        root=insert(root,string(str));
    }
}
int work()
{
    int i,n,m,cm;
    scanf("%d%d",&n,&m);
    COUNT=1;
    tire[0].dic.clear();
    while(n--)
    {
        scanf("%s",buf);
        auto_insert();
    }
    cm=COUNT;
    while(m--)
    {
        scanf("%s",buf);
        auto_insert();
    }
    return COUNT-cm;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cas;
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        printf("Case #%d: %d\n",cas,work());
    }
    return 0;
}
