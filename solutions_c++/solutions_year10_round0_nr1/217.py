#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

string problem = "A";

int main(int argc, char** argv)
{
    if (argc == 2)
    {
        problem = argv[1];
        string last3 = problem.substr(problem.size() - 3, 3);
        if (last3 == ".in")
            problem = problem.substr(0, problem.size() - 3);
    }

    string inPath = problem + ".in";
    string outPath = problem + ".out";

    cout << "doing " << inPath << endl;
    cout << "to    " << outPath << endl;
    
    freopen(inPath.data(), "r", stdin);
    freopen(outPath.data(), "w", stdout);

    int Ti,T;
    cin >> T;
    for (Ti = 0; Ti < T; ++Ti)
    {
        int N,K;
        cin >> N >> K;
        int ans;
        for (ans = 0; ans < 32; ++ans)
        {
            if (!(K & 1)) break;
            K >>= 1;
        }
        
        cout << "Case #" << Ti+1 << ": " 
             << (ans >= N ? "ON" : "OFF")
             << endl;
    }
    return 0;
}
