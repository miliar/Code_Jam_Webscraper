#include<fstream>
using namespace std;
int ten[10] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000};

ifstream cin("C-large.in");
ofstream cout("C-large.out");

int get_len(int n) {
    int cnt = 0;
    while (n!=0) {
        ++cnt;
        n = n/10;
    }
    if (cnt==0) return 1;
    return cnt;
}
int main() {
    int t, i, a, b, j, k, num, cnt, len, d;
    cin>>t;
    for (i=0; i<t; ++i) {
        cin>>a>>b;
        cnt = 0;
        for (j=a; j<=b; ++j) {
            num = j;
            len = get_len(j);

            for (k=0; k<len; ++k) {
                d = num%10;
                num = num/10;
                num += d*ten[len-1];
                if (num == j) break;
                if (num>j && num<=b) {
                    ++cnt;
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<cnt<<endl;
    }
    return 0;
}
