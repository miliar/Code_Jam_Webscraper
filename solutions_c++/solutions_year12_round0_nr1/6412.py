#include <stdio.h>
#include<conio.h>
#include<iostream.h>
#include<ctype.h>
#include<fstream.h>
#include<string.h>


char chnge(ch)
{
if(ch=='a')
	return 'y';
else if(ch=='b')
	return 'h';
else if(ch=='c')
	return 'e';
else if(ch=='d')
	return 's';
else if(ch=='e')
	return 'o';
else if(ch=='f')
	return 'c';
else if(ch=='g')
	return 'v';
else if(ch=='h')
	return 'x';
else if(ch=='i')
	return 'd';
else if(ch=='j')
	return 'u';
else if(ch=='k')
	return 'i';
else if(ch=='l')
	return 'g';
else if(ch=='m')
	return 'l';
else if(ch=='n')
	return 'b';
else if(ch=='o')
	return 'k';
else if(ch=='p')
	return 'r';
else if(ch=='q')
	return 'z';
else if(ch=='r')
	return 't';
else if(ch=='s')
	return 'n';
else if(ch=='t')
	return 'w';
else if(ch=='u')
	return 'j';
else if(ch=='v')
	return 'p';
else if(ch=='w')
	return 'f';
else if(ch=='x')
	return 'm';
else if(ch=='y')
	return 'a';
else if(ch=='z')
	return 'q';

	return ch;
}

void main()
{
    clrscr();
    FILE *stream,*st1;
    char st[1500],ch ;
    int c,i=0;
    stream=fopen("A.txt","r");
    st1=fopen("output.txt","w");
    c=fgetc(stream);
    cout<<c;
    c=fgetc(stream);
    cout<<c;
    do
    {   ch=fgetc(stream);
	st[i]=chnge(ch);
	fputc(st[i],st1);
	i++;
    }while(ch!=EOF);
    fclose(stream);
    fclose(st1);
    getch();
}