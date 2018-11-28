#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
char cd[60][60];
char da[60][60];
int ax[]={0,0,1,-1,1,-1,1,-1};
int ay[]={1,-1,0,0,1,-1,-1,1};
int main()
{
	freopen("a1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int i,j,k,l,m,n,z,tk;
	scanf("%d",&z);
	for(int y=1;y<=z;y++)
	{
		scanf("%d%d",&n,&tk);
		for(i=0;i<n;i++)
			scanf("%s",cd[i]);
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				da[i][j]=cd[n-1-j][i];
				
		for(j=0;j<n;j++)
		{
			i=n-1;k=n-1;
			for(;i>=0;i--)
				if(da[i][j]!='.')
					da[k--][j]=da[i][j];
			for(;k>=0;k--)
				da[k][j]='.';
		}
//		for(i=0;i<n;i++,cout<<endl)
//			for(j=0;j<n;j++)
//				;//printf("%c",da[i][j]);
		bool br,bb;
		br=bb=false;
		int t[8];
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
			{
				if(da[i][j]=='.')
					continue;
				for(k=0;k<8;k++)
				{
					for(l=1;;l++)
					{
						if(i+l*ax[k]>=0 && i+l*ax[k]<n && j+l*ay[k]>=0 && j+l*ay[k]<n && da[i+l*ax[k]][j+l*ay[k]]==da[i][j]);
						else
							break;
					}
					t[k]=l-1;
				}
				t[0]+=t[1]+1;
				t[2]+=t[3]+1;
				t[4]+=t[5]+1;
				t[6]+=t[7]+1;
				if(t[0]>=tk || t[2]>=tk || t[4]>=tk || t[6]>=tk)
				{
					if(da[i][j]=='B')
						bb=true;
					else
						br=true;
				}
			}
			
		if(bb&& br)
			printf("Case #%d: Both\n",y);
		else if(bb)
			printf("Case #%d: Blue\n",y);
		else if(br)
			printf("Case #%d: Red\n",y);
		else
			printf("Case #%d: Neither\n",y);
	}
	return 0;
}
