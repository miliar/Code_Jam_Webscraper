#include<stdio.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
using namespace std;
#define MAX 201
const int BIG=0x3f3f3f3f;
char cc[MAX],mp[128][128],sk[MAX];
bool ban[128][128];
int skn,has[128];
int main()
{
	int cs,c,d,n,i,j;
	scanf("%d",&cs);
	for(int dd=1;dd<=cs;dd++)
	{
		memset(mp,0,sizeof(mp));
		memset(ban,0,sizeof(ban));
		memset(has,0,sizeof(has));
		scanf("%d",&c);
		for(i=0;i<c;i++)
		{
			scanf("%s",cc);
			mp[cc[0]][cc[1]]=cc[2];
			mp[cc[1]][cc[0]]=cc[2];
		}
		scanf("%d",&d);
		for(i=0;i<d;i++)
		{
			scanf("%s",cc);
			ban[cc[0]][cc[1]]=true;
			ban[cc[1]][cc[0]]=true;
		}
		int f;
		scanf("%d %s",&n,cc);
		for(skn=i=0;i<n;i++)
		{
			f=0;
			has[sk[skn]=cc[i]]++;
			while(skn>0 && mp[sk[skn]][sk[skn-1]])
			{
				f=1;
				has[sk[skn]]--;
				has[sk[skn-1]]--;
				sk[skn-1]=mp[sk[skn]][sk[skn-1]];
				has[sk[skn-1]]++;
				skn--;
			}
			has[cc[i]]--;
			for(j=0;j<128;j++)
				if(has[j]>0 && ban[sk[skn]][j])
					break;
			has[cc[i]]++;
			if(j==128 || f==1)
				skn++;
			else
			{
				skn=0;
				memset(has,0,sizeof(has));
			}
		}
		printf("Case #%d: [",dd);
		for(i=0;i<skn;i++)
			if(i==0)
				printf("%c",sk[i]);
			else
				printf(", %c",sk[i]);
		puts("]");
	}
}