#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    ifstream in("C.in");
    ofstream out("C.out");
    
    double golden = (1.0 + sqrt(5.0))/2.0;
    int T;
    in >> T;
    
    for (int tc = 1; tc <= T; ++tc)
    {
        int A1, A2, B1, B2;
        in >> A1 >> A2 >> B1 >> B2;
        
        long long total = 0;
        
        for (int i = A1; i <= A2; ++i)
        {
            int lwrBound = min(B2, int(floor(double(i)/golden)));
            int uprBound = max(B1, int(ceil(double(i)*golden)));
            
            if (lwrBound >= B1)
               total += (lwrBound - B1 + 1);
            if (uprBound <= B2)
               total += (B2 - uprBound + 1);
        }
        
        out << "Case #" << tc << ": " << total << endl;
    }
    
    in.close();
    out.close();
    return 0;
}
