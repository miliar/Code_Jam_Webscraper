#include <cstdio>
#include <iostream>
#include <map>

using namespace std;

int main()
{
    map <char,char> mymap;
    mymap['a']='y';
    mymap['b']='h';
    mymap['c']='e';
    mymap['d']='s';
    mymap['e']='o';
    mymap['f']='c';
    mymap['g']='v';
    mymap['h']='x';
    mymap['i']='d';
    mymap['j']='u';
    mymap['k']='i';
    mymap['l']='g';
    mymap['m']='l';
    mymap['n']='b';
    mymap['o']='k';
    mymap['p']='r';
    mymap['q']='z';
    mymap['r']='t';
    mymap['s']='n';
    mymap['t']='w';
    mymap['u']='j';
    mymap['v']='p';
    mymap['w']='f';
    mymap['x']='m';
    mymap['y']='a';
    mymap['z']='q';
    mymap[' ']=' ';


    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);

    int cases;
    scanf("%d",&cases);
    getchar();

    char line[110];
    for (int m=1;m<=cases;++m)
    {
        gets(line);

        printf("Case #%d: ",m);
        for (int i=0;line[i]!='\0';++i)
        {
            if (mymap.find(line[i])!=mymap.end())
                printf("%c",mymap[line[i]]);
            else
                printf("%c",line[i]);
        }
        printf("\n");

    }
    return 0;

}
