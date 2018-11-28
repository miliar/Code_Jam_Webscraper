#include<iostream.h>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<conio.h>
char match[28][2]={{' ', ' '},{'a', 'y'},{'b','h'},{'c','e'},{'d','s'},{'e','o'},{'f','c'},{'g', 'v'},{'h', 'x'},{'i', 'd'},{'j', 'u'},{'k', 'i'},{'l', 'g'},{'m', 'l'},{'n', 'b'},{'o', 'k'},{'p', 'r'},{'q','z'},{'r','t'},{'s', 'n'},{'t', 'w'},{'u', 'j'},{'v', 'p'},{'w', 'f'},{'x', 'm'},{'y','a'},{'z', 'q'}};
void main()

{
	int i,n,count=1,f=0;
	char c;
	FILE *f1,*f2;
	f1=fopen("g:/sairam/codejam/A-small-attempt1.in","r");
	f2=fopen("g:/sairam/codejam/A-small.out","w");
	   fscanf(f1,"%d",&n);
	   fprintf(f2,"Case #1: ");
	   c=fgetc(f1);
	   c=fgetc(f1);
	   while(!feof(f1))
	   {



		for(i=0;i<=26;i++)
			if(c==match[i][0])
			  {
				fputc(match[i][1],f2);
				f=1;
				break;

			  }


		if(f==0)
		{
		      fputc('\n',f2);
			count++;
			if(count<=n)
			{
				fprintf(f2,"Case #");
				fprintf(f2,"%d",count);
				fputc(':',f2);
				fputc(' ',f2);
			 }
		}
			//fputc(c,f2);
			f=0;
		c=fgetc(f1);
	   }


    fclose(f1);
    fclose(f2);
}