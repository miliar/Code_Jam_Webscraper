#include <vector>
#include <stack>
#include <map>
#include <iostream>
#include <fstream>
#include <strstream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int Count(int l_on_key, int keys_count, int letters_count, vector<int> &letters, int step, int s_i)
{
    sort(letters.rbegin(), letters.rend());
    vector<int>::iterator v = letters.begin();
    int res = 0;
    for(size_t n = 1; n<=l_on_key; ++n) {
        for(size_t j = 0; j<keys_count; ++j) {
            res += *v * n;
            ++v;
            if(v == letters.end()) break;
        }
        if(v == letters.end()) break;
    }
    return res;
    
}

int main(int argc, char* argv[])
{
    bool wait = false;
    string in_file("A-sample.in");
    if(argc > 1)
        in_file = argv[1];
    else
        wait = true;
    ifstream in(in_file.c_str());

    int N;
    in>>N;
    for(size_t i = 0; i<N; ++i) {
        // Read data
        vector<int> l;
        int P, K, L, ll;
        in>>P>>K>>L;
        for(size_t j = 0; j<L; ++j)
        { in>>ll; l.push_back(ll); }

        // Output
        cout<<"Case #"<<i+1<<": "<<Count(P, K, L, l, 0, 0)<<endl;
    }

    if(wait) {
        int a;
        cin>>a;
    }
    return 0;
}

