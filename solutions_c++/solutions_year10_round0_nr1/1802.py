#include <vector>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

string SnapperChain(long N, long K)
{
    long tmp = 1;
    for(int i=0; i<N; i++) tmp *= 2;

    if(K % tmp == tmp - 1) return "ON";
    else return "OFF";
}

int main()
{
    string file = "A-large";
    ifstream ifs((file + ".in").c_str());
    ofstream ofs((file + ".out").c_str());
    int T;
    ifs >> T;

    for(int problem=0; problem<T; problem++)
    {
        // input
        string result;
        long N, K;
        ifs >> N >> K;

        result = SnapperChain(N, K);

        // output
        ofs << "Case #" << problem+1 << ": " << result << endl;
        cout << problem+1 << endl;
    }


    return 0;
}