#include <iostream>
#include <vector>
#include <iterator>

using namespace std;

int main() {
    int n;
    cin>>n;
    for (int i = 1; i <= n; ++i) {
        int m;
        cin>>m;
        vector<size_t> vec;
        while (m--)
            *back_inserter(vec) = *istream_iterator<size_t>(cin);

        cout<<"Case #"<<i<<':';
        size_t v = 0;
        for (size_t j = 0; j < vec.size(); ++j)
            v ^= vec[j];
        if (v) cout<<" NO";
        else {
            unsigned long long sum = 0;
            size_t min = vec[0];
            for (size_t j = 0; j < vec.size(); ++j) {
                sum += vec[j];
                if (vec[j] < min) min = vec[j];
            }
            cout<<' '<<sum - min;
        }
        cout<<'\n';
    }

    return 0;
}
