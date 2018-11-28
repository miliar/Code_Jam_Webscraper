#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
char ori[1001];
char temp[1001];
int d[20];
int main()
{
	int ii,k,j,may,ans,cs,css,i,need,l;
	char last;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	scanf("%d",&cs);
	for(css=1;css<=cs;css++)
	{
		ans=99999999;
		scanf("%d%s",&k,ori);
		memset(temp,0,sizeof(temp));
		for(i=0;i<k;i++)
			d[i]=i;
		need=1;
		for(i=2;i<=k;i++)
			need*=i;
		l=strlen(ori);
		for(ii=0;ii<need;ii++)
		{
			next_permutation(d,d+k);
			for(i=0;i<l;i+=k)
			{
				for(j=0;j<k;j++)
					temp[i+d[j]]=ori[i+j];
			}
			for(may=i=1;i<l;i++)
				if(temp[i]!=temp[i-1])may++;
			if(may<ans)ans=may;
		}
		printf("Case #%d: %d\n",css,ans);
	}
	return 0;
}
