#include <iostream>
#include <vector>

using namespace std;

int calc(int n, int s, int p, vector<int>& pts) {
    int line1 = max(3*p-2, 0);
    int line2 = max(3*p-4, 0);

    int count_line1 = 0;
    int count_line2 = 0;

    for (int i = 0; i < pts.size(); ++i) {
        if (pts[i] == 0 && p > 0)
           continue; 
        else if (pts[i] >= line1) 
            ++count_line1;
        else if (pts[i] >= line2) 
            ++count_line2;
    }

    return count_line1 + min(count_line2, s);
}

int main() {
    int m;
    cin >> m;
    for (int i = 0; i < m; ++i) {
        int n, s, p;
        cin >> n >> s >> p;
        vector<int> pts;
        for (int j = 0; j < n; ++j) {
            int t;
            cin >> t;
            pts.push_back(t);
        } 

        cout << "Case #" << i+1 << ": " << calc(n,s,p,pts) << endl;
    }

    return 0;
}

