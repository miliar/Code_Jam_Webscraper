#include<iostream>
#include<string>
#include<fstream>
#include<sstream>
using namespace std;

const string goal = "welcome to code jam";
const int lg = 19;
int F[501][20];
int N;

int main() {
    ifstream cin("input.in");
    string str;
    cin >> N; 
    getline(cin, str);
    for (int i=0;i<N;++i) {
        getline(cin, str);
        int len = str.size();

        memset(F, 0, sizeof(F));
        F[0][0] = 1;
        for (int j=0;j<len;++j) {
            F[j+1][0] = 1;
            for (int k=0;k<lg;++k) {
                F[j+1][k+1] = F[j][k+1];
                if (str[j] == goal[k])
                    F[j+1][k+1] = (F[j+1][k+1] + F[j][k]) % 10000;
            }
        }
    
        ostringstream sout;
        sout << F[len][lg];
        string ans = sout.str();
        while (ans.size() < 4) ans = "0" + ans;
        printf("Case #%d: %s\n", i+1, ans.c_str());
    }
    return 0;
}
