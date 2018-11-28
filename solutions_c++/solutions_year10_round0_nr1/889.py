#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    ifstream in("A.in");
    ofstream out("A.out");
    
    int T;
    in >> T;
    
    for (int tc = 1; tc <= T; ++tc)
    {
        int N, K;
        in >> N >> K;
        K = (K+1) % (1<<N);
        out << "Case #" << tc << ": ";
        if (K == 0)
           out << "ON" << endl;
        else
           out << "OFF" << endl;
    }
    
    in.close();
    out.close();
    return 0;
}
