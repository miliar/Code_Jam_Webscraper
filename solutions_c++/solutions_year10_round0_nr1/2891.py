#include <iostream>

using std::cin;
using std::cout;
using std::endl;


int main()
{
    int T_in, N_in, K_in;
    cin >> T_in;
    int period;
    int CaseNum = 1;
    while(CaseNum <= T_in) {
        cin >> N_in >> K_in;
        if((K_in&0x01) == 0)
            cout << "Case #" << CaseNum << ": OFF" << endl;
        else {
            period = (1 << N_in);
            while(K_in > period) K_in -= period;
            if(K_in  == (period -1))
//            if( (K_in % (1<<N_in)) == ((1<<N_in) -1))
                cout << "Case #" << CaseNum << ": ON" << endl;
            else
                cout << "Case #" << CaseNum << ": OFF" << endl;
        }
        CaseNum++;
    }
    return 0;
}
