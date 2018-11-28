#include<cstdio>
#include<algorithm>
#include<map>
#include<vector>
#include<cstring>
using namespace std;
char words[120];
char trans[300];
char line[120];
int TC;
int main(){
    int i,j;
    scanf("%d",&TC);
    trans['a']='y';
trans['b']='h';
trans['c']='e';
trans['d']='s';
trans['e']='o';
trans['f']='c';
trans['g']='v';
trans['h']='x';
trans['i']='d';
trans['j']='u';
trans['k']='i';
trans['l']='g';
trans['m']='l';
trans['n']='b';
trans['o']='k';
trans['p']='r';
trans['q']='z';
trans['r']='t';
trans['s']='n';
trans['t']='w';
trans['u']='j';;
trans['v']='p';
trans['w']='f';
trans['x']='m';;
trans['y']='a';
trans['z']='q';
scanf("%*c");
    for(int tc=1;tc<=TC;tc++){
        fgets(line,120,stdin);
        for(i=0;i<strlen(line);i++){
            if(line[i]!=' '&&line[i]!='\n')line[i]=trans[line[i]];
        }
        printf("Case #%d: %s",tc,line);



    }
    return 0;

    return 0;
}
