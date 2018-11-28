#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

int main(int argc, char const* argv[])
{
    int T;
    cin >> T;
    for (int i=0 ; i<T; i++) {
        int A,B;
        cin >> A >>B;
        cout << "Case #" << i+1 << ": ";
        vector<double> p;
        double tmp;
        for (int j = 0; j < A; j++) {
            cin >> tmp;
            p.push_back(tmp);
        }
        tmp=0.0;
        //先頭j個があっていたとき
        //それぞれの確率
        vector<double> tries;
        for (int j = 0; j < A+1; j++) {
            int l;
            tmp = 1.0;
            for (l = 0; l < j; l++) {
                tmp *= p[l];
            }
            tmp *= (1.0-p[l]);
            tries.push_back(tmp);
        }
        //backspace * j
        //less than k is correct
        int tmpans;
        double ans = 100000000000;
        double anscand = 0;
        int size = tries.size();
        for (int j = 0; j < A+1; j++) {
            anscand =0;
            for (int k = 0; k < size; k++) {
                tmpans = j*2 + B - A + 1;
                if(A-j>k){
                    tmpans += B+1;
                }
                anscand += tmpans * tries[k];
            }
            if (anscand < ans) {
                ans = anscand;
            }
        }
        anscand = double(B + 2);
        if (anscand < ans) {
            ans = anscand;
        }
        std::cout.setf(std::ios_base::fixed,std::ios_base::floatfield);
        cout << setprecision(6) <<
            ans << endl;
    }
    return 0;
}
