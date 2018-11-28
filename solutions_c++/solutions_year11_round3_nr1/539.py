#include <cstdio>
#include <cstring>
#include <iostream>

#include <cmath>
#include <algorithm>

#include <set>
#include <queue>
#include <stack>
using namespace std;

int main ()
{
	FILE *fin=freopen("a.in","r",stdin);
	FILE *fout=freopen("a.out","w",stdout);

	int T,t;
	int i,j,r,c;
	char g[60][60];
	bool b;

	//cin>>T;
	fscanf(fin,"%d",&T);
	for(t=1;t<=T;t++)
	{
		fscanf(fin,"%d %d",&r,&c);
		for(i=0;i<r;i++)
		{
			fscanf(fin," %s ",&g[i]);
		}
		b=false;
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(g[i][j]=='#')
				{
					if(g[i][j+1]=='#' && g[i+1][j+1]=='#' && g[i+1][j]=='#' && i+1<r && j+1<c)
					{
						g[i][j]='/';
						g[i][j+1]='\\';
						g[i+1][j]='\\';
						g[i+1][j+1]='/';
					}
					else
					{
						fprintf(fout,"Case #%d:\nImpossible\n",t);
						b=true;
						break;
					}
				}
			}
			if(b)
				break;
		}
		if(b)
			continue;
		fprintf(fout,"Case #%d:\n",t);
		for(i=0;i<r;i++)
		{
			fprintf(fout,"%s\n",g[i]);
		}
	}

	return 0;
}
