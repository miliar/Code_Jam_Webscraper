#include<stdio.h>
#include<string.h>
char a[105];
int b[150];
int main()
{
    int t,j,i;
    b[97]='y';
    b[98]='h';
    b[99]='e';
    b[100]='s';
    b[101]='o';
    b[102]='c';
    b[103]='v';
    b[104]='x';
    b[105]='d';
    b[106]='u';
    b[107]='i';
    b[108]='g';
    b[109]='l';
    b[110]='b';
    b[111]='k';
    b[112]='r';
    b[113]='z';
    b[114]='t';
    b[115]='n';
    b[116]='w';
    b[117]='j';
    b[118]='p';
    b[119]='f';
    b[120]='m';
    b[121]='a';
    b[122]='q';
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        gets(a);
        j=0;
        while(a[j]!='\0')
        {
            printf("%c",b[a[i]]);
            i++;
        }
        printf("\n");
    }
    return(0);
}
