#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;

int t;
int num[9]={0,2,3,4,5,6,7,8,9};
char s[66];
int hash[128];

int main()
{
	int i,j,k,tt;
	freopen("A.small.out","w",stdout);
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++)
	{
		scanf("%s",s);
		memset(hash,-1,sizeof(hash));
		int l=strlen(s);
		int y=0;
		hash[s[0]]=1;
			for(i=0;i<l;i++)
				if(hash[s[i]]==-1)
				if(y<9)
					hash[s[i]]=num[y++];
			     else hash[s[i]]=1+y++;
				int ss;
			if(y==0)
				ss=2;
			else ss=y+1;
		//	printf("%d\n",ss);
			long long sum=0;
			for(i=0;i<l;i++)
			{
				sum=hash[s[i]]+sum*ss;
			}
			printf("Case #%d: ",tt);
			cout<<sum<<endl;
	}
	return 0;
}
	

