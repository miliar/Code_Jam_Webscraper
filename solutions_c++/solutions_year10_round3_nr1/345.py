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
    int t,n;
    infile>>t;
    for (int i=0;i!=t;++i)
    {
        int res=0;
        infile>>n;
        vector<int> a(n);
        vector<int> b(n);
        for (int j=0;j!=n;++j)
        {
            infile>>a[j]>>b[j];
        }
        for (int j=0;j!=n-1;++j)
            for (int k=j+1;k!=n;++k)
            {
                if ((a[j]<a[k] && b[j]>b[k]) || (a[j]>a[k] && b[j]<b[k]))
                {
                    ++res;
                }
            }
            outfile<<"Case #"<<i+1<<": "<<res<<endl;
    }
    infile.close();
    outfile.close();
    return 0;
}