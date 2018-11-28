#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
char mp[210];
char ch[1100],ch1[1100];
int main()
{
    //freopen("hehehe.in","r",stdin);
    //freopen("kengdiea_A.out","w",stdout);
    int i,j,k,T,tt=0,N;
mp['a']='y';
mp['b']='h';
mp['c']='e';
mp['d']='s';
mp['e']='o';
mp['f']='c';
mp['g']='v';
mp['h']='x';
mp['i']='d';
mp['j']='u';
mp['k']='i';
mp['l']='g';
mp['m']='l';
mp['n']='b';
mp['o']='k';
mp['p']='r';
mp['q']='z';
mp['r']='t';
mp['s']='n';
mp['t']='w';
mp['u']='j';
mp['v']='p';
mp['w']='f';
mp['x']='m';
mp['y']='a';
mp['z']='q';
    scanf("%d",&T);gets(ch);
    while(T--)
    {tt++;
        gets(ch);N=strlen(ch);
        printf("Case #%d: ",tt);
        for(i=0;i<N;i++)
        {
            if(ch[i]>='a'&&ch[i]<='z') printf("%c",mp[ch[i]]);
            else printf("%c",ch[i]);
        }printf("\n");
    }
    return 0;
}
