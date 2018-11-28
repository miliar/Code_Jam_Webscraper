#include <iostream>
using namespace std;

int tc, ttc;
int n, k, b, t;
int X[100], V[100];
bool is_capable[100];
int not_capable_till[100];

int main() {
    cin >> tc;
    for(int ttc=1; ttc<=tc; ttc++) {
        cin >> n >> k >> b >> t;

        for(int i=0; i<n; i++) cin >> X[i];
        for(int i=0; i<n; i++) cin >> V[i];
        memset(is_capable, 0, sizeof(is_capable));

        int capable_count = 0;
        int last_non_capable = n;


        for(int i=0; i<n; i++)
        {
            is_capable[i] = (X[i] + t*V[i] >= b);
            if (is_capable[i]) capable_count++;
            else last_non_capable = i;
        }

        int count = 0;
        for(int i=0; i<n; i++)
        {
            count += (is_capable[i]?0:1);
            not_capable_till[i] = count;
           // cout << is_capable[i] << " ";
        }
        not_capable_till[n] = count;

        //cout << endl << ">>" << last_non_capable << " " << capable_count << endl;

        int swi = 0;
        int res_count = 0;
        for(int i=n-1; i>=0 && res_count<k; i--) {
            if (is_capable[i]) {
                swi += not_capable_till[last_non_capable] - not_capable_till[i];
                res_count++;
            }
        }
        //cout << ">>" << res_count << endl;

        cout << "Case #" << ttc << ": ";
        if (res_count >= k)
            cout << swi;
        else
            cout << "IMPOSSIBLE";


        cout << endl;
    }
}
