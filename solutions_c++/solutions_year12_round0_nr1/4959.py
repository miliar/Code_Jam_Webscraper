#include<stdio.h>
#include<string.h>
int main()
{
	char str[105],buf,re[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int t,i,cas=1;
	FILE *p,*p1;
	p= fopen("try.txt","r");
	p1=fopen("output.txt","a");
	fscanf(p,"%d",&t);
	fscanf(p,"%c",&buf);
	while(t--)
	{
		fgets(str,105,p);
		for(i=0;str[i]!='\0';i++)
		{
			if((str[i]==' ')||(str[i]=='\n'))continue;
			str[i]=re[str[i]-97];
		}
		fprintf(p1,"Case #%d: ",cas);
		fputs(str,p1);
		cas++;
	}
	fclose(p);
	fclose(p1);
	return 0;
}