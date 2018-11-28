#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

char word[100000],target[100000];
int k,len;
int p[100];
int ans;

void CHECK()
{
	int i,j,x,cnt;

	for(i=0,j=k-1;i<len;i+=k,j+=k)
	{
		for(x=0;x<k;x++) target[x+i]=word[ p[x]+i ];
	}

	cnt=1;
	for(i=1;i<len;i++)
		if(target[i]!=target[i-1])
			cnt++;

	if(ans>cnt) ans=cnt;
}

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int T,ks,i;
	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		ans=1000000000;

		scanf("%d%s",&k,word);

		len=strlen(word);

		for(i=0;i<k;i++)
			p[i]=i;

		do
		{
//			for(i=0;i<k;i++) printf(" %d",p[i]); printf("\n");
			CHECK();
		}while(next_permutation(p,p+k));

		printf("Case #%d: %d\n",ks,ans);
	}

	return 0;
}