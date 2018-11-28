#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream be("D-large.in");
    ofstream ki("large.ki");
    int t;
    be>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        be>>n;
        int s=0;
        for(int j=0;j<n;j++)
        {
            int x;
            be>>x;
            if(x==j+1)
            {
                s++;
            }
        }
        ki<<"Case #"<<(i+1)<<": "<<n-s<<".000000"<<endl;
    }
    be.close();
    ki.close();
    return 0;
}
