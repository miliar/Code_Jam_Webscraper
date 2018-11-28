#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char **argv)
{
    int T, N, K;
    int case_no;
    int rem;
    long long loop_len;
    if (argc < 2) {
        cerr << "Please provide input file\n";
        return 1;
    }
    
    ifstream in(argv[1]);
    ofstream out((argc < 3) ? "sn_chain.out" : argv[2]);
    in >> T;
    for (case_no = 1; case_no <= T; case_no++) {
        in >> N >> K;
        //cout << "N = " << N << endl;
        loop_len = 1 << N;
        //cout << "Checking with " << loop_len << endl;
        rem = (K+1) % loop_len;
        out << "Case #" << case_no << ": " << (rem == 0 ? "ON" : "OFF") << endl;
    }

    in.close();
    out.close();   
        
    return 0;
}
