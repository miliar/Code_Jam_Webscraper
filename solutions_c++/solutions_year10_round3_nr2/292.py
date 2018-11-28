#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <vector>
using namespace std;

int main()
{
    ifstream infile("input.txt");
    ofstream outfile("output.txt");
    long long t,l,p,c;
    infile>>t;
    for (int i=0;i!=t;++i)
    {
        int res=0;
        int temp;
        infile>>l>>p>>c;
        if (p%l)
        {
            temp=p/l+1;
        }
        else
        {
            temp=p/l;
        }
        while (c<temp)
        {
            ++res;
            c=c*c;
        }
        outfile<<"Case #"<<i+1<<": "<<res<<endl;
    }
    infile.close();
    outfile.close();
    return 0;
}