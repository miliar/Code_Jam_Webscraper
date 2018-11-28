#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int tc=1;tc<=T;tc++)
	{
		int r,c,i,j;
		char pic[100][100]={0};
		cin>>r>>c;
		for(i=0;i<r;i++)
			scanf("%s",pic[i]);
		bool pos=true;
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(pic[i][j]=='#')
				{
					if(pic[i][j+1]!='#' || pic[i+1][j]!='#' || pic[i+1][j+1]!='#')
					{
						pos=false;
						break;
					}
					pic[i][j]='/';
					pic[i][j+1]=92;
					pic[i+1][j]=92;
					pic[i+1][j+1]='/';
				}
			}
			if(pos==false)break;
		}
		printf("Case #%d:\n",tc);
		if(pos==false)
		{
			puts("Impossible");
			continue;
		}
		for(i=0;i<r;i++)
			printf("%s\n",pic[i]);
	}
	return 0;
}
