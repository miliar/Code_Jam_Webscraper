#include <iostream>
using namespace std;

char ch[100][100];
double wp[100];
double owp[100];
double oowp[100];

void foo() {
    int n;
    cin>>n;
    for (int i=0;i<n;i++) for (int j=0;j<n;j++) cin>>ch[i][j];

    // calculate the WP
    for (int i=0;i<n;i++) {
        int wc = 0, lc = 0;
        for (int j=0;j<n;j++) {
            if (ch[i][j] == '1') wc++;
            else if (ch[i][j] == '0') lc++;
        }
        int tc = wc + lc;
        if (tc > 0) {
            wp[i] = 1.0 * wc / tc;
        } else wp[i] = 0;
    }

    // Now, calculate the OWP
    for (int i=0;i<n;i++) {
        int matches = 0;
        double val = 0.0;
        for (int j=0;j<n;j++) {
            if (ch[i][j] != '.') {
                // There was some match between i & j. So, calculate the OWP
                int wc = 0, lc = 0;
                for (int k=0;k<n;k++) { 
                    if (i != k) {
                        if (ch[j][k] == '0') lc++;
                        else if (ch[j][k] == '1') wc++;
                    }
                }
                int tc = wc + lc;
                matches++;
                if (tc > 0) 
                    val += (wc * 1.0 / tc);
            }
        }
        if (matches == 0) owp[i] = 0;
        else owp[i] = val / matches;
    }
    for (int i=0;i<n;i++) {
        double val = 0.0;
        int matches = 0;
        for (int j=0;j<n;j++) {
            if (ch[i][j] != '.')  {
                matches ++;
                val += owp[j];
            }
        }
        if (matches > 0) oowp[i] = val / matches;
        else oowp[i] = 0;
    }
    for (int i=0;i<n;i++) {
        cout<<(0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i])<<endl;
    }
}
int main() {
    int testcases;
    cin>>testcases;
    for (int i=0;i<testcases;i++) {
        cout<<"Case #"<<(i+1)<<":"<<endl;
        foo();
    }
    return 0;
}
