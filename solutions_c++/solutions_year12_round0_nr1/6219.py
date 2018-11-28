#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char dec_table[27]={20,};

void decode(char *p1, char *p2);

void dec(char *src);

FILE *fp, *fout;

int main()
{
	char enc1[]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	char enc2[]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	char enc3[]="de kr kd eoya kw aej tysr re ujdr lkgc jv";

	char dec1[]="our language is impossible to understand";
	char dec2[]="there are twenty six factorial possibilities";
	char dec3[]="so it is okay if you want to just give up";

	dec_table['q'-'a']='z';
	dec_table['z'-'a']='q';
	
	decode(enc1,dec1);
	decode(enc2,dec2);
	decode(enc3,dec3);



	fp = fopen("in.txt","r");
	fout = fopen("out.txt","w");


	int num;
	int i;
	char buffer[256];
	fgets(buffer,255,fp);
	num=atoi(buffer);

	for (i=0;i<num;i++)
	{
		char buffer2[100]={0,};
		fgets(buffer,255,fp);
		dec(buffer);
		sprintf(buffer2,"Case #%d: ",i+1); 
		fputs(buffer2,fout);
		fputs(buffer,fout);
		fputs("\n",fout);
	}

	fclose(fout);
	fclose(fp);


	return 0;
}

void dec(char *src)
{
	while(*src != 0)
	{
		if (*src >= 'a'&& *src <= 'z')
			*src = dec_table[(*src)-'a'];
		else if (*src == '\r' || *src == '\n')
			*src=0;
		src++;
	}
}

void decode(char *p1, char *p2)
{
	while(*p1 != 0)
	{
		if (*p2 >= 'a'&& *p2 <= 'z'){
			dec_table[*p1-'a']=*p2;
		}
		p1++;
		p2++;
	}
}