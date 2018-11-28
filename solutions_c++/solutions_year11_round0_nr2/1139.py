#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <map>
using namespace std;

bool vst1[30],vst2[30];
int G[30][30];
bool del[30][30];

int main()
{
	freopen("d://B-small-attempt3.in","r",stdin);
	freopen("d://lowesy.txt","w",stdout);
	int _,cases=1;
	scanf("%d",&_);
	while(_--)
	{
		int C,D,N;
		char str[1005];
		scanf("%d",&C);
		memset(vst1,0,sizeof(vst1));
		memset(vst2,0,sizeof(vst2));
		memset(G,0xff,sizeof(G));
		memset(del,0,sizeof(del));
		for(int i=0;i<C;i++)
		{
			scanf("%s",str);
			vst1[str[0]-'A']=true;
			vst1[str[1]-'A']=true;
			G[str[0]-'A'][str[1]-'A']=G[str[1]-'A'][str[0]-'A']=str[2]-'A';
			
			if(str[2]=='A'||str[2]=='S'||str[2]=='D'||str[2]=='F')
				printf("Error\n");
			if(str[2]=='Q'||str[2]=='W'||str[2]=='E'||str[2]=='R')
				printf("Error\n");
		}
		scanf("%d",&D);
		for(int i=0;i<D;i++)
		{
			scanf("%s",str);
			vst2[str[0]-'A']=true;
			vst2[str[1]-'A']=true;
			del[str[0]-'A'][str[1]-'A']=del[str[1]-'A'][str[0]-'A']=true;
		}
		scanf("%d%s",&N,str);
		int pos=0;
		string res="";
		while(pos<N)
		{
			if(vst1[str[pos]-'A'])
			{
				if(pos+1<N&&G[str[pos]-'A'][str[pos+1]-'A']!=-1)
				{
					res+='A'+G[str[pos]-'A'][str[pos+1]-'A'],pos+=2;
					continue;
				}
			}
			if(vst2[str[pos]-'A'])
			{
				int np=pos+1;
				while(np<N)
				{
					if(del[str[pos]-'A'][str[np]-'A'])
					{
						if(np>0&&G[str[np-1]-'A'][str[np]-'A']!=-1) ;
						else break;
					}
					np++;
				}
				if(np<N) res="",pos=np+1;
				else res+=str[pos++];
			}
			else res+=str[pos++];
		}
		printf("Case #%d: [",cases++);
		if(res.length()==0) puts("]");
		else
		{
			printf("%c",res[0]);
			for(int i=1;i<res.length();i++)
				printf(", %c",res[i]);
			puts("]");
		}
	}
	return 0;
}