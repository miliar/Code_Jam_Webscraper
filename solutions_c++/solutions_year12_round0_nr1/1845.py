#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
int map[50];
char str[10000];
int main()
{
   // freopen("A.in","r",stdin);
  //  freopen("A.out","w",stdout);
    map[0]='y'-'a';
    map[1]='h'-'b';
    map[2]='e'-'c';
    map[3]='s'-'d';
    map[4]='o'-'e';
    map[5]='c'-'f';
    map[6]='v'-'g';
    map[7]='x'-'h';
    map[8]='d'-'i';
    map[9]='u'-'j';
    map[10]='i'-'k';
    map[11]='g'-'l';
    map[12]='l'-'m';
    map[13]='b'-'n';
    map[14]='k'-'o';
    map[15]='r'-'p';
    map[16]='z'-'q';
    map[17]='t'-'r';
    map[18]='n'-'s';
    map[19]='w'-'t';
    map[20]='j'-'u';
    map[21]='p'-'v';
    map[22]='f'-'w';
    map[23]='m'-'x';
    map[24]='a'-'y';
    map[25]='q'-'z';
    int T;
    int iCase=0;
    scanf("%d",&T);
    getchar();
    while(T--)
    {
        iCase++;
        cin.getline(str,10000);
        int len=strlen(str);
        printf("Case #%d: ",iCase);
        for(int i=0;i<len;i++)
        {
            if(str[i]==' ') printf(" ");
            else
              printf("%c",str[i]+map[str[i]-'a']);
        }    
        printf("\n");
    }    
    return 0;
}    
