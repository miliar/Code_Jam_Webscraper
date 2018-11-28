#include<iostream>
#include<algorithm>
#include<map>
#include<string>
#include<vector>
using namespace std;
const int MAX=60;

int N,M;
string st,sy;
char s[1100];
map<string,int> my;
map<string,int>::iterator it;
int a[400][200];
void init()
{
	my.clear();
	int i;
	for(i=1;i<=300;i++) a[i][0]=0;
}
int main()
{
	freopen("F:\\A-large.in","r",stdin);
	freopen("F:\\A-large.out","w",stdout);
	int i,j,T;scanf("%d",&T);
	int CN=0;
	while(T--)
	{
		scanf("%d%d",&N,&M);
		init();
		int cnt=0,res=0;
		for(i=1;i<=N;i++)
		{
			scanf("%s",s);
			j=1;
			while(s[j]!='\0')
			{
				if(s[j]=='/') j++;
				st="";
				while(s[j]!='/'&&s[j]!='\0')
				{
					st=st+s[j];
					j++;
				}
				it=my.find(st);
				if(it==my.end())
				{
					my[st]=++cnt;
					a[i][++a[i][0]]=cnt;
				}
				else
				{
					a[i][++a[i][0]]=it->second;
				}
			}
		}
		for(i=N+1;i<=M+N;i++)
		{
			scanf("%s",s);
			j=1;
			while(s[j]!='\0')
			{
				if(s[j]=='/') j++;
				st="";
				while(s[j]!='/'&&s[j]!='\0')
				{
					st=st+s[j];
					j++;
				}
				it=my.find(st);
				if(it==my.end())
				{
					my[st]=++cnt;
					a[i][++a[i][0]]=cnt;
				}
				else
				{
					a[i][++a[i][0]]=it->second;
				}
			}
			int k,ans=0;
			for(j=1;j<i;j++)
			{ 
				int tt=0;
				for(k=1;k<=a[j][0]&&k<=a[i][0]&&a[j][k]==a[i][k];k++) tt++;
				if(ans<tt) ans=tt;
			}
			res+=a[i][0]-ans;
		}
		printf("Case #%d: %d\n",++CN,res);
		
	}
	//system("pause");
	return 0;
}
