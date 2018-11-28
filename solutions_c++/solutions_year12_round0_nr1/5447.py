#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
using namespace std;
int main()
{
    freopen("txt.in","r",stdin);
    freopen("txt.out","w",stdout);
    int t,num=1;
    char a[102];
    cin >>t;
    gets(a);
    while(t--)
    {

        map<char,char>Map;
        Map['a']='y';
        Map['b']='h';
        Map['c']='e';
        Map['d']='s';
        Map['e']='o';
        Map['f']='c';
        Map['g']='v';
        Map['h']='x';
        Map['i']='d';
        Map['j']='u';
        Map['k']='i';
        Map['l']='g';
        Map['m']='l';
        Map['n']='b';
        Map['o']='k';
        Map['p']='r';
        Map['q']='z';
        Map['r']='t';
        Map['s']='n';
        Map['t']='w';
        Map['u']='j';
        Map['v']='p';
        Map['w']='f';
        Map['x']='m';
        Map['y']='a';
        Map['z']='q';
        printf("Case #%d: ",num++);
        char ch[120];
        gets(ch);
        int cnt=0,len=strlen(ch),first=1;
        while(cnt<len)
        {
            char str[102];
            sscanf(ch+cnt,"%s",str);
            int len2=strlen(str);
            if(!first)
            {
                printf(" ");
                first=0;
            }
            for(int i=0;i<len2;i++)
            printf("%c",Map[str[i]]);
            cnt+=strlen(str)+1;
            first=0;
        }
        printf("\n");
    }
    return 0;
}
