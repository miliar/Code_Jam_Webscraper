#include<iostream>
using namespace std;
char a[60][60];
int main()
{
    freopen("n.txt","w",stdout);
	int i,j,id,t;
	int r,c;
	cin>>t;
	for(id=1;id<=t;id++)
	{
		scanf("%d%d",&r,&c);
		printf("Case #%d:\n",id);
		for(i=0;i<r;i++)
		{
			scanf("%s",a[i]);
		}
		int flag=0;
		for(i=0;i<r;i++)
			for(j=0;j<c;j++)
			{
				if(a[i][j]=='#')
				{
					if(i==r-1||j==c-1)
						flag=1;
					else if(a[i][j+1]=='#'&&(a[i+1][j]=='#')&&a[i+1][j+1]=='#')
					{
						a[i][j]='/';
						a[i+1][j+1]='/';
						a[i+1][j]='\\';
						a[i][j+1]='\\';
					}
					else
					{
						flag=1;
					}
					if(flag==1)
						goto chasingdream;
				}
			}
chasingdream:
			if(flag==1)
				puts("Impossible");
			else
			{
				for(i=0;i<r;i++)
					puts(a[i]);
			}
			
	}
}