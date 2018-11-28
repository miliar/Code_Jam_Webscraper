#include<cstdio>
void deal(char&i)
{
    if(i=='a')i='y';
    else if(i=='b')i='h';
    else if(i=='c')i='e';
    else if(i=='d')i='s';
    else if(i=='e')i='o';
    else if(i=='f')i='c';
    else if(i=='g')i='v';
    else if(i=='h')i='x';
    else if(i=='i')i='d';
    else if(i=='j')i='u';//q
    else if(i=='k')i='i';
    else if(i=='l')i='g';
    else if(i=='m')i='l';
    else if(i=='n')i='b';
    else if(i=='o')i='k';
    else if(i=='p')i='r';
    else if(i=='q')i='z';
    else if(i=='r')i='t';
    else if(i=='s')i='n';
    else if(i=='t')i='w';
    else if(i=='u')i='j';
    else if(i=='v')i='p';
    else if(i=='w')i='f';
    else if(i=='x')i='m';
    else if(i=='y')i='a';
    else if(i=='z')i='q';
}
char tmp[110];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a.out","w",stdout);
    int ti;
    scanf("%d",&ti);getchar();
    for(int i=1;i<=ti;i++)
    {
        gets(tmp);
        for(int j=0;tmp[j];j++)
        {
            deal(tmp[j]);
        }
        printf("Case #%d: %s\n",i,tmp);
    }
}
