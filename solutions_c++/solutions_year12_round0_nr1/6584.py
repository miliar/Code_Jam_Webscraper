#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;
int main()
{
    int n,j=1;
    cin>>n;
    char vec[257];
    string cad;
    getline(cin,cad);
    vec[97]='y';
    vec[98]='h';
    vec[99]='e';
    vec[100]='s';
    vec[101]='o';
    vec[102]='c';
    vec[103]='v';
    vec[104]='x';
    vec[105]='d';
    vec[106]='u';
    vec[107]='i';
    vec[108]='g';
    vec[109]='l';
    vec[110]='b';
    vec[111]='k';
    vec[112]='r';
    vec[113]='z';
    vec[114]='t';
    vec[115]='n';
    vec[116]='w';
    vec[117]='j';
    vec[118]='p';
    vec[119]='f';
    vec[120]='m';
    vec[121]='a';
    vec[122]='q';

    while(j<=n)
    {
        char x;cout<<"Case #"<<j<<": ";
        while((x=getchar())!='\n')
        {
            if((x>=97&&x<=122)&&x!='\0')
            {
                cout<<vec[x];
            }
            else
            {
                cout<<x;
            }
        }
        cout<<endl;
    j++;
    }
    return 0;
}



