#include <iostream>

using namespace std;

bool possible(int n, int pd, int pg) {
    if (!pd && !pg) return true;
    if (pd && !pg) return false;

    for (int d = 1; d <= n; ++d) {
        if (pd*d%100) continue;
        int dw = pd*d/100;

        if (dw != d && pg == 100) return false;
        if (dw && !pg) return false;

        return true;
    }

    return false;
}

int main() {
    int t;
    cin>>t;
    cin.get();
    for (int i = 1; i <= t; ++i) {
        int n, pd, pg;
        cin>>n>>pd>>pg;

        cout<<"Case #"<<i<<':';
        if (possible(n, pd, pg))
            cout<<" Possible";
        else
            cout<<" Broken";
        cout<<'\n';
    }

    return 0;
}