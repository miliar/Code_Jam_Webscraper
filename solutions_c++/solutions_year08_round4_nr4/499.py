#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string.h>
using namespace std;
#define N 50000
char str[N+1],sss[N+1];
int myindex[100];
void shuffle(char *p1,char* p2,int map[],int n)
{
	for(int i=0;i<n;i++)
		p2[i]=p1[myindex[i]];
}
int RLE(char* pp,int n)
{
	int re=0;
	for(int i=1;i<n;i++)
		if(pp[i]!=pp[i-1])re++;
	return re;
}
int main()
{
	int t,ca=1;
	for(scanf("%d",&t);t--;)
	{
		int k;
		scanf("%d",&k);
		assert(k<=5);
		scanf("%s",&str);
		int n=strlen(str);
		assert(0==(n%k));
		for(int i=0;i<k;i++)myindex[i]=i;
		int ans=n;
		do
		{
			for(int i=0;i<n;i+=k)
				shuffle(str+i,sss+i,myindex,k);
			ans=min(ans,1+RLE(sss,n));
		}while(next_permutation(myindex,myindex+k));
		printf("Case #%d: %d\n",ca++,ans);
	}
	return 0;
}
