#include <iostream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; i++)

#define FORI(i,b,a) for(int i = b - 1 ; i >= a ; i--)

#define LL long long
#define ULL unsigned long long
#define UI unsigned int

#define VI vector<int>
#define VS vector<string>

#define pb push_back

int main() {
    int tc,n;
    cin>>tc;
    FOR(i,1,tc+1) {
        cin>>n;
        int min = 100000001;
        LL sum = 0;
        int total = 0;
        int num;
        FOR(j,0,n) {
            cin>>num;
            total = total ^ num;
            sum = sum + num;
            if(min > num) min = num;
        }
        printf("Case #%d: ",i);
        if(total != 0) cout << "NO" << endl;
        else {
            cout << sum - min << endl;
        }
    }
    return (0);
}
