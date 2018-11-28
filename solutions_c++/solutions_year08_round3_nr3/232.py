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

vector<long long> data;

long long Count(vector<long long> &limits, int step = 0)
{
    size_t sz = limits.size();

    if(step == 0) {
        data.clear();
        data.resize(sz, 0);
    }

    if(step == sz - 1)
        return 1;

    if(data[step] > 0)
        return data[step];

    int c = limits[step];

    long long res = 1;

    for(size_t i = step+1; i<sz; ++i) {
        if(limits[i] > c)
            res = ( res + Count(limits, i))  % 1000000007;
    }

    data[step] = res;

    if(step == 0) {
        for(size_t i = 1; i<sz; ++i) {
            res = (res + Count(limits, i)) % 1000000007;
        }
    }

    return res;
}


int main(int argc, char* argv[])
{
    bool wait = false;
    string in_file("C-sample.in");
    if(argc > 1)
        in_file = argv[1];
    else
        wait = true;
    ifstream in(in_file.c_str());

    int N;
    in>>N;
    for(size_t i = 0; i<N; ++i) {
        // Read data
        long long m, n, X, Y, Z;
        in>>n>>m>>X>>Y>>Z;

        vector<long long> limits;
        vector<long long> A;
        for(size_t j = 0; j<m; j++)
        {
            long long a;
            in>>a;
            A.push_back(a);
        }

        for(size_t j = 0; j<n; j++)
        {
            limits.push_back(A[j%m]);
            A[j%m] = (X * A[j%m] + Y*(j+1)) % Z;
        }

        // Output
        cout<<"Case #"<<i+1<<": "<<Count(limits)<<endl;
    }

    if(wait) {
        int a;
        cin>>a;
    }
    return 0;
}