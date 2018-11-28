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

void Count(long M, long N, long A)
{
    /*// Find search interval
    long x2 = A/M;
    long y1 = A/N;

    if(x2 == 0)
        x2 = 1;
    if(y1 == 0)
        y1 = 1;

    for(long x1 = 0; x1<x2; ++x1) {
        for(long y2 = 0; y2<y1; ++y2) {
            long a = x2*y1*2 - (y1*x1+x2*y2+(y1-y2)*(x2-x1));
            if(a == A) {
                cout<<"0 0 "<<x1<<' '<<y1<<' '<<x2<<' '<<y2;
                return;
            }
        }
    } // */

    for(long x2 = 0; x2<=N; ++x2) {
        for(long y1 = 0; y1<=M; ++y1) {
            for(long x1 = 0; x1<=x2; ++x1) {
                for(long y2 = 0; y2<=y1; ++y2) {
                    long a = x2*y1*2 - (y1*x1+x2*y2+(y1-y2)*(x2-x1));
                    if(a == A) {
                        cout<<"0 0 "<<x1<<' '<<y1<<' '<<x2<<' '<<y2;
                        return;
                    }
                }
            }
        }
    }

    cout<<"IMPOSSIBLE";

}

int main(int argc, char* argv[])
{
    bool wait = false;
    string in_file("B-sample.in");
    if(argc > 1)
        in_file = argv[1];
    else
        wait = true;
    ifstream in(in_file.c_str());

    size_t N;
    in>>N;
    for(size_t i = 0; i<N; ++i) {
        // Read data
        long m, n, a;
        in>>n>>m>>a;

        // Output
        cout<<"Case #"<<i+1<<": ";
        
        Count(m, n, a);    
            
        cout<<endl;
    }

    if(wait) {
        int a;
        cin>>a;
    }
    return 0;
}

