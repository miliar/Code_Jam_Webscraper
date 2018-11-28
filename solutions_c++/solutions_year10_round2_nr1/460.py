#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <iostream>

using namespace std;


class TDir
{
	public:
		TDir()
		{
			memset(Name,0,sizeof(Name));
			memset(Son,NULL,sizeof(Son));
			Tot=0;
		}	
		char Name[256];
		TDir *Son[1000];
		int Tot;
}	;



int AddNode(TDir * root,char Dir[])
{
	if (Dir[0]==0)	return 0;
	int p=0;
	char Name[200];
	
	memset(Name,0,sizeof(Name));
	while (Dir[p]!='/'&&Dir[p]!=0)
		++p;
	--p;
	memcpy(Name,Dir,(p+1));
	for (int i=1;i<=root->Tot;++i)
	if (strcmp(root->Son[i]->Name,Name)==0)
		return AddNode(root->Son[i],&Dir[p+2]);
	root->Son[++(root->Tot)]=new(TDir);
	strcpy(root->Son[(root->Tot)]->Name,Name);
	return AddNode(root->Son[(root->Tot)],&Dir[p+2])+1;
}

void Solve(int KKKKK)
{
	TDir Root;
	memset(&Root,0,sizeof(Root));
	int N,M;
	char Dir[200];
	scanf("%d%d",&N,&M);
	for (int i=1;i<=N;++i)
	{
	memset(Dir,0,sizeof(Dir));
		scanf("%s",Dir);
		AddNode(&Root,Dir+1);
	}
	int Ans=0;
	for (int i=1;i<=M;++i)
	{
	memset(Dir,0,sizeof(Dir));
		scanf("%s",Dir);
		Ans+=AddNode(&Root,Dir+1);
	}
	printf("Case #%d: %d\n",KKKKK,Ans);
}	
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int Test;
	scanf("%d",&Test);
	for (int i=1;i<=Test;++i)
		Solve(i);
	
	return 0;
}