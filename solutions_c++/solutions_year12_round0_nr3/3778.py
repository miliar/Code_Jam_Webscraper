#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <set>

using namespace std;

int pow(int x, int y)
{
    int ret = 1;
    while(y--) ret *= x;
    return ret;
}

int solve(int A, int B)
{
    set<pair<int, int> > s;
    for(int n = A; n < B; n++) {
        vector<int> v;
        for(int t = n; t; t /= 10)
            v.push_back(t%10);
        for(int x = 0; x < v.size(); x++) {
            int m = 0;
            for(int i = v.size() - 1 - x; i >= 0; i--)
                m += v[i] * pow(10, i+x);
            for(int i = x; i > 0; i--) 
                m += v[v.size()-i] * pow(10, x - i);
         
            if(m <= B && n < m) {
                s.insert(pair<int, int>(n,m));
                //cout << "(n,m)=" << n << "," << m << endl;
            }

        } 
    }

    return s.size();
}

int main()
{
    int n;
    cin >> n;

    for(int i = 0; i < n; i++) {
        int A, B;
        cin >> A >> B;
        cout << "Case #" << i+1 << ": " << solve(A, B) << endl;
    }
    
    return 0;
}

