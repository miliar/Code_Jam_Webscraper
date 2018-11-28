#include <cstdio>
using namespace std;

char a[203];
char decode[200];

void solve (int test){
     gets(a);
     printf ("Case #%d: ",test);
     for (int i=0;a[i]!='\0';++i){
         printf ("%c",decode[ a[i] ]);
     }
     printf ("\n");
     return;
}

void fill(){
     decode[' ']=' ';
     decode['a']='y';
     decode['b']='h';
     decode['c']='e';
     decode['d']='s';
     decode['e']='o';
     decode['f']='c';
     decode['g']='v';
     decode['h']='x';
     decode['i']='d';
     decode['j']='u';
     decode['k']='i';
     decode['l']='g';
     decode['m']='l';
     decode['n']='b';
     decode['o']='k';
     decode['p']='r';
     decode['q']='z';
     decode['r']='t';
     decode['s']='n';
     decode['t']='w';
     decode['u']='j';
     decode['v']='p';
     decode['w']='f';
     decode['x']='m';
     decode['y']='a';
     decode['z']='q';

}

int main (){
    int t;
    fill();
    scanf ("%d\n",&t);
    for (int i=0;i<t;++i){
        solve(i+1);
    }    
    return 0;
}
