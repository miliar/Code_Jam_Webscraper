#include <stdio.h>
char rep[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z',
't','n','w','j','p','f','m','a','q'};
int main ( void )
{
	int T,i,j;	
	FILE *file = fopen ( "a.txt", "r" );
	FILE *file2 = fopen ( "file2.txt", "w" );
	char line[102]; /* or other suitable maximum line size */
	if (file == NULL) perror ("Error opening file");
    while(fscanf(file,"%d",&T)==1)
	{
		fgets(line,sizeof(line),file);
		for(j=0;j<T;j++)
		{
			fgets(line,sizeof(line),file);
			fprintf(file2,"Case #%d: ",j+1);
			for(i=0;line[i];i++)
			{
				if(line[i]==32)
					fprintf(file2," ");
				else if(line[i]>=97 && line[i]<123)
					fprintf(file2,"%c",rep[line[i]-97]);
			}
			fprintf(file2,"\n");
		}
	}
	return 0;
}