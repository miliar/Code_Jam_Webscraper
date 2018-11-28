#include <vector>
#include <iostream>
#include <cassert>

using namespace std;

typedef vector<long> VecLong;
typedef vector<vector<long> > VecVecLong;

VecVecLong allsum(const VecLong &v) {
    VecVecLong allsums;
    for(int i = 0; i < v.size(); ++i) {
        VecLong sums;
        long total = 0;
        for(int j = 0; j < v.size(); ++j) {
            total += v[(j + i) % v.size()];
            sums.push_back(total);
        }
        allsums.push_back(sums);
    }
    return allsums;
}

long count(VecVecLong &allsums, int k, int &pointer) {
    VecLong &v = allsums[pointer];
    int low = 0;
    int high = v.size() - 1;

    while(low < high) {
        int mid = (low + high) / 2;
        long midVal = v[mid];

        if (midVal < k) {
            low = mid + 1;
        } else if (midVal > k) {
            high = mid - 1;
        } else {
            pointer = (mid + pointer + 1) % v.size();
            return k;
        }
    }
    int idx = min(max(low, high), (int)v.size() - 1);
    while(v[idx] > k)
        idx--;
    pointer = (idx + pointer + 1) % v.size();
    return v[idx];
}

void print(VecLong &values, int pointer) {
    for(int i = 0; i< values.size(); ++i) {
        cout << values[(pointer + i) % values.size()] << " ";
    }
    cout << endl;
}

long solve(int r, int k, int n, VecLong &values) {
    VecVecLong allsums = allsum(values);

    long money = 0;
    int pointer = 0;

    for (int i = 0; i < r; ++i) {
        money += count(allsums, k, pointer);
        //print(values, pointer);
    }

    return money;
}

int main() {
    int ncases;

    cin >> ncases;

    for(int i = 0; i < ncases; ++i) {
        int r, k, n, v, result;

        cin >> r >> k >> n;
        VecLong values;
        for (int j = 0; j < n; ++j) {
            cin >> v;
            values.push_back(v);
        }
        cout << "Case #" << (i + 1) << ": "<< solve(r, k, n, values) << endl;
    }
}
