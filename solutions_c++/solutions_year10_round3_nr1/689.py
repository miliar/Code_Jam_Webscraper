// Google Code Jam Round 1C 2010
// Problem A: Rope Intranet
// soimort

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("A-large.in");
    ofstream out("A.out");
    
    int t, n;
    in>>t;
    for(int j=1; j<=t; j++)
    {
        in>>n;
        int a[1000], b[1000];
        for(int i=0; i<n; i++)
            in>>a[i]>>b[i];
        int sum=0;
        for(int x=0; x<n-1; x++)
            for(int y=x+1; y<n; y++)
                if((a[x]>a[y] && b[x]<b[y]) || (a[x]<a[y] && b[x]>b[y]))
                    sum++;
        out<<"Case #"<<j<<": "<<sum<<endl;
    }
    
    return 0;
}
