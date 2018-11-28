#include <cstdio>

int main()
{
	int testcase,cnt=1;
	FILE* fp;
	fp=fopen("output.out","w");

	scanf("%d",&testcase);
	while(testcase--)
	{
		int R,C;
		char map[55][55];
		int i,j;
		bool isright=true;

		scanf("%d%d",&R,&C);
		for(i=0;i<R;i++)
		{
			scanf("%s",map[i]);
		}
		for(i=0;i<R;i++)
		{
			for(j=0;j<C;j++)
			{
				if(map[i][j]=='#')
				{
					if((j+1)<C&&(i+1)<R)
					{
						if(map[i+1][j]=='#'&&map[i+1][j+1]=='#'&&map[i][j+1]=='#')
						{
							map[i][j]='/';
							map[i][j+1]='\\';
							map[i+1][j]='\\';
							map[i+1][j+1]='/';
						}
					}
				}
			}
		}
		for(i=0;i<R;i++)
		{
			for(j=0;j<C;j++)
			{
				if(map[i][j]=='#')
				{
					isright=false;
				}
			}
		}
		fprintf(fp,"Case #%d:\n",cnt++);
		if(isright)
		{
			for(i=0;i<R;i++)
			{
				fprintf(fp,"%s\n",(map[i]));
			}
		}
		else
		{
			fprintf(fp,"Impossible\n");
		}
	}
	return 0;
}
