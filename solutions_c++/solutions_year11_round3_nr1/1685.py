#include <iostream>
#include<fstream>
#include <conio.h>
using namespace std;

int gcd(int a, int b)
{
    while( 1 )
    {
        a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

        if( b == 0 )
			return a;
    }
}

int main()
{
    ofstream op("A.op");
	ifstream ip("A.ip");

    int T,i,j,k,C,R,flag;
    char P[100][100];
    
    ip>>T;
    
    for(i=0;i<T;i++)
    {
        ip>>R>>C;
        //cout<<R<<C;
        flag=1;
        for(j=0;j<R;j++)
        for(k=0;k<C;k++)
        ip>>P[j][k];
        
        for(j=0;j<R;j++)
        for(k=0;k<C;k++)
        if(P[j][k]=='#')
        if(P[j][k+1]=='#' && P[j+1][k]=='#' && P[j+1][k+1]=='#' && j!=R-1 && k!=C-1)
        {
            P[j][k]='/';
            P[j][k+1]='\\';
            P[j+1][k]='\\';
            P[j+1][k+1]='/';
        } else 
        {
            flag=0;
        }
        
        if(flag)
        {
            cout<<"Case #"<<i+1<<":\n";
            op<<"Case #"<<i+1<<":\n";
            
            for(j=0;j<R;j++)
            {
                for(k=0;k<C;k++)
                {
                    cout<<P[j][k];
                    op<<P[j][k];
                }
                
                cout<<"\n";
                op<<"\n";
            }
        } else
        {
            cout<<"Case #"<<i+1<<":\nImpossible";
            op<<"Case #"<<i+1<<":\nImpossible";
        }
        cout<<"\n";
        op<<"\n";
    }
    op.close();
    ip.close();
    getch();
    return 0;
}
