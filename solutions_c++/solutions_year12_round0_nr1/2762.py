/*
ID: kishwarshafin
PROG:
LANG: C++
*/
/*
Timus JI: 119454XP
*/
#include<iostream>
#include<vector>
#include<stack>
#include<string>
#include<queue>
#include<map>
#include<algorithm>
#include<sstream>
using namespace std;
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#define MAX 100
#define INF 2147483647
#define in(a) freopen(a,"r",stdin)
#define out(a) freopen(a,"w",stdout)

int main()
{
//    #ifndef ONLINE_JUDGE
//	in("in.txt");
//	out("out.txt");
//    #endif

    int t,caseno=1;
    scanf("%d\n",&t);
    while(t--)
    {
        printf("Case #%d: ",caseno++);
        char str[1000];
        gets(str);
        for(int i=0;i<strlen(str);i++)
        {
            if(str[i]=='a')str[i]='y';
            else if(str[i]=='b')str[i]='h';
            else if(str[i]=='c')str[i]='e';
            else if(str[i]=='d')str[i]='s';
            else if(str[i]=='e')str[i]='o';
            else if(str[i]=='f')str[i]='c';
            else if(str[i]=='g')str[i]='v';
            else if(str[i]=='h')str[i]='x';
            else if(str[i]=='i')str[i]='d';
            else if(str[i]=='j')str[i]='u';
            else if(str[i]=='k')str[i]='i';
            else if(str[i]=='l')str[i]='g';
            else if(str[i]=='m')str[i]='l';
            else if(str[i]=='n')str[i]='b';
            else if(str[i]=='o')str[i]='k';
            else if(str[i]=='p')str[i]='r';
            else if(str[i]=='q')str[i]='z';
            else if(str[i]=='r')str[i]='t';
            else if(str[i]=='s')str[i]='n';
            else if(str[i]=='t')str[i]='w';
            else if(str[i]=='u')str[i]='j';
            else if(str[i]=='v')str[i]='p';
            else if(str[i]=='w')str[i]='f';
            else if(str[i]=='x')str[i]='m';
            else if(str[i]=='y')str[i]='a';
            else if(str[i]=='z')str[i]='q';
        }
        puts(str);
    }
	return 0;
}
