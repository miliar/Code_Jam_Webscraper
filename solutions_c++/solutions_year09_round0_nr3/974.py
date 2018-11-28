#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main() {
    int N;
    string s, key="welcome to code jam";

    cin >> N; getline(cin, s);
    for(int n=1;n<=N;n++) {
        int T[502][20]={{0,},};

        getline(cin, s);

        for(int i=0;i<s.size();i++)
            if(s[i]==key[0]) T[i][0]=1;

        for(int i=0;i<s.size();i++) {
            for(int j=1;j<19;j++) {
                if(s[i]==key[j]) {
                    for(int k=0;k<i;k++) T[i][j] = (T[i][j]+T[k][j-1]) % 10000;
                }
            }
        }

        int cnt=0;
        for(int i=0;i<s.size();i++) cnt = (cnt+T[i][18]) % 10000;
        cout << "Case #" << n << ": " << setfill('0') << setw(4) << cnt << endl;
    }

    return 0;
}
