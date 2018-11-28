#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp1(long long a, long long b) {
    if (a!=b) return a<b;
    else return true;
}

bool cmp2(long long a, long long b) {
    if (a!=b) return a>b;
    else return true;
}

int main() {
    int cases;
    cin >> cases;
    for(int ccases=0; ccases<cases; ccases++) {
        int n; long long tmp;
        cin >> n;
        vector<long long> A, B;

        for(int i=0; i<n; i++) {
            cin >> tmp;
            A.push_back(tmp);
        }

        for(int i=0; i<n; i++) {
            cin >> tmp;
            B.push_back(tmp);
        }
    
        sort(A.begin(), A.end(), cmp1);
        sort(B.begin(), B.end(), cmp2);

        long long res=0;
        for(int i=0; i<n; i++) {
            res += A[i] * B[i];
        }
        
        cout << "Case #" << ccases+1 << ": " << res << endl;
    }

}
