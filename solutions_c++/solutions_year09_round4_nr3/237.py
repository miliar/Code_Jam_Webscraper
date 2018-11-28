#include<iostream>
#include<cstdio>
using namespace std;
#include <string.h>
#define MAXN 310
#define _clr(x) memset(x,0xff,sizeof(int)*MAXN)

int hungary(int m,int n,int mat[][MAXN],int* match1,int* match2){
	int s[MAXN],t[MAXN],p,q,ret=0,i,j,k;
	for (_clr(match1),_clr(match2),i=0;i<m;ret+=(match1[i++]>=0))
		for (_clr(t),s[p=q=0]=i;p<=q&&match1[i]<0;p++)
			for (k=s[p],j=0;j<n&&match1[i]<0;j++)
				if (mat[k][j]&&t[j]<0){
					s[++q]=match2[j],t[j]=k;
					if (s[q]<0)
						for (p=j;p>=0;j=p)
							match2[j]=k=t[j],p=match1[k],match1[k]=j;
				}
	return ret;
}
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int cs,i,n,k,j,kk,mat[MAXN][MAXN],flag,mp[MAXN][MAXN],l,ll,match1[MAXN],match2[MAXN];
	cin>>cs;
	for (kk=1;kk<=cs;kk++)
	{
		cin>>n>>k;
		memset(mp,0,sizeof(mp));
		for (i=0;i<n;i++)
			for (j=0;j<k;j++)
				cin>>mp[i][j];
		memset(mat,0,sizeof(mat));
		for (i=0;i<n;i++)
			for (j=0;j<n;j++)
			{
				flag=0;
				for (l=0;l<k;l++)
					for (ll=0;ll<k;ll++)
						if (mp[i][l]>=mp[j][l] && mp[j][ll]>=mp[i][ll])
						{
							//mp[i][j]=1;
							flag=1;
							break;
						}
				if (flag==0)
					if (mp[i][0]>mp[j][0]) mat[i][j]=1;  
			}
		/*for (i=0;i<n;i++)
		{
			for (j=0;j<n;j++)
				cout<<mat[i][j]<<" ";
			cout<<endl;
		}*/
		cout<<"Case #"<<kk<<": "<<n-hungary(n,n,mat,match1,match2)<<endl;
	}
}
