#include <stdio.h>

int map[55][55];
int t,tcase,n,m;
char str[55][55];

int main()
{
	int i,j,ch;

	FILE *in,*out;
	in=fopen("a.in","r");
	out=fopen("a.out","w");

	fscanf(in,"%d",&tcase);
	for(t=0;t<tcase;t++)
	{
		fscanf(in,"%d",&n);
		fscanf(in,"%d",&m);

		for(i=0;i<n;i++)
		{
			fscanf(in,"%s",str[i]);
			for(j=0;j<m;j++)
				map[i][j]=0;
		}

		for(i=0;i<n-1;i++)
		{
			for(j=0;j<m-1;j++)
			{
				if(str[i][j]=='#' && str[i+1][j+1]=='#' && str[i][j+1]=='#' && str[i+1][j]=='#')
				{
					if(map[i][j]==0 && map[i+1][j+1]==0 && map[i+1][j]==0 && map[i][j+1]==0)
					{
						map[i][j]=map[i+1][j+1]=map[i+1][j]=map[i][j+1]=1;
						str[i][j]=str[i+1][j+1]='/';
						str[i+1][j]=str[i][j+1]=92;
					}
				}
			}
		}

		ch=0;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(str[i][j]!='.' && map[i][j]==0)
					ch=1;
			}
		}
		if(ch==0)
		{
			fprintf(out,"Case #%d:\n",t+1);
			for(i=0;i<n;i++)
				fprintf(out,"%s\n",str[i]);
		}
		else
			fprintf(out,"Case #%d:\nImpossible\n",t+1);
	}


	return 0;
}