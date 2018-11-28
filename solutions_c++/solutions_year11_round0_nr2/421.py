#include <stdio.h>
#include <iostream>
#include <memory.h>
using namespace std;
int ma[32][32];
bool tma[32][32];
int tot;
char St[128],ans[128];
int Alen,len;
void init()
{
	int c;
	char CC[8];
	scanf("%d",&c);
	for(int i=0;i<c;i++)
	{
		scanf("%s",&CC);
		ma[CC[0]-'A'][CC[1]-'A']=CC[2]-'A'+1;
		ma[CC[1]-'A'][CC[0]-'A']=CC[2]-'A'+1;
	}
	scanf("%d",&c);
	for(int i=0;i<c;i++)
	{
		scanf("%s",&CC);
		tma[CC[0]-'A'][CC[1]-'A']=true;
		tma[CC[1]-'A'][CC[0]-'A']=true;
	}
	scanf("%d",&Alen);	
	scanf( "%s",&St);
}
void work1()
{
	if(len==1)return;
	if(ma[ans[len-1]][ans[len-2]]!=0)
	{
		ans[len-2]=ma[ans[len-1]][ans[len-2]]-1;
		len--;
	}
	return;
}
void work2()
{
	for(int i=len-2;i>=0;i--)
	{
		if(tma[ans[i]][ans[len-1]])
		{
			len=0;
			return;
		}
	}
	return;
}
void workans()
{
	len=0;
	for(int i=0;i<Alen;i++)
	{
		ans[len]=St[i]-'A';
		len++;
		work1();
		work2();
	}
	return;
}
void outans()
{
	printf("[");
	if(len!=0)
	{
		for(int i=0;i<len-1;i++)
			printf("%c, ",ans[i]+'A');
		printf("%c",ans[len-1]+'A');
	}
	printf("]\n");
}	
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&tot);
	for(int kk=1;kk<=tot;kk++)
	{
		memset(ma,0,sizeof(ma));
		memset(tma,false,sizeof(tma));
		init();
		workans();
		printf("Case #%d: ",kk);
		outans();
	}
	return 0;
}
