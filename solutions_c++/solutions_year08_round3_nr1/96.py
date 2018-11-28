#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int ii=0;ii<t;ii++) {
        int p, k, l;
        cin >> p >> k >> l;
        vector<int> vi;
        for(int i=0;i<l;i++) {
            int tmp;
            cin >> tmp;
            vi.push_back(tmp);
        }
        if(p*k < l)
            cout << "Case #" << ii+1 << ": " << "Impossible" << endl;
        else {
            sort(vi.begin(), vi.end(), greater<int>());
            int idx = 0;
            long long sum = 0;
            for(int i=0;i<l;i++)
                sum += vi[i]*(i/k+1);
            cout << "Case #" << ii+1 << ": " << sum << endl;
        }
    }

    return 0;
}
