#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<memory.h>
using namespace std;

char n[2000008],m[2000008];
bool f[2000008];

int trans(char *a)
{
	int len=strlen(a);
	int sum=0;
	for(int i=0;i<len;i++)
	{
		sum=sum*10+a[i]-'0';
	}
	return sum;
}		

int main()
{
	int t;
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int i=1 ;i<=t; i++)
	{
		scanf("%s%s",&n,&m);
		//cout<<n<<" "<<m<<endl;
		int len=strlen(n);
		if(len<2)
		{
			printf("Case #%d: 0\n",i);
		}
		else
		{
			int b=trans(n),e=trans(m);
			//cout<<b<<" "<<e<<endl;
			int ans=0;
			for(int j=b;j<=e;j++)
			{
				char ttemp[10];
				itoa(j,ttemp,10);
				//cout<<"temp="<<ttemp<<endl;
				memset(f,0,sizeof(f));
				for(int k=0;k<len;k++)
				{
					int l;
					int ntemp=0;
					for(l=0;l<len;l++)
					{
						ntemp=ntemp*10+ttemp[(k+l)%len]-'0';
					}
					//cout<<"trans="<<ntemp<<endl;
					if(f[ntemp]==0&&ntemp>=b&&ntemp<=e&&ntemp>j)
					{
						f[ntemp]=1;
						//cout<<f[ntemp];
						//cout<<j<<" "<<ntemp<<endl;
						ans++;
					}
				}
			}
			printf("Case #%d: %d\n",i,ans);
		}
	}
	return 0;
}
