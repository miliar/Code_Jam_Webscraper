#include<stdio.h>
int main()
{
    int a,b,n;
    char word[35][105];
    char key[26];
    key[0]='y';
    key[1]='h';
    key[2]='e';
    key[3]='s';
    key[4]='o';
    key[5]='c';
    key[6]='v';
    key[7]='x';
    key[8]='d';
    key[9]='u';
    key[10]='i';
    key[11]='g';
    key[12]='l';
    key[13]='b';
    key[14]='k';
    key[15]='r';
    key[16]='z';
    key[17]='t';
    key[18]='n';
    key[19]='w';
    key[20]='j';
    key[21]='p';
    key[22]='f';
    key[23]='m';
    key[24]='a';
    key[25]='q';
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    scanf("%d\n",&n);
    for(a=0;a<n;a++)
        gets(word[a]);
    for(a=0;a<n;a++)
    {
        printf("Case #%d: ",a+1);
        for(b=0;word[a][b]!='\0';b++)
            if(word[a][b]==' ')
                printf(" ");
            else if(word[a][b]>='a' && word[a][b]<='z')
                printf("%c",key[word[a][b]-'a']);
        printf("\n");
    }
    scanf(" ");
}
