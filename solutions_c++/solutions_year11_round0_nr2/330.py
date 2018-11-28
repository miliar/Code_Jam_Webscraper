#include<cstdio>
#include<iostream>
#include<cmath>
#include<climits>
#include<string>
#include<cstring>
#include<vector>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++)
	{
		int n;
		char with[26][26];
		int oppose[26];
		memset(with,-1,sizeof with);
		memset(oppose,0,sizeof oppose);
		string st;
		scanf("%d",&n);
		while(n--)
		{
			cin>>st;
			with[st[0]-'A'][st[1]-'A']=with[st[1]-'A'][st[0]-'A']=st[2];
		}
		scanf("%d",&n);
		while(n--)
		{
			cin>>st;
			oppose[st[0]-'A']|=(1<<(st[1]-'A'));
			oppose[st[1]-'A']|=(1<<(st[0]-'A'));
		}
		int set=0;
		cin>>n;
		cin>>st;
		int len=st.length();
		vector<char> vc;
		vc.push_back(st[0]);
		for(int i=1;i<len;i++)
		{
			int p=vc[vc.size()-1]-'A';
			char last;
			if(with[p][st[i]-'A']!=-1)
			{
				vc.pop_back();
				last=with[p][st[i]-'A'];
			}
			else
				last=st[i];
			for(int j=0;j<vc.size();j++)
				if((oppose[last-'A']>>(vc[j]-'A'))%2!=0)
				{
					vc.clear();
					i++;
					if(i<len)
						last=st[i];
					break;
				}
			if(i<len)
			vc.push_back(last);
		}
		printf("Case #%d: [",tc);
		if(vc.size()>0)
		{
			for(int i=0;i<vc.size()-1;i++)
				printf("%c, ",vc[i]);
			printf("%c]\n",vc[vc.size()-1]);
		}
		else
			printf("]\n");
	}
	return 0;
}
