#include<iostream>
#include<cstdio>
#include<cstring>
#include<map>
using namespace std;

map<int,int>mymap;

int main()
{
	int i,j,k,l,a,b,t,cas=0,ans,f[8]={10,100,1000,10000,100000,1000000};
	char s[10];
	
	//freopen("C-large.in","r",stdin);
    //freopen("out.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %d",&a,&b);
		ans=0;
		for(i=a;i<=b;i++)
		{
			sprintf(s,"%d",i);
			l=strlen(s);
			mymap.clear();
			for(j=0;j<l-1;j++)
			{
				k=(i%f[j])*f[l-j-2]+(i/f[j]);
				if (k>i&&k<=b&&!mymap[k]) {
					mymap[k]=1;
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}