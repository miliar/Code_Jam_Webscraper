#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int i,j,n;

    char niza[123]="";

    freopen("tongues.in","r",stdin);
    freopen("tongues.out","w",stdout);

    niza['a']='y';
    niza['b']='h';
    niza['c']='e';
    niza['d']='s';
    niza['e']='o';
    niza['f']='c';
    niza['g']='v';
    niza['h']='x';
    niza['i']='d';
    niza['j']='u';
    niza['k']='i';
    niza['l']='g';
    niza['m']='l';
    niza['n']='b';
    niza['o']='k';
    niza['p']='r';
    niza['q']='z';
    niza['r']='t';
    niza['s']='n';
    niza['t']='w';
    niza['u']='j';
    niza['v']='p';
    niza['w']='f';
    niza['x']='m';
    niza['y']='a';
    niza['z']='q';

    cin>>n;
    for (j=0;j<n+1;j++)
    {
        string a;
        getline(cin,a);

        if (j) cout<<"Case #"<<j<<": ";

        for (i=0;i<a.size();i++)
        if (a[i]==' ') cout<<a[i];
            else cout<<niza[a[i]];
        cout<<"\n";
    }


    return 0;
}
