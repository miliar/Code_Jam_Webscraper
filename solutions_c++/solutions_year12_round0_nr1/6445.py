#include <stdio.h>
#include <string.h>
int m[255];
void init(){
char _s[] = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
char __s[] = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

int i;
//bool used[1005]={false};
//for(i=0;i<sizeof(_s);i++)used[__s[i]]=true;
//for(i='a';i<='z';i++)if(!used[i])putchar(i);
//while(1);
for(i=0;i<sizeof(_s);i++)m[_s[i]]=__s[i];
/*m['a'] = 'y';
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
m['r'] = 't';
m['s'] = 'n';
m['t'] = 'w';
m['u'] = 'j';
m['v'] = 'p';
m['w'] = 'f';
m['x'] = 'm';
m['y'] = 'a';
*/
m['q'] = 'z';
m['z'] = 'q';
//qz
}
char ss[1000005];
void solve(){
    gets(ss);
    int l = strlen(ss),i;
    for(i=0;i<l;i++)if(ss[i]>='a'&&ss[i]<='z')ss[i] = m[ss[i]];
    puts(ss);
}
int main(){
    freopen("f:\\acm日志\\in.txt","r",stdin);
    freopen("f:\\acm日志\\out.txt","w",stdout);
    init();
    int cas,t=1;
    scanf("%d", &cas);gets(ss);
    while(cas--){
        printf("Case #%d: ",t++);
        solve();
        //while(1);
    }
}
