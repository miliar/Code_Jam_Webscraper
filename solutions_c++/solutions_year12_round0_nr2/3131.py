#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for (int i=1;i<=t;i++){
        int t1,t2,t3,t4=0,t5=0,t6;
        vector<int> vect1;
        cin >> t1 >> t2 >> t3;
        for (int j=0;j<t1;j++) {
            int value;
            cin >> value;
            vect1.push_back(value);
        }
        for (int j=0;j<t1;j++){
            if (vect1[j] >= 3*t3-2) t4++;
            else if (vect1[j] >= 3*t3-4 && vect1[j] > 0) t5++;

        }
        if (t3==0) t6=t1;
        else {
            t6=t4+min(t5,t2);
        }
        cout << "Case #" << i << ": " << t6 << "\t1";
    }
    return 0;
}