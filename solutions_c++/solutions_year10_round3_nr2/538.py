// Google Code Jam Round 1C 2010
// Problem B: Load Testing
// soimort

#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
    ifstream in("B-small-attempt0.in");
    ofstream out("B.out");
    
    int t, l, p, c;
    in>>t;
    for(int i=1; i<=t; i++)
    {
        in>>l>>p>>c;
        double m=(log(p)-log(l))/log(c);
        if(abs(m-round(m))<1e-4) m=round(m);
        int s=ceil(log(m)/log(2));
        if(s<0) s=0;
        
        out<<"Case #"<<i<<": "<<s<<endl;
    }
    
    return 0;
}
