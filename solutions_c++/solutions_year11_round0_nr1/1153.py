#include <iostream>
using namespace std;
int main()
{
    int n,t,i,j,p,bn,on,ototal,btotal;
    char color;
    
    cin>>t; 
    for (i=1;i<=t;i++)
    {
        cin>>n;
        on=1;bn=1;btotal=0;ototal=0;
        for (j=1;j<=n;j++)
        {
            cin>>color>>p;
            if (color=='O') 
            {
                ototal+=(abs(p-on));
                if (ototal<btotal) ototal=btotal;
                on=p;
                ototal++;
            }
            else
            {
                btotal+=(abs(p-bn));
                if (btotal<ototal) btotal=ototal;
                bn=p;
                btotal++;
            }
        }
        if (ototal<btotal) ototal=btotal;
        cout<<"Case #"<<i<<": "<<ototal<<endl;
    }
}
