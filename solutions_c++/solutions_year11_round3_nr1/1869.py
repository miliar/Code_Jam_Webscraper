#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define max_buf 200000



void main()
{

	int T=0,R=0,C=0;
	int i=0,j=0,k=0;

	char buf[max_buf];
	char* s= (char*)malloc(sizeof(char));
	char* a= (char*)malloc(sizeof(char));
	char** tiles;

	
	int sum=0,iter=0;
	int impossible=0;

	FILE* in=fopen("large.in","r");
	FILE* out=fopen("large_output.in","w");


	fgets(buf,sizeof(buf),in);
	T=atoi(buf);

	
	while(T-->0)
	{
		iter++;
		fgets(buf,sizeof(buf),in);
		R=atoi(strtok(buf," "));
		C=atoi(strtok(NULL," "));

		impossible=0;
		tiles=(char**)malloc(sizeof(char*) * R);

		for(i=0;i<R;i++)
		{
			tiles[i]=(char*)malloc(sizeof(char)*C);
			fgets(buf,sizeof(buf),in);
		
			for(j=0;j<C;j++)
			{
				tiles[i][j]=buf[j];
			}
		}

		//tiles배열 입력 완료


		for(i=0;i<R;i++)
		{
			if(impossible==1)
				break;
			for(j=0;j<C;j++)
			{
				if(impossible==1)
					break;

				if(tiles[i][j]=='#')
				{
					if(j==C-1 || i== R-1)
						impossible=1;
					else if(tiles[i][j+1] =='#' &&tiles[i+1][j] =='#' && tiles[i+1][j+1] =='#')
					{
						tiles[i][j]='/';
						tiles[i][j+1]='\\';
						tiles[i+1][j]='\\';
						tiles[i+1][j+1]='/';
					}
					else
						impossible=1;
				}
			}

		}







		

		fputs("Case #",out);
		_itoa(iter,s,10);
		fputs(s,out);
		fputs(":\n",out);


		_itoa(sum,a,10);
		if(impossible==1)
			fputs("Impossible\n",out);
		else
		{
			for(i=0;i<R;i++)
			{
				for(j=0;j<C;j++)
				{
					
					*a=tiles[i][j];
					fputs( a ,out);
				}
				fputs("\n",out);

			}
		}


	}
}






	