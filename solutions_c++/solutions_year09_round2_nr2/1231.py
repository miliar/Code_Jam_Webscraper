#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    for(int k=0; k<N; ++k) {
        string num;
        cin >> num;
        int pos = -1;
        for(int i=num.size()-1; i>=0; --i) {
            bool flag = false;
            char min = '9';
            string tnum;
            string sol;
            for(int j=i+1; j<num.size(); ++j) {
                tnum = num;
                if(tnum[j]>num[i] && tnum[j]<=min) {
                    min = tnum[j];
                    char t = tnum[i];
                    tnum[i] = tnum[j];
                    tnum[j] = t;
                    pos = i;
                    sol = tnum;
                    flag = true;
                }
            }
            if(flag) {
                num = sol;
                break;
            }
        }
        if(pos==-1) {
            num += "0";
            sort(num.begin(),num.end());
            for(int i=1; i<num.size(); ++i) {
                if(num[i]!='0') {
                    num[0] = num[i];
                    num[i] = '0';
                    break;
                }
            }
        }
        if(pos<num.size()-1) sort(num.begin()+pos+1,num.end());
        cout << "Case #" << k+1 << ": " << num << endl;
    }
    return 0;
}
