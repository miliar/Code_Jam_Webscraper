#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[]) {
    int cases = 0;
    cin >> cases;
    int a;
    int b;
    for(int i = 1; i <= cases; ++i) {
        cin >> a;
        cin >> b;
        vector<double> prob;
        double full = 1.0;
        for(int j = 0; j < a; ++j) {
            double temp;
            cin >> temp;
            prob.push_back(temp);
            full *= temp;
        }
        int probsize = prob.size()-1;
        double left = b-a;
        double enterNow = 1 + b + 1;
        double finishNow = full*(left+1) + (left+2+b)*(1-full);
        double allbackspace = a+b+1;
        vector<double> therest(a);
        for(int here = 0; here < a; ++here) {
            int backspaces = here + 1;
            double localp;
            double localfull = full;
            for(int shave = 0; shave < backspaces; ++shave) {
                localfull /= prob[probsize-shave];
            }
            therest[here] = localfull*(left+(backspaces*2)+1) + (left+(backspaces*2)+2+b)*(1-localfull);
        }
        therest.push_back(enterNow);
        therest.push_back(finishNow);
        therest.push_back(allbackspace);
        cout << "Case #" << i << ": " << fixed << setprecision(6) << *min_element(therest.begin(), therest.end()) << endl;
    }
    return 0;
}
