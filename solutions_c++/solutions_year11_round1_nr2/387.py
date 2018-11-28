// gcjr1b.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
struct cz
{
	char word[20];
	int bh;
}dcb[105],cs[105];
int cmp(cz a,cz b)
{
	if(strcmp(a.word,b.word)==0)
		return a.bh<b.bh;
	else return strcmp(a.word,b.word)<0;
}
char sx[15][30];
int main()
{
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int t,n,m,i,j,k,cas,max1,cnt,maxi,k1,i1,j1;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			scanf(" %s",dcb[i].word);
		}
		for(i=0;i<m;i++)
		{
			scanf(" %s",sx[i]);
		}
		sort(dcb,dcb+n,cmp);
		for(i=0;i<n;i++)
			dcb[i].bh=i;
		printf("Case #%d: ",cas);
		for(k1=0;k1<m;k1++)
		{
			max1=-1;
		maxi=-1;
			for(i=0;i<n;i++)
			{
				
				for(j=0;j<n;j++)
				{
					cs[j]=dcb[j];
				}
				for(j=0;j<n;j++)
				{
					int len=strlen(cs[j].word);
					for(k=0;k<len;k++)
					{
						cs[j].word[k]='-';
					}
				}
				cnt=0;
				int cnt1=1000000;
				for(k=0;k<26;k++)
				{
					char t1=sx[k1][k];
					sort(cs,cs+n,cmp);
					for(i1=0;i1<n;i1++)
					{
						if(cs[i1].bh==i)
							break;
					}
					int sj,xj;
					sj=i1;
					xj=i1;
					while(strcmp(cs[sj+1].word,cs[i1].word)==0&&sj<n-1)
						sj++;
					while(strcmp(cs[xj-1].word,cs[i1].word)==0&&xj>0)
						xj--;
					cnt1=sj-xj+1;
					if(cnt1==1)
						break;
					int tag1=0;//原词中有
					int tag2=0;//所有词中有
					for(i1=xj;i1<=sj;i1++)
					{
						int len=strlen(cs[i1].word);
						for(j1=0;j1<len;j1++)
						{
							if(dcb[cs[i1].bh].word[j1]==t1)
							{
								tag2=1;
								if(cs[i1].bh==i)
									tag1=1;
							}
						}
					}
					if(tag2&&!tag1)
						cnt++;
					for(i1=0;i1<n;i1++)
					{
						int len=strlen(cs[i1].word);
						for(j1=0;j1<len;j1++)
						{
							if(dcb[cs[i1].bh].word[j1]==t1)
							{
								cs[i1].word[j1]=t1;
							}
						}
					}
				}
            if(cnt>max1)
			{
				max1=cnt;
                maxi=i;
			}
			}
	printf("%s",dcb[maxi].word);
	if(k1==m-1)
		printf("\n");
	else
		printf(" ");
		}
	}

	return 0;
}

