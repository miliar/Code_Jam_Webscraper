#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("b.in");
ofstream fout("b.out");

int T;

int main()
{
    fin>>T;
    int N,M,A,k;
    for (int z = 1; z<=T; z++)
    {
        fin>>N>>M>>A;
        k =1;
        if (N*M < A )
        {
             fout<<"Case #"<<z<<": IMPOSSIBLE\n";
             continue;
        }
        for ( int x1 = 0; x1 <= N && k; x1++)
            for ( int y1 = 0; y1 <=M && k; y1++)
                for ( int x2 = 0; x2 <= N && k; x2++)
                    for ( int y2 = 0; y2 <=M && k; y2++)
                        for ( int x3 = 0; x3 <= N && k; x3++)
                            for ( int y3 = 0; y3 <=M && k; y3++)
                            {
                                int a = abs( x1*y2 + x2*y3 + x3*y1 - x3*y2 - x2*y1 - x1*y3);
                                if ( a == A )
                                {
                                    k = 0;
                                    fout<<"Case #"<<z<<": "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<x3<<" "<<y3<<"\n";
                                }


                            }
        if ( k )
            fout<<"Case #"<<z<<": IMPOSSIBLE\n";

    }



}
