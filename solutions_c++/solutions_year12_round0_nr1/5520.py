#include<stdio.h>
#include<string.h>
char s1[35]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char dizi[150],c;
int main()
{
	int n,i,j;
	char t;
	FILE *oku=fopen("A-small-attempt1.in","r");
	FILE *yaz=fopen("A-small-attempt1.out","w");
	fscanf(oku,"%d ",&n);
	for(i=0;i<n;i++)
	{
		fprintf(yaz,"Case #%d: ",i+1);
		while(1)
		{
			fscanf(oku,"%c",&c);
			if(c=='\n')break;
			else if(c==' ')fprintf(yaz," ");
			else fprintf(yaz,"%c",s1[c-'a']);
		}
		if(i!=n-1)
			fprintf(yaz,"\n");
	}
	return 0;
}		
