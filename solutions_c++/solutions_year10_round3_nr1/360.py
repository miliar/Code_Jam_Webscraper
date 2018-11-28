#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int A_in[1000], B_in[1000];

int main()
{
    int T_in, N_in;
    cin >> T_in;
    int intersection;
    int CaseNum = 1;
    while(CaseNum <= T_in) {
        cin >> N_in;
        for(int i = 0; i<N_in; i++)
            cin >> A_in[i] >> B_in[i];

        intersection = 0;
        for(int i = 0; i < N_in; i++)
            for(int j = i+1; j < N_in; j++ ) {
                if ((A_in[i] < A_in[j]) && (B_in[i] > B_in[j]))
                    intersection++;
                if ((A_in[i] > A_in[j]) && (B_in[i] < B_in[j]))
                    intersection++;
            }
        cout << "Case #" << CaseNum << ": " << intersection << endl;
        CaseNum++;
    }
    return 0;
}
