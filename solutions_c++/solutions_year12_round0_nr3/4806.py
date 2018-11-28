#include <iostream>
#include <string>
#include <cmath>

using namespace::std;

int tamano(int a)
{
    int cont=0;
    while(a>=10)
    {
        a=a/10;
        cont=cont+1;
    }
    return cont+1;
}

int elevar(int a)
{
    int result=1;
    int i;
    for(i=0;i<a;i++)
    {
        result=result*10;
    }
    return result;
}

int main()
{
    int casos, n, m, cont, i, a=1, j, intsize;
    int intermedio;
    cin>>casos;
    while(casos > 0)
    {
        cin>>n;
        cin>>m;
        if(n<10 && m <10)
        {
            cont=0;
        }
        else
        {
            cont=0;
            for(i=n;i<=m;i++)
            {
                intsize=tamano(i);
                intermedio=i;
                for(j=1;j<=intsize-1;j++)
                {
                    intermedio=(intermedio%10)*elevar(intsize-1) + intermedio/10;
                    if(intermedio>n && intermedio<=m && intermedio>i && i>=n )
                    {
                        cont=cont+1;
                    }
                }
            }
        }
        cout<<"Case #"<<a<<": "<<cont;
        if(casos>1)
        {
            cout<<endl;
        }
        a++;
        casos--;
    }
    return 0;
}
