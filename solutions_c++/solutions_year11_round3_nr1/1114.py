#include<iostream>
#include<algorithm>

using namespace std;
int n,m;

bool out(int i,int j)
{
	if(i < 0 || j<0 || i>=n || j>=m)
		return true;

	return false;
}
char map[55][55];

int main()
{

	freopen("A-large!!!.in","r",stdin);
	freopen("A-large!!!.out","w",stdout);
	int i,j;

	int cas;
	int k = 1;

	scanf("%d",&cas);

	while(cas --)
	{
		scanf("%d%d",&n,&m);

		for(i=0;i<n;i++)

			scanf("%s",map[i]);


		for(i=0;i<n;i++)

			for(j=0;j<m;j++)

				if(map[i][j] == '#')
				{		
					if(out(i,j+1) || out(i+1,j) || out(i+1,j+1) )
						continue;
					
					if(map[i+1][j] != '#' || map[i][j+1] != '#' || map[i+1][j+1] != '#')
					
						continue;

					map[i][j] = '/';
					map[i+1][j] = '\\';
					map[i][j+1] = '\\';
					map[i+1][j+1] = '/';
				}
		
		int flag = 0;

		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)

				if(map[i][j] == '#')
				{
					flag = 1;
					break;
				}
			if(flag )
				break;
		}

		printf("Case #%d:\n",k++);

		if(flag )
			printf("Impossible\n");

		else
			for(i=0;i<n;i++)
				printf("%s\n",map[i]);
				
	}

	return 0;
}


					