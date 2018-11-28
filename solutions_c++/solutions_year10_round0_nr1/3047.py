#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream infile("in.txt");
    ofstream outfile("output.txt");
    int T,N,K;
    infile>>T;
    for (int i=0;i<T;++i)
    {
        infile>>N>>K;
        unsigned long temp=1;
        temp=temp<<N;
        ++K;
        if (K % temp ==0)
        {
            outfile<<"Case #"<<i+1<<": ON"<<endl;
        }
        else
        {
            outfile<<"Case #"<<i+1<<": OFF"<<endl;
        }
    }
    infile.close();
    outfile.close();
    return 0;
}