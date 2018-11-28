#include<iostream>
#include<queue>

using namespace std;

typedef pair<char,int> PCI;
PCI ord[101];
queue<int> B,O;
int T,n,m;
char ch;

int main() {
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> n;
        for (int i = 1; i <= n; i++) {
            cin >> ch >> m;
            if (ch == 'B') B.push(m);
            else O.push(m);
            ord[i] = make_pair(ch,m);
        }
        int k = 1, o = 1, b = 1, time = 0;
        while (k <= n) {
              PCI p = ord[k];
              time++;
              int nO = O.front();
              int nB = B.front();
              if (o < nO) o++;
              else 
              if (o > nO) o--;
              else
              if ('O' == p.first && p.second == o) {
                      k++;
                      O.pop();
                      }
              if (b < nB) b++;
              else 
              if (b > nB) b--;
              else
              if ('B' == p.first && p.second == b) {
                      k++;
                      B.pop();
                      }
              }
              cout << "Case #" << t << ": " << time;
              if (t < T) cout << endl;
    }
    fclose(stdout);
    return 0;
}
