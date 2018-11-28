#include<iostream>
#include<algorithm>
#include<memory.h>
#include<string.h>
using namespace std;
int map1[10][10];
bool map2[10][10];
char temp[5];
char s[105];
char ans[105];

int Change(char c)
{
	switch(c)
	{
	case('Q'):return 1;
	case('W'):return 2;
	case('E'):return 3;
	case('R'):return 4;
	case('A'):return 5;
	case('S'):return 6;
	case('D'):return 7;
	case('F'):return 8;
	default:return 0;
	}
}
int XChange(int d)
{
	switch(d)
	{
	case(1):return 'Q';
	case(2):return 'W';
	case(3):return 'E';
	case(4):return 'R';
	case(5):return 'A';
	case(6):return 'S';
	case(7):return 'D';
	case(8):return 'F';
	}
}
int work(int kans)
{
	int i;
	if(kans<2)return kans;
	if(map1[Change(ans[kans-1])][Change(ans[kans-2])]!=0)
	{
		ans[kans-2]=map1[Change(ans[kans-1])][Change(ans[kans-2])];
		kans=work(kans-1);
	}
	for(i=0;i<=kans-2;i++)
	{
		if(map2[Change(ans[i])][Change(ans[kans-1])]!=0)
			return kans=0;

	}

	return kans;
/*	if(kans==0){ans[kans++]=a;return;}
	ans[kans]=a;
	if(map1[Change(ans[kans-1])][Change(ans[kans])]!=0)
	{
		ans[kans-1]=map1[Change(ans[kans-1])][Change(ans[kans])];
		kans--;
		work(ans[kans]);
	}
	for(i=0;i<kans;i++)
	{
		if(map2[Change(ans[i])][Change(ans[kans])]!=0)
		{
			kans=0;
			return ;
		}
	}
	kans++;*/
}
int main()
{
//	freopen("B-large.in","r",stdin);
//	freopen("B.out","w",stdout);

	int ct,tt=0;
	int kans;
	int n1,n2,n,i,j,k,cur,kkans;
	scanf("%d",&ct);
	while(ct--)
	{
		scanf("%d ",&n1);
		memset(map1,0,sizeof(map1));
		memset(map2,0,sizeof(map2));
		kans=0;
		for(i=0;i<n1;i++)
		{
			scanf("%s ",&temp);
			map1[Change(temp[0])][Change(temp[1])]=map1[Change(temp[1])][Change(temp[0])]=temp[2];
		}
		scanf("%d",&n2);
		for(i=0;i<n2;i++)
		{
			scanf("%s",&temp);
			map2[Change(temp[0])][Change(temp[1])]=map2[Change(temp[1])][Change(temp[0])]=1;
		}
		scanf("%d ",&n);
		scanf("%s",&s);
		cur=s[0];
		ans[kans++]=cur;
		for(i=1;i<n;i++)
		{
			ans[kans++]=s[i];
			kans=work(kans);
		}
		printf("Case #%d: [",++tt);
		for(i=0;i<kans-1;i++)
			printf("%c, ",ans[i]);
		if(kans>0)printf("%c]\n",ans[kans-1]);
		else printf("]\n");
	}
	return 0;
}
