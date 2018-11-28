#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

int m, n;
vector <double> valores;
double probs[2000][4];

void brute(int pos, double acu) {
    if (pos == n) {
        valores.push_back(acu);
        return;
    }
    brute(pos+1,acu*probs[pos][0]);
    brute(pos+1,acu*probs[pos][1]);
    brute(pos+1,acu*probs[pos][2]);
    brute(pos+1,acu*probs[pos][3]);
}

int main(){
    int teste;
    int t;
    int i, j;
    scanf("%d", &t);
    for (teste=0;teste<t;teste++) {
        scanf("%d %d", &m, &n);
        for (i=0; i<n; i++) {
            for (j=0; j<4; j++) {
                scanf("%lf", &probs[i][j]);
            }
        }
        valores.clear();
        brute(0, 1.0);
        double resp = 0;
        sort(valores.begin(),valores.end());
        int total = (1<<(2*n));
        if (m > total) m = total;
        for (i=0; i<m; i++){
            resp += valores[total-1-i];
        }
        printf("Case #%d: %lf\n", teste+1, resp);
    }
    return 0;
}
