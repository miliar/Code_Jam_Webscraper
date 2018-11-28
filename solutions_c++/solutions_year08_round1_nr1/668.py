#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long int LLI;

main() {
    LLI nc;
    cin >> nc;
    for (LLI ic=1; ic<=nc; ic++) {
        LLI nv;
        cin >> nv;
        vector<LLI> v1;
        vector<LLI> v2;
        for (LLI i=0; i<nv; i++) {
            LLI v;
            cin >> v;
            v1.push_back(v);
        }
        for (LLI i=0; i<nv; i++) {
            LLI v;
            cin >> v;
            v2.push_back(v);
        }
        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());
        reverse(v2.begin(), v2.end());
        LLI tot = 0;
        for (LLI i=0; i<v1.size(); i++) {
            tot += v1[i]*v2[i];
        }
        cout << "Case #" << ic << ": " << tot << endl;
    }
}
