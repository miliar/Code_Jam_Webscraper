#include<cstdio>
#include<map>
#include<cstring>
using namespace std;
main(){
    map<char,char> m;
    int T,i,k;
m['a'] = 'y';
m['b'] = 'h';
m['c'] = 'e';
m['d'] = 's';
m['e'] = 'o';
m['f'] = 'c';
m['g'] = 'v';
m['h'] = 'x';
m['i'] = 'd';
m['j'] = 'u';
m['k'] = 'i';
m['l'] = 'g';
m['m'] = 'l';
m['n'] = 'b';
m['o'] = 'k';
m['p'] = 'r';
m['q'] = 'z';
m['r'] = 't';
m['s'] = 'n';
m['t'] = 'w';
m['u'] = 'j';
m['v'] = 'p';
m['w'] = 'f';
m['x'] = 'm';
m['y'] = 'a';
m['z'] = 'q';
    char ch,str[101];
    scanf("%d",&T);
    getchar();
    i=1;
    while(T--){
        k=0;
        while((ch=getchar())!='\n')
        if(ch>='a' && ch<='z')
            str[k++]=m[ch];
        else
            str[k++]=ch;
        str[k]='\0';
        printf("Case #%d: %s\n",i++,str);
    }
    return 0;
}
