#include<stdio.h>
int count=1;
char replace(char a)
{
    if(a=='a')
    return 'y';
    else if(a=='b')
    return 'h';
    else if(a=='c')
    return 'e';
    else if(a=='d')
    return 's';
    else if(a=='e')
    return 'o';
    else if(a=='f')
    return 'c';
    else if(a=='g')
    return 'v';//
    else if(a=='h')
    return 'x';
    else if(a=='i')
    return 'd';
    else if(a=='j')
    return 'u';
    else if(a=='k')
    return 'i';
    else if(a=='l')
    return 'g';
    else if(a=='m')
    return 'l';
    else if(a=='n')
    return 'b';
    else if(a=='o')
    return 'k';
    else if(a=='p')
    return 'r';
    else if(a=='q')
    return 'z';
    else if(a=='r')
    return 't';
    else if(a=='s')
    return 'n';
    else if(a=='t')
    return 'w';
    else if(a=='u')
    return 'j';
    else if(a=='v')
    return 'p';
    else if(a=='w')
    return 'f';
    else if(a=='x')
    return 'm';
    else if(a=='y')
    return 'a';
    else if(a=='z')
    return 'q';//
    else if(a==' ')
    return ' ';
    else if(a=='\0')
    return '\0';
    else if(a=='\n')
    return '\0';
    else
    {
        printf("error in the input");
        exit(2);
    }
}
void pass(char* gr)
{
    int i ;
    char* lan;
    int siz=100;
    lan=(char*)malloc(strlen(gr)+1);
    for(i=0;i<=strlen(gr);i++)
    {
        lan[i]=replace(gr[i]);
    }
    printf("Case #%d: %s\n",count,lan);
    count++;
}
int main ()
{
int test_case;
size_t siz=100;
char* gr;
gr=(char*)malloc(101);
scanf("%d",&test_case);
if(test_case>30)
{
    printf("invalid entry");
    exit(1);
}
getchar();
while(test_case--)
{
    //getchar();
    //scanf("%s",gr);
    getline(&gr,&siz,stdin);
    pass(gr);
    //printf("%s",gr);
}
return 0;
}
