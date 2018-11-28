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

    int T,i,j,D,G;
    char R[100];
    int P[100];
    long long N;
    ip>>T;
    for(i=0;i<T;i++)
    {
        ip>>N>>D>>G;
        if( ((100/gcd(D,100))<=N || D==0) && (G<100 || G==D) && (G>0 || G==D) )
        {
            cout<<"Case #"<<i+1<<": Possible";
            op<<"Case #"<<i+1<<": Possible";
        } else
        {
            cout<<"Case #"<<i+1<<": Broken";
            op<<"Case #"<<i+1<<": Broken";
        }
        cout<<"\n";
        op<<"\n";
    }
    op.close();
    ip.close();
    //getch();
    return 0;
}
