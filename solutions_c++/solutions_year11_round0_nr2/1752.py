#include<cstdio>
#include<cstring>
#include<list>
#include<map>
#include<string>
using namespace std;

char base[500][500];
bool can[500][500];
char str[500];
int main()
{
	int t,c,d,n;
	FILE* pFile=fopen("2.out","w");
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		string vec;
		vec="";
		memset(base,0,sizeof(base));
		memset(can,0,sizeof(can));
		
		scanf("%d",&c);
		for(int i=0;i<c;i++)
		{
			char tmp[5];
			scanf("%s",tmp);
			base[tmp[1]][tmp[0]]=base[tmp[0]][tmp[1]]=tmp[2];
		}
		scanf("%d",&d);
		for(int i=0;i<d;i++)
		{
			char tmp[5];
			scanf("%s",tmp);
			can[tmp[0]][tmp[1]]=1;
			can[tmp[1]][tmp[0]]=1;
		}
		int len=0;
		scanf("%d %s",&n,str);
		for(int i=0;i<n;i++)
		{
			vec[len++]=str[i];
			if(len==1) continue;
			if(base[vec[len-1]][vec[len-2]]!=0) 
			{
				vec[len-2]=base[vec[len-1]][vec[len-2]];
				vec[len-1]=0;
				len--;
				continue;
			}
			for(int k=0;k<len-1;k++)
				if(can[vec[k]][vec[len-1]]==1)
				{
					len=0;
					break;
				}
		}
		vec[len]=0;
		fprintf(pFile,"Case #%d: [",cas);
		for(int i=0;i<len;i++)
			if(i==len-1) fprintf(pFile,"%c",vec[i]);
			else fprintf(pFile,"%c, ",vec[i]);
		fprintf(pFile,"]\n");
	}
	return 0;
}
