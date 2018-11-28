#include <stdio.h>

int main(int argc, char *argv[])
{
	FILE *fp;
	int k=1;
	int i;
	int n;
	char t[128];
	char out[32][128];
	int trans[27]={0,'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	
	if((fp=fopen("test.txt","w"))==NULL)  /*以只写方式打开文件*/
        {
            printf("cannot open file!\n");
        }

	scanf("%d ",&n);
	while(k<=n)
	{
		gets(t);
		for(i=0;t[i]!='\0';i++)
		{
			if(t[i]!=' ')
				out[k][i]=trans[t[i]-96];
			else
				out[k][i]=' ';
		}
		out[k][i]='\0';
		k++;
	}

	for(int i=1;i<=n;i++)
	{
		printf("Case #%d: %s\n",i,out[i]);
		fprintf(fp,"Case #%d: %s\n",i,out[i]);
	}
	fclose(fp);
	return 0;
}
