#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
#include <map>

using namespace std;

int main()
{
	int N,S,Q,t,i,j;
	scanf("%d",&N);
	map<string,int> ms;
	for(t=1;t<=N;t++)
	{
		ms.clear();
		scanf("%d",&S);
		char ch;
		ch=getchar();
		for(i=0;i<S;i++)
		{
			string name;
			ch=getchar();
			while(ch!='\n')
			{
				name+=ch;
				ch=getchar();
			}
			ms[name]=i;
		}
		scanf("%d",&Q);
		ch=getchar();
		int was[101]={0};
		int ans=0;
		int w=0;
		for(i=0;i<Q;i++)
		{
			string que;
			ch=getchar();
			while(ch!='\n')
			{
				que+=ch;
				ch=getchar();
			}
			if(was[ms[que]]==0)
			{
				was[ms[que]]=1;
				w++;
				if(w==S)
				{	
					ans++;
					for(j=0;j<S;j++)was[j]=0;
					was[ms[que]]=1;
					w=1;
				}
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}