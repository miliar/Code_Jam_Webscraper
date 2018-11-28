#include<iostream>
#include<string>
#include<map>
using namespace std;
#define  maxn  1010

bool  visit[maxn];
map<string,int> mp;
int main()
{
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);
	int i,l,Ncase; cin>>Ncase;
	string temp;

	int N,M,num,answer;
	for(l=1;l<=Ncase;l++)
	{
		scanf("%d",&N);getchar();
		for(i=1;i<=N;i++)getline(cin,temp),mp[temp]=i;

		scanf("%d",&M);getchar();
		memset(visit,0,sizeof(visit));
		for(answer=num=0,i=1;i<=M;i++)
		{
			getline(cin,temp);
			if(!visit[mp[temp]])
			{
				visit[mp[temp]]=true;
				num++;
			}
			if(num==N)
			{
				memset(visit,0,sizeof(visit));
				num=1;answer++;visit[mp[temp]]=true;
			}
		}
		printf("Case #%d: %d\n",l,answer);
		mp.clear();
	}

	return 0;
}
