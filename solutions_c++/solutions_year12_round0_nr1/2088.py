#include"stdio.h"
//#include"conio.h"
int main()
{
    int test,c=0,n=0;
    char g[120];
    
    scanf("%d%*c",&test);
    
    for(;c<test;c++)
    {
                    gets(g);
                    for(n=0;g[n]!='\0';n++)
                    {
                                           switch(g[n])
                                           {
                                                       case 97 :
                                                            {
                                                                g[n]='y';
                                                                break;
                                                            }
                                                       case 98 :
                                                            {
                                                                g[n]='h';
                                                                break;
                                                            }
                                                       case 99 :
                                                            {
                                                                g[n]='e';
                                                                break;
                                                            }
                                                       case 100 :
                                                            {
                                                                g[n]='s';
                                                                break;
                                                            }
                                                       case 101 :
                                                            {
                                                                g[n]='o';
                                                                break;
                                                            }
                                                       case 102 :
                                                            {
                                                                g[n]='c';
                                                                break;
                                                            }
                                                       case 103 :
                                                            {
                                                                g[n]='v';
                                                                break;
                                                            }
                                                       case 104 :
                                                            {
                                                                g[n]='x';
                                                                break;
                                                            }
                                                       case 105 :
                                                            {
                                                                g[n]='d';
                                                                break;
                                                            }
                                                       case 106 :
                                                            {
                                                                g[n]='u';
                                                                break;
                                                            }
                                                       case 107 :
                                                            {
                                                                g[n]='i';
                                                                break;
                                                            }
                                                       case 108 :
                                                            {
                                                                g[n]='g';
                                                                break;
                                                            }
                                                       case 109 :
                                                            {
                                                                g[n]='l';
                                                                break;
                                                            }
                                                       case 110 :
                                                            {
                                                                g[n]='b';
                                                                break;
                                                            }
                                                       case 111 :
                                                            {
                                                                g[n]='k';
                                                                break;
                                                            }
                                                       case 112 :
                                                            {
                                                                g[n]='r';
                                                                break;
                                                            }
                                                       case 113 :
                                                            {
                                                                g[n]='z';
                                                                break;
                                                            }
                                                       case 114 :
                                                            {
                                                                g[n]='t';
                                                                break;
                                                            }
                                                       case 115 :
                                                            {
                                                                g[n]='n';
                                                                break;
                                                            }
                                                       case 116 :
                                                            {
                                                                g[n]='w';
                                                                break;
                                                            }
                                                       case 117 :
                                                            {
                                                                g[n]='j';
                                                                break;
                                                            }
                                                       case 118 :
                                                            {
                                                                g[n]='p';
                                                                break;
                                                            }
                                                       case 119 :
                                                            {
                                                                g[n]='f';
                                                                break;
                                                            }
                                                       case 120 :
                                                            {
                                                                g[n]='m';
                                                                break;
                                                            }
                                                       case 121 :
                                                            {
                                                                g[n]='a';
                                                                break;
                                                            }
                                                       case 122 :
                                                            {
                                                                g[n]='q';
                                                                break;
                                                            }
                                                       case 32 :
                                                            {
                                                                break;
                                                            }
                                                       default :
                                                               {
                                                                      printf("error");
                                                               }
                                           }
                    }
                    printf("Case #%d: ",c+1);
                    puts(g);
                    
    }
//    getch();
    return 0;
}
