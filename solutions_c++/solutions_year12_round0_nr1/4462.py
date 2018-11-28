#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <fstream>

using namespace std;

ofstream fout("A-small-attempt2.out");
ifstream fin("A-small-attempt2.in");

char a[26]={'y','h','e','s','o','c','v',
            'x','d','u','i','g','l','b',
            'k','r','z','t','n','w','j','p',
            'f','m','a','q'};
char e[150];
char ch[150];

int main()
{
    int j,i,T,l;
    fin>>T;
    fin.getline(e,150);
    for (i=1;i<=T;i++)
    {
        fin.getline(e,150);
        l=strlen(e);
        memset(ch,0,sizeof(ch));
        for (j=0;j<l;j++)
        {
            if (e[j]==' ') ch[j]=' ';
              else ch[j]=a[e[j]-'a'];
        }
        ch[l]='\0';
        fout<<"Case #"<<i<<": "<<ch<<endl;    
    }
    return 0;
}
