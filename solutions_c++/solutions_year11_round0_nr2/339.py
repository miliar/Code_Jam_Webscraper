#include<iostream>
#include<stdio.h>
#include<string>
#include<string.h>
#include<vector>
#include<algorithm>

using namespace std;
vector<string>change;
vector<string>destroy;
int mark[110][110];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("temp.txt","w",stdout);
	int t,i,j,k,cas=1,n;
	cin>>t;
	string s;
	while(t--)
	{
		change.clear();
		destroy.clear();
		scanf("%d",&n);		
		while(n--)
		{
			cin>>s;
			change.push_back(s);
		}
		memset(mark,0,sizeof(mark));	
		scanf("%d",&n);		
		while(n--)
		{
			cin>>s;
			destroy.push_back(s);
			mark[s[0]-'A'][s[1]-'A']=1;
		}
		
		scanf("%d",&n);
		cin>>s;
		
		char ans[1010];
		int tail=0;
		for(i=0;i<(int)s.length();i++)
		{
			ans[tail++]=s[i];
			while(tail>=2)
			{
				for(j=0;j<(int)change.size();j++)
					if((ans[tail-2] == change[j][0] && ans[tail-1] == change[j][1])
					|| (ans[tail-2] == change[j][1] && ans[tail-1] == change[j][0]))
					{
						break;
					}
				if(j!=(int)change.size())
				{
					tail-=2;
					ans[tail++]=change[j][2];
				}
				else break;
			}
			for(j=0;j<tail;j++)
			{
				for(k=0;k<tail;k++)
				{
					if(mark[ans[j]-'A'][ans[k]-'A'])
						break;				
				}
				if(k<tail)
					break;
			}
			if(j<tail)
				tail=0;
		}
		printf("Case #%d: [",cas++);
		for(i=0;i<tail;i++)
		{
			if(i) printf(", ");
			printf("%c",ans[i]);
		}
		cout<<"]"<<endl;
	}
}