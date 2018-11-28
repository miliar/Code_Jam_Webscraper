#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<string>
using namespace std;

string s[10001],q[10001];

int main()
{
	int i,j,k,tc,T,n,m;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d", &T);
	for(tc=1; tc<=T; tc++)
	{
		scanf("%d%d", &n,&m);
		int ans=0;
		int cs=0,cq=0;
		for(i=0; i<n; i++)
		{
			cin>>s[cs++];
		}
		for(i=0; i<m; i++)
			cin>>q[cq++];
		for(i=0; i<cq; i++)
		{
			int found=0;
			string ss="/";
				int pos=0;
				while(pos!=q[i].size())
				{
					//int pos=q[i].find('/',pos+1);
					string tmp1;
					found=0;
					for(k=pos+1; k<q[i].size(); k++)
						if(q[i][k]=='/')
							break;
					pos=k;
					string tmp=q[i].substr(0,pos);
					for(k=pos-1; k>=0; k--)
						if(q[i][k]=='/')
							break;
					if(k!=0)
						tmp1=q[i].substr(0,k);
					for(j=0; j<cs; j++)
					{
						if(s[j]==tmp1)
							found|=1;
						if(s[j]==tmp)
							found|=2;
					}
					if(!found)
					{
						if(k!=0)
						{
							s[cs++]=tmp1;
							ans++;
						}
						s[cs++]=tmp;
						ans++;
					}
					if(found==1)
					{
						s[cs++]=tmp;
						ans++;
					}
				}

		}
		printf("Case #%d: %d\n", tc,ans);
	}
	return 0;	
}

