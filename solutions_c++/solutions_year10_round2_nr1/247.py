#include <cstdio>
#include <cstring>
#include <map>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

map<string,int>	H;
int Tmp[1005],T[100005][1005],len,All,tot,N,M;
string s;
inline int Trie_Ins()
{
	int ret=0;
	for (int i=0,j=1;j<=len;i=T[i][Tmp[j++]])
	if (!T[i][Tmp[j]])	T[i][Tmp[j]]=++All,++ret;
	return ret;
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int Test;
	scanf("%d",&Test);
	for (int Te=1;Te<=Test;++Te)
	{
		scanf("%d%d",&N,&M);
		memset(T,0,sizeof(T)),All=0,tot=0;
		H.clear();
		for (int i=1;i<=N;++i)
		{
			cin>>s;s+='/';
			len=0;
			string tmp="";
			for (int j=1;j<s.size();++j)
			if (s[j]=='/')
			{
				if (!H[tmp])	H[tmp]=++tot;
				Tmp[++len]=H[tmp];
				tmp="";
			}
			else	tmp+=s[j];
			Trie_Ins();
		}
		int ret=0;
		for (int i=1;i<=M;++i)
		{
			cin>>s;s+='/';
			len=0;
			string tmp="";
			for (int j=1;j<s.size();++j)
			if (s[j]=='/')
			{
				if (!H[tmp])	H[tmp]=++tot;
				Tmp[++len]=H[tmp];
				tmp="";
			}
			else	tmp+=s[j];
			ret+=Trie_Ins();
		}
		printf("Case #%d: %d\n",Te,ret);
	}
	return 0;
}
