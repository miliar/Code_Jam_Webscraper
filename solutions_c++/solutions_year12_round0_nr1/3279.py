#include<stdio.h>
#include<string.h>
int main()
{
    char s[26],str[105];
    int ctr=1,t,i,l;
    s[0]='y';
    s[1]='h';
    s[2]='e';
    s[3]='s';
    s[4]='o';
    s[5]='c';
    s[6]='v';
    s[7]='x';
    s[8]='d';
    s[9]='u';
    s[10]='i';
    s[11]='g';
    s[12]='l';
    s[13]='b';
    s[14]='k';
    s[15]='r';
    s[16]='z';
    s[17]='t';
    s[18]='n';
    s[19]='w';
    s[20]='j';
    s[21]='p';
    s[22]='f';
    s[23]='m';
    s[24]='a';
    s[25]='q';
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    getchar();
    for(;ctr<=t;ctr++)
    {
             gets(str);
             l=strlen(str);
             for(i=0;i<l;i++)
             {
                             if((str[i]>='a')&&(str[i]<='z'))  
                             {
                              str[i]=s[str[i]-'a'];
                             }
             }
             printf("Case #%d: %s\n",ctr,str);
    }
    return 0;
}
    
