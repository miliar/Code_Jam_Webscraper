#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
int ctr=0;
char name[250];
int main()
{   int l1=0;
int a;
    scanf("%d",&a);
    getchar();
    while(a--)
    {
    ctr++;
    gets(name);
    l1=strlen(name);
    func(l1);
    printf("Case #%d: %s",ctr,name);
    printf("\n");
    
   memset(name,0,l1);
    }
    
    getch();
}

int func(int l)
{    char ch;
     int i;
     for(i=0;i<l;i++)
     {
      ch=name[i];
      
      switch(ch)
      {
                case 'a':name[i]='y';
                break;
                case 'b':name[i]='h';
                break;
                case 'c':name[i]='e';
                break;
                case 'd':name[i]='s';
                break;
                case 'e':name[i]='o';
                break;
                case 'f':name[i]='c';
                break;
                case 'g':name[i]='v';
                break;
                case 'h':name[i]='x';
                break;
                case 'i':name[i]='d';
                break;
                case 'j':name[i]='u';
                break;
                case 'k':name[i]='i';
                break;
                case 'l':name[i]='g';
                break;
                case 'm':name[i]='l';
                break;
                case 'n':name[i]='b';
                break;
                case 'o':name[i]='k';
                break;
                case 'p':name[i]='r';
                break;
                case 'q':name[i]='z';
                break;
                case 'r':name[i]='t';
                break;
                case 's':name[i]='n';
                break;
                case 't':name[i]='w';
                break;
                case 'u':name[i]='j';
                break;
                case 'v':name[i]='p';
                break;
                case 'w':name[i]='f';
                break;
                case 'x':name[i]='m';
                break;
                case 'y':name[i]='a';
                break;
                case 'z':name[i]='q';
                break;
                case ' ':name[i]=' ';
                break;
      }
      }
      
      }
                     
    
     
