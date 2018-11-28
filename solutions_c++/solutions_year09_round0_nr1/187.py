#include<iostream>
#include<string>
#include<stdio.h>
#include<vector>
#include<math.h>
#include<sstream>
#include<algorithm>
#include<set>
using namespace std;
const int INF=1<<30;
typedef __int64 ll;

int l,d,n;
char dic[6000][20];
char ss[10000];
char ft[20][1000];
int lt[20];
int isdigit(char ch)
{
	if(ch>='a'&&ch<='z') return 1;
	return 0;
}
int main()
{
	int i,j,k;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	while(scanf("%d%d%d",&l,&d,&n)>0) 
	{
		for(i=0;i<d;i++) scanf("%s",dic[i]);
		for(i=1;i<=n;i++) 
		{
			scanf("%s",ss);
			int len=strlen(ss);
			int has=0;
			memset(lt,0,sizeof(lt));
			for(j=0;j<len;)
			{
				if(isdigit(ss[j])) 
				{
					ft[has][0]=ss[j]; lt[has++]=1;j++;
				}
				else if(ss[j]=='(') 
				{
					j++;
					while(j<len&&isdigit(ss[j]))
					{
						ft[has][lt[has]++]=ss[j];j++;
					}
					sort(ft[has],ft[has]+lt[has]);
					has++;
					j++;
				}
			}
			int cnt=0;
			for(j=0;j<d;j++) 
			{
				for(k=0;k<l;k++) 
				{
					int temp=lower_bound(ft[k],ft[k]+lt[k],dic[j][k])-ft[k];
					if(temp==lt[k]||ft[k][temp]!=dic[j][k]) break;
				}
				if(k==l) cnt++;
			}
			printf("Case #%d: %d\n",i,cnt);
		}
	}
	return 0;
}