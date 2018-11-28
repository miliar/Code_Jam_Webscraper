#include <iostream>

using std::cin;
using std::cout;
using std::endl;


int main()
{
    long long T_in, L_in, P_in, C_in;
    cin >> T_in;
    int cnt1, cnt2;
    int CaseNum = 1;
    while(CaseNum <= T_in) {
        cnt1 = cnt2 = 0;
        cin >> L_in >> P_in >> C_in;
        L_in *= C_in;
        while(L_in < P_in) {
            cnt1++;
            L_in *= C_in;
        }

        while(cnt1 > 0) {
            cnt2++;
            cnt1 /= 2;
        }

        cout << "Case #" << CaseNum << ": " << cnt2 << endl;
        CaseNum++;
    }
    return 0;
}
