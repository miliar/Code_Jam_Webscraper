#include<stdio.h>
#include<stdlib.h>
char mp[300];
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
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

    int n;
    scanf("%d\n",&n);
    for(int i=1;i<=n;i++){
        char tmp[1000];
        scanf("%[^\n]%*\n",tmp);
        printf("Case #%d: ",i);
        for(int j=0;tmp[j];j++){
            if(tmp[j]<='z'&&tmp[j]>='a'){
                printf("%c",mp[tmp[j]]);

            }
            else printf("%c",tmp[j]);
        }
        printf("\n");
    }
}
