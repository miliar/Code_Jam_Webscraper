#include<iostream>
#include<stdio.h>
#define N 1010
char comb[N][3],destr[N][2],a[N];
bool d[N]={false};
char c[N],ans[N];
using namespace std;
int main()
{
	int tc,p,q,n,cnt;
	scanf("%d",&tc);
	for(int t=0;t<tc;t++)
	{
		cnt=0;
		for(int i=0;i<676;i++) c[i]=0,d[i]=false;
		scanf("%d ",&p);
		for(int i=0;i<p;i++) {
			scanf(" %c%c%c ",&comb[i][0],&comb[i][1],&comb[i][2]);
			for(int j=0;j<3;j++) comb[i][j]=comb[i][j]-'A';
		}
		scanf(" %d ",&q);
		for(int i=0;i<q;i++) {
			scanf(" %c%c ",&destr[i][0],&destr[i][1]);
			for(int j=0;j<2;j++) destr[i][j]=destr[i][j]-'A';
		}
		scanf(" %d ",&n);
		for(int i=0;i<n;i++) {
			scanf(" %c ",&a[i]);
			a[i]=a[i]-'A';
		}
		for(int i=0;i<p;i++) 
		{
			c[comb[i][0]*26+comb[i][1]]=comb[i][2];
			c[comb[i][1]*26+comb[i][0]]=comb[i][2];
		}
		for(int i=0;i<q;i++)
		{
			d[destr[i][0]*26+destr[i][1]]=true;
			d[destr[i][1]*26+destr[i][0]]=true;
		}
		ans[0]=a[0],cnt=1;
		for(int i=1;i<n;i++)
		{
			ans[cnt++]=a[i];
			while(cnt>=2 && c[ans[cnt-1]*26+ans[cnt-2]]!=0)
			{
				ans[cnt-2]=c[ans[cnt-1]*26+ans[cnt-2]];
				cnt=cnt-1;
			}
			for(int j=cnt-2;j>=0;j--)
				if(d[ans[cnt-1]*26+ans[j]])
				{
					cnt=0;
					break;
				}
		}
		printf("Case #%d: [",t+1);
		for(int i=0;i<cnt-1;i++) printf("%c, ",ans[i]+65);
		if(cnt>0) printf("%c",ans[cnt-1]+65);
		printf("]\n");
	}
	return 0;
}
