#include <iostream>
#include <list>
#include <algorithm>

using namespace std;

int main(int argc, char** argv) {
    long N; cin>>N;
    for(long c = 0; c < N; ++c) {
        long candies; cin>>candies;
        long xor_sum = 0l;
        long sum = 0;
        long tmp;
        long min = 0;
        long min_found = 0;
        for(long i = 0; i < candies; ++i) {
            cin>>tmp;
            if(!min_found || min > tmp) {
                min = tmp;
                min_found = 1;
            }
            xor_sum ^= tmp;
            sum += tmp;
        }
        if (xor_sum) {
            cout<<"Case #"<<c+1<<": "<<"NO"<<endl;
        } else {
            cout<<"Case #"<<c+1<<": "<<sum-min<<endl;
        }
    }
    return 0;
}