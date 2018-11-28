#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool ishappy(int n, int b, vector<int>& hist)
{
    if(n == 1)
        return true;
    int sum = 0;
    while(n) {
        int m = n%b;
        sum += m*m;
        n /= b;
    }
    if(find(hist.begin(), hist.end(), sum) == hist.end())
        hist.push_back(sum);
    else
        return false;
    return ishappy(sum, b, hist);
}

int main()
{
    int n;
    cin >> n;
    string s;
    getline(cin, s);
    for(int cnt=1;cnt<=n;cnt++) {
        string s;
        getline(cin, s);
        istringstream iss(s);
        vector<int> vi;
        while(1) {
            int b;
            iss >> b;
            if(!iss)
                break;
            
            vi.push_back(b);
        }
        for(int i=2;;i++) {
            bool ok = true;
            for(int j=0;j<vi.size();j++) {
                vector<int> h;
                if(!ishappy(i, vi[j], h)) {
                    ok = false;
                    break;
                }
            }
            if(ok) {
                cout << "Case #" << cnt << ": " << i << endl;
                break;
            }
            else
                continue;
        }
    }
    
    return 0;
}
