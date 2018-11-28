#include <iostream> 
#include <fstream>

using namespace std;

int GCD(int a, int b)
{  
    while( 1 )
    {
        a = a % b;
        if( a == 0 ) return b;
        b = b % a;
        if( b == 0 ) return a;
    }
}

int a[10001];
int gcd, lcm;
void main()
{   ofstream outfile( "C-small-attempt0.out" );
    ifstream infile( "C-small-attempt0.in" );
    int T, N, L, H, i, j, k, l, t ;
    bool gflag, lflag,flag;
    infile>>T;
    for (i=1;i<=T;i++)
    {
        infile>>N>>L>>H;
        for (j=0;j<N;j++) infile>>a[j];
        gcd=lcm=1;
        
        for (k=L;k<=H;k++)
        {   flag=true;
            for(j=0;j<N;j++)
            {
                if (!((k%a[j]==0)||(a[j]%k==0)))
                {flag=false; break;}
            }
            if (flag==true)
            { break;
            }
        }
        outfile<<"Case #"<<i<<": ";
        if (flag==true) {outfile<<k<<endl;}else{outfile<<"NO\n";}
    }
 };
    