#include<iostream>
#include<string>
#include<map>
#include<queue>
#include<vector>
using namespace std;
vector<string>words;
bool hash[50][50];
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int L,D,N;
	int i,j,k;
	string str;
	scanf("%d%d%d",&L,&D,&N);
	words.clear();
	for(int i=0;i<D;i++)
	{
		cin>>str;
		words.push_back(str);
	}
	for(i=1;i<=N;i++)
	{
		cin>>str;
		int cnt=0,ans=0;
		memset(hash,false,sizeof(hash));
		for(j=0;j<str.size();j++)
		{
			if(str[j]=='(')
			{
				j++;
				while(str[j]!=')')
				{
					hash[cnt][str[j]]=true;
					j++;
					
				}
			}
			else hash[cnt][str[j]]=true;
			cnt++;
		}
		for(j=0;j<words.size();j++)
		{
			for(k=0;k<words[j].size();k++)
				if(!hash[k][words[j][k]])
					break;
			if(k>=words[j].size())ans++;
		}
		printf("Case #%d: %d\n",i,ans);
	}
}