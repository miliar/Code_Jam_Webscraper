#include<stdio.h>
#include<conio.h>
#include<string.h>

int main()
{
    FILE *f1,*f2;
    int t,l,j,k,i;
    char word[102];
    f1=fopen("A.in","r");
    f2=fopen("A.out","w");
    fscanf(f1,"%d\n",&t);
    for(i=1;i<=t;i++)
    {
                    k=0;
                    while(1)
                    {
                            word[k]=getc(f1);
                            if(word[k]=='\n')
                            {
                            word[k]='\0';
                            break;
                            }
                            k++;
                            }
                            
                            // gets(word);
                    //scanf("[^\n]",word);
                     l=strlen(word);
                     for(j=0;j<l;j++)
                     {
                                     if(word[j]=='a')
                                     {
                                                     word[j]='y';
                                                     }
                                                     else if(word[j]=='b')
                                     {
                                                     word[j]='h';
                                                     } else if(word[j]=='c')
                                     {
                                                     word[j]='e';
                                                     } else if(word[j]=='d')
                                     {
                                                     word[j]='s';
                                                     } else if(word[j]=='e')
                                     {
                                                     word[j]='o';
                                                     } else if(word[j]=='f')
                                     {
                                                     word[j]='c';
                                                     } else if(word[j]=='g')
                                     {
                                                     word[j]='v';
                                                     } else if(word[j]=='h')
                                     {
                                                     word[j]='x';
                                                     } else if(word[j]=='i')
                                     {
                                                     word[j]='d';
                                                     } else if(word[j]=='j')
                                     {
                                                     word[j]='u';
                                                     } else if(word[j]=='k')
                                     {
                                                     word[j]='i';
                                                     } else if(word[j]=='l')
                                     {
                                                     word[j]='g';
                                                     } else if(word[j]=='m')
                                     {
                                                     word[j]='l';
                                                     } else if(word[j]=='n')
                                     {
                                                     word[j]='b';
                                                     } else if(word[j]=='o')
                                     {
                                                     word[j]='k';
                                                     } else if(word[j]=='p')
                                     {
                                                     word[j]='r';
                                                     } else if(word[j]=='q')
                                     {
                                                     word[j]='z';
                                                     } else if(word[j]=='r')
                                     {
                                                     word[j]='t';
                                                     } else if(word[j]=='s')
                                     {
                                                     word[j]='n';
                                                     } else if(word[j]=='t')
                                     {
                                                     word[j]='w';
                                                     } else if(word[j]=='u')
                                     {
                                                     word[j]='j';
                                                     } else if(word[j]=='v')
                                     {
                                                     word[j]='p';
                                                     } else if(word[j]=='w')
                                     {
                                                     word[j]='f';
                                                     } else if(word[j]=='x')
                                     {
                                                     word[j]='m';
                                                     } else if(word[j]=='y')
                                     {
                                                     word[j]='a';
                                                     } else if(word[j]=='z')
                                     {
                                                     word[j]='q';
                                                     } 
                                                     }
                                                     fprintf(f2,"Case #%d: %s\n",i,word);
                                                     
                                                     }
                                                     getch();
                                                     fclose(f1);
                                                     fclose(f2);
                                                     return 0;
                                                     }
                                                     
    
