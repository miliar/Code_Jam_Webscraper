#include <iostream>

using namespace std;

int main()
{
    int T,A,B,i,k,j,warunek;
    cin>>T;
    for(i=0;i<T;i++)
    {
        cin>>A;
        cin>>B;
        char tab[A][B];
        for(j=0;j<A;j++)
        {
            for(k=0;k<B;k++)
            {
                cin>>tab[j][k];
            }
        }
        for(j=0;j<A-1;j++)
        {
            for(k=0;k<B-1;k++)
            {
                if(tab[j][k]=='#'&&tab[j+1][k]=='#'&&tab[j][k+1]=='#'&&tab[j+1][k+1]=='#')
                {
                    tab[j][k]='/';
                    tab[j][k+1]=(char) 92;
                    tab[j+1][k]=(char) 92;
                    tab[j+1][k+1]='/';
                }
            }
        }
        warunek=0;
        for(j=0;j<A;j++)
        {
            for(k=0;k<B;k++)
            {
                if(tab[j][k]=='#') warunek=1;
            }
        }
        cout<<"Case #"<<i+1<<":"<<endl;
        if(warunek==1) cout<<"Impossible"<<endl;
        else
        {
        for(j=0;j<A;j++)
        {
            for(k=0;k<B;k++)
            {
                cout<<tab[j][k];
            }
            cout<<endl;
        }
        }
    }
    return 0;
}
