#include<stdio.h>
//#include<conio.h>
#include<string.h>
int main()
{
    int t,i,j;
    char a[105],b[105];
    freopen("r.in","r",stdin);
    freopen("write.txt","w",stdout);
    scanf("%d\n",&t);
    for(i=0;i<t;i++)
    {
     gets(a);
     j=0;
     while(a[j]!='\0')
     {
      switch(a[j])
     { 
      case 'a':b[j]='y';
      break;
      case 'b':b[j]='h';
      break;
      case 'c':b[j]='e';
      break;
      case 'd':b[j]='s';
      break;
      case 'e':b[j]='o';
      break;
      case 'f':b[j]='c';
      break;
      case 'g':b[j]='v';
      break;
      case 'h':b[j]='x';
      break;
      case 'i':b[j]='d';
      break;
      case 'j':b[j]='u';
      break;
      case 'k':b[j]='i';
      break;
      case 'l':b[j]='g';
      break;
      case 'm':b[j]='l';
      break;
      case 'n':b[j]='b';
      break;
      case 'o':b[j]='k';
      break;
      case 'p':b[j]='r';
      break;
      case 'q':b[j]='z';
      break;
      case 'r':b[j]='t';
      break;
      case 's':b[j]='n';
      break;
      case 't':b[j]='w';
      break;
      case 'u':b[j]='j';
      break;
      case 'v':b[j]='p';
      break;
      case 'w':b[j]='f';
      break;
      case 'x':b[j]='m';
      break;
      case 'y':b[j]='a';
      break;
      case 'z':b[j]='q';
      break;
      case ' ':b[j]=' ';
      }
      j++;
      }
      b[j]='\0';
      printf("Case #%d: %s\n",i+1,b);
      }
  //    getch();
      return 0;
      }
