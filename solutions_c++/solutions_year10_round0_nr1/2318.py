#include <iostream>
#include <fstream>
using namespace std;

int pow(int a,int b)
{
    int res=1;
    for (int i=0;i<b;i++)
        res*=a;
    return res;
}

int main()
{
    ifstream inp;
    ofstream op;
    inp.open("A-large.in");
    op.open("A-large.out");
    int K,N,T;
    inp >> T;
    for (int i=0;i<T;i++)
    {
        inp >> N >> K;
        if (K%pow(2,N)==(pow(2,N)-1)) op << "Case #" << i+1 << ": ON\n";
        else op << "Case #" << i+1 << ": OFF\n";
    }
    
    inp.close();
    op.close();
    return 0;
}