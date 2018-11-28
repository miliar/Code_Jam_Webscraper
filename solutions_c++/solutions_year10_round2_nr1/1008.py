#pragma warning(disable: 4786)
#include<stdio.h>
#include<string>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<map>
#include<iostream>
#include<set>
#include<math.h>
#include<queue>
using namespace std;
		


int main()	
{			
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	
	//freopen("out.txt","w",stdout);
	int T,cs,m,n,i,j,len;
	scanf("%d",&T);
	char in[200],now[200],next[200];

	for(cs=1;cs<=T;cs++)
	{
		char *p;
		map<string,bool> mp;
		scanf("%d %d",&n,&m);
		getchar();
		for(i=0;i<n;i++)
		{
			gets(in);
			len=strlen(in);
			for(j=0;j<len;j++)
				if(in[j]=='/')
					in[j]=' ';
			p=in;
			strcpy(now,"");
			while(*p)
			{
				while(*p==' ')p++;
				strcat(now,"-");
				sscanf(p,"%s",next);
				p+=strlen(next);
				strcat(now,next);
				mp[now]=1;
				while(*p==' ')p++;
			}
		}

		int ans=0;
		for(i=0;i<m;i++)
		{
			gets(in);
			len=strlen(in);
			for(j=0;j<len;j++)
				if(in[j]=='/')
					in[j]=' ';
			p=in;
			strcpy(now,"");
			while(*p)
			{
				while(*p==' ')p++;
				strcat(now,"-");
				sscanf(p,"%s",next);
				p+=strlen(next);
				strcat(now,next);
				if(!mp[now])
				{
					ans++;
					mp[now]=1;
				}
				while(*p==' ')p++;
			}
		}

		printf("Case #%d: %d\n",cs,ans);
	}
  	return 0;
}			