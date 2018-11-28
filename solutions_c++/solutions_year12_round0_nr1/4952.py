#include<stdio.h>

int main()
{
    int t,i,j;
    char A[120];
    
    scanf("%d%*i",&t);
    
    for(i=0;i<t;i++)
    {
                    gets(A);
                    for(j=0;A[j]!='\0';j++)
                    {
                                           switch(A[j])
                                           {
                                                       case 97 :
                                                            {
                                                                A[j]='y';
                                                                break;
                                                            }
                                                       case 98 :
                                                            {
                                                                A[j]='h';
                                                                break;
                                                            }
                                                       case 99 :
                                                            {
                                                                A[j]='e';
                                                                break;
                                                            }
                                                       case 100 :
                                                            {
                                                                A[j]='s';
                                                                break;
                                                            }
                                                       case 101 :
                                                            {
                                                                A[j]='o';
                                                                break;
                                                            }
                                                       case 102 :
                                                            {
                                                                A[j]='c';
                                                                break;
                                                            }
                                                       case 103 :
                                                            {
                                                                A[j]='v';
                                                                break;
                                                            }
                                                       case 104 :
                                                            {
                                                                A[j]='x';
                                                                break;
                                                            }
                                                       case 105 :
                                                            {
                                                                A[j]='d';
                                                                break;
                                                            }
                                                       case 106 :
                                                            {
                                                                A[j]='u';
                                                                break;
                                                            }
                                                       case 107 :
                                                            {
                                                                A[j]='i';
                                                                break;
                                                            }
                                                       case 108 :
                                                            {
                                                                A[j]='g';
                                                                break;
                                                            }
                                                       case 109 :
                                                            {
                                                                A[j]='l';
                                                                break;
                                                            }
                                                       case 110 :
                                                            {
                                                                A[j]='b';
                                                                break;
                                                            }
                                                       case 111 :
                                                            {
                                                                A[j]='k';
                                                                break;
                                                            }
                                                       case 112 :
                                                            {
                                                                A[j]='r';
                                                                break;
                                                            }
                                                       case 113 :
                                                            {
                                                                A[j]='z';
                                                                break;
                                                            }
                                                       case 114 :
                                                            {
                                                                A[j]='t';
                                                                break;
                                                            }
                                                       case 115 :
                                                            {
                                                                A[j]='n';
                                                                break;
                                                            }
                                                       case 116 :
                                                            {
                                                                A[j]='w';
                                                                break;
                                                            }
                                                       case 117 :
                                                            {
                                                                A[j]='j';
                                                                break;
                                                            }
                                                       case 118 :
                                                            {
                                                                A[j]='p';
                                                                break;
                                                            }
                                                       case 119 :
                                                            {
                                                                A[j]='f';
                                                                break;
                                                            }
                                                       case 120 :
                                                            {
                                                                A[j]='m';
                                                                break;
                                                            }
                                                       case 121 :
                                                            {
                                                                A[j]='a';
                                                                break;
                                                            }
                                                       case 122 :
                                                            {
                                                                A[j]='q';
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
                    printf("Case #%d: ",i+1);
                    puts(A);
                    
    }

    return 0;
}
