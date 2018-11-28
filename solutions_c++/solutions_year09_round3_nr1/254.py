#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;
long long int power(int a,int n)
{
	if(n==1)
		return a;
	else if(n==0)
		return 1;
	long long int ans=power(a,n/2);
	if(n%2==0)
		return ans*ans;
	else
		return ans*ans*a;
}
int main()
{
	int i,j,k,p,t,n,z,cnt,len;
	long long int w;
	int ascii[256];
	char word[65];
	int wt[256];
	scanf("%d\n",&t);
	long long int ans=0;
	for(p=1;p<=t;p++)
	{
		ans=0;
		fgets(word,62,stdin);
		len=strlen(word);
		fill(ascii,ascii+256,0);
		len--;
		fill(wt,wt+256,0);
		for(i=0;i<len;i++)
			ascii[word[i]]++;
		k=0;
		for(i=0;i<256;i++)
		{
			if(ascii[i]!=0)
				k++;
		}
		if(k<2)
			k=2;
		z=1;
		while(z<len&&word[z]==word[z-1])
			z++;
		w=power(k,len-1);
		//printf("YO%d %d %lld\n",k,len,w);
		for(i=0;i<z;i++)
		{
			ans+=w;
			w/=k;
		}
		wt[word[0]]=1;
		wt[word[z]]=-1;
		cnt=1;
		w/=k;
		for(i=z+1;i<len;i++)
		{
			if(wt[word[i]]==0)
			{
				wt[word[i]]=++cnt;
				ans+=wt[word[i]]*w;
			}
			else if(wt[word[i]]!=-1)
			{
				ans+=wt[word[i]]*w;
			}
			w/=k;
		}
		printf("Case #%d: %lld\n",p,ans);
	}
}