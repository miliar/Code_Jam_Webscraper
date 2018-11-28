#include <cstdio>
#include <map>

using namespace std;
int main (int argc, char const* argv[])
{
    map<char,char> mmap;
    mmap['a']='y';
    mmap['b']='h';
    mmap['c']='e';
    mmap['d']='s';
    mmap['e']='o';
    mmap['f']='c';
    mmap['g']='v';
    mmap['h']='x';
    mmap['i']='d';
    mmap['j']='u';
    mmap['k']='i';
    mmap['l']='g';
    mmap['m']='l';
    mmap['n']='b';
    mmap['o']='k';
    mmap['p']='r';
    mmap['q']='z';
    mmap['r']='t';
    mmap['s']='n';
    mmap['t']='w';
    mmap['u']='j';
    mmap['v']='p';
    mmap['w']='f';
    mmap['x']='m';
    mmap['y']='a';
    mmap['z']='q';
    mmap[' ']=' ';
 
    int t;
    scanf("%d",&t);
    char str[200];
    int i,j;
    int len;
    for ( i = 1; i <= t; i += 1)
    {
        scanf(" %[^\n]%n",str,&len);
        //puts(str);break;
        len--;
        printf("Case #%d: ",i);
        for ( j = 0; j < len; j += 1)
        {
            printf("%c",mmap[str[j]]);
        }
        printf("\n");
    }
    return 0;
}
