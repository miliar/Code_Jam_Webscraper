#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int maxn = 100009;
const int mod = 100000007;


char m[26];
int init(void)
{

    m['a'-'a']='y';
    m['b'-'a']='h';
    m['c'-'a']='e';
    m['d'-'a']='s';
    m['e'-'a']='o';
    m['f'-'a']='c';
    m['g'-'a']='v';
    m['h'-'a']='x';
    m['i'-'a']='d';
    m['j'-'a']='u';
    m['k'-'a']='i';
    m['l'-'a']='g';
    m['m'-'a']='l';
    m['n'-'a']='b';
    m['o'-'a']='k';
    m['p'-'a']='r';
    m['q'-'a']='z';
    m['r'-'a']='t';
    m['s'-'a']='n';
    m['t'-'a']='w';
    m['u'-'a']='j';
    m['v'-'a']='p';
    m['w'-'a']='f';
    m['x'-'a']='m';
    m['y'-'a']='a';
    m['z'-'a']='q';
}
int main(void)
{
    string ans = "";
    int cases ;
 //   freopen("in.txt","r",stdin);
  //  freopen("out.txt","w",stdout);
    scanf("%d",&cases);
    char c;
    init();
    c=getchar();
    for(int p=1;p<=cases;++p)
    {
        ans="";
        while(1)
        {
            c=getchar();
            if(c==' ')ans.push_back(' ');
            else if(c=='\n')break;
            else ans.push_back( m [c-'a']);

        }
        printf("Case #%d: %s\n",p,ans.c_str());

    }
    return 0;
}
