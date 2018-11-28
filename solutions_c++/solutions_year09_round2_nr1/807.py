#include<iostream>
#include<string.h>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

#define  maxn 1000000

char str[maxn];

struct node
{
	string name;
	double p;
	int flag;

}a[10000];
void build(int x,int y,int k)
{
	int i;
	a[k].flag=1;
	for(i=x+1;i<y;i++)
	{
		if(str[i]=='(') 
		{
			a[k].flag=0;
		}
	}
	if(a[k].flag)
	{
		a[k].p=0.0;
		string tmp="";
		for(i=x+1;i<y;i++)
		{
			tmp=tmp+str[i];
		}
		stringstream sout(tmp);
		sout>>a[k].p;
	}
	else
	{
		
		string tmp="";
		for(i=x+1;i<y;i++)
		{
			tmp=tmp+str[i];
		}
		stringstream sout(tmp);
		sout>>a[k].p>>a[k].name;
		int x1,y1,x2,y2;
		for(x1=x+1;x1<y;x1++)
		{
			if(str[x1]=='(') break;
		}
		int cnt=1;
		for(y1=x1+1;y1<y;y1++)
		{
			if(str[y1]=='(') cnt++;
			if(str[y1]==')') cnt--;
			if(cnt==0) break;
		}

		for(x2=y1+1;x2<y;x2++)
		{
			if(str[x2]=='(')break;
		}
		cnt=1;
		for(y2=x2+1;y2<y;y2++)
		{
			if(str[y2]=='(') cnt++;
			if(str[y2]==')') cnt--;
			if(cnt==0) break;
		}
		build(x1,y1,k*2);
		build(x2,y2,k*2+1);
		
	}
}


vector<string> pets;
double ans;
void f(int k)
{
	ans*=a[k].p;
	if(a[k].flag) return;
	else
	{
		int i;
		for(i=0;i<pets.size();i++)
		{
			if(pets[i]==a[k].name) 
			{
				break;
			}
		}
		int size=pets.size();
		if(i==pets.size()) f(k*2+1);
		else f(k*2);
	}
}
int main()
{
	int t;
	int L;
	int i;
	char tmp[1000];
	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		scanf("%d",&L);
		gets(str);
		str[0]=0;
		for(i=0;i<L;i++)
		{
			int len=strlen(str);
			str[len]=' ';
			str[len+1]=0;
			gets(tmp);
			strcat(str,tmp);
		}
		int x,y;
		int len=strlen(str);
		for(x=0;x<len;x++)
		{
			if(str[x]=='(') break;
		}
		int cnt=1;
		for(y=x+1;y<len;y++)
		{
			if(str[y]=='(') cnt++;
			if(str[y]==')') cnt--;
			if(cnt==0) break;
		}
		build(x,y,1);
		
		int m;
		printf("Case #%d:\n",cas);
		scanf("%d",&m);
		for(i=0;i<m;i++)
		{
			scanf("%s",tmp);
			int n;
			scanf("%d",&n);
			pets.clear();
			for(int j=0;j<n;j++)
			{
				scanf("%s",tmp);
				string stmp(tmp);
				pets.push_back(stmp);
			}	
			ans=1.0;
			
			f(1);
			printf("%.7lf\n",ans);
		}

		
	}
	return 0;
}