#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
	int i,j,k,n,t,r,c;
	char map[52][52];
	bool flag;
	
	freopen("al.in","r",stdin);
	freopen("al.out","w",stdout);
	k=0;
	cin>>t;
	while(t--)
	{
		k++;
		flag=true;
		cin>>r>>c;
		for(i=0;i<r;i++) cin>>map[i];
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if (map[i][j]=='#')
				{
					map[i][j]='/';
					if (i+1<r&&map[i+1][j]=='#')
						map[i+1][j]='\\';
					else
				    	flag=false;
					if (j+1<c&&map[i][j+1]=='#')
						map[i][j+1]='\\';
					else
						flag=false;
					if (i+1<r&&j+1<c&&map[i+1][j+1]=='#')
						map[i+1][j+1]='/';
					else
						flag=false;
				}
				if (!flag) break;
			}
			if (!flag) break;
		}
		printf("Case #%d:\n",k);
		if (!flag) cout<<"Impossible"<<endl;
		else
		{
			for(i=0;i<r;i++)
			{
				for(j=0;j<c;j++)
					printf("%c",map[i][j]);
				printf("\n");
			}
		}
	}
	//system("pause");
	return 0;
}