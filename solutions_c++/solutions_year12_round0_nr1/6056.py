#include<stdio.h>
#include<string.h>
#include<conio.h>

	char in[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char out[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int index(char a)
	{
				return int(a)-97;
	}
int main()
{
	FILE *input,*output;
	input=fopen("input.txt","r");
	output=fopen("output.txt","w");
	int n,i;
	fscanf(input,"%d",&n);fgetc(input);//getchar();
	for(i=1;i<=n;i++)
	{
	 //	int length=0;
	   //	char a[120];
		//scanf("%s[\n]",a);getchar();getchar();
		//gets(a);
		
		fprintf(output,"Case #%d: ",i);
		char b=fgetc(input);
		while( b!='\n')
		{
	 //	length=strlen(a);
	       //	for(int j=0;j<length;j++)
	       //	{
			if(b<=122&&b>=97)
			{
				fprintf(output,"%c",out[index(b)]);
			}
			else fprintf(output,"%c",b);
	       //	}
		b=fgetc(input);
		}
		fprintf(output,"\n");
	}
	fclose(input);
	fclose(output);
//	getch();
	return 0;
}
