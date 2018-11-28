#include<cstdio>
#include<cstring>
#include<map>

using namespace std;

int main(){
    map<char,char> googler;
    googler[' ']=' ';
    googler['a']='y';
    googler['b']='h';
    googler['c']='e';
    googler['d']='s';
    googler['e']='o';
    googler['f']='c';
    googler['g']='v';
    googler['h']='x';
    googler['i']='d';
    googler['j']='u';
    googler['k']='i';
    googler['l']='g';
    googler['m']='l';
    googler['n']='b';
    googler['o']='k';
    googler['p']='r';
    googler['q']='z';
    googler['r']='t';
    googler['s']='n';
    googler['t']='w';
    googler['u']='j';
    googler['v']='p';
    googler['w']='f';
    googler['x']='m';
    googler['y']='a';
    googler['z']='q';
    
    int i,j,lines,googlen;
    scanf("%d",&lines);
    getchar();
    char googlersentence[100];
    for(i=0;i<lines;i++){
        gets(googlersentence);
        printf("Case #%d: ",i+1);
        googlen = strlen(googlersentence);
        for(j=0;j<googlen;j++)
            printf("%c",googler[googlersentence[j]]);
        printf("\n");
    }
    return 0;
}