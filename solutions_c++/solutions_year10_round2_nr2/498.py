#include <iostream>
#include <vector>
#define MAX 200
#define EPS 0.00000001
using namespace std;

int c,n,k,b,t;


int main() {
    cin >> c;
    for (int l=1;l<=c;l++) {
        cin >> n >> k >> b >> t;
        vector<double> pos;
        vector<double> vel;
        
        for (int x=0;x<n;x++) {
            double a; cin >> a; pos.push_back(a);
        }
        for (int x=0;x<n;x++) {
            double a; cin >> a; vel.push_back(a);
        }
        /*
        int mat[MAX][MAX] = {};
        for (int x=0;x<n-1;x++)
            for (int y=x+1;y<n;y++) {
                if (vel[x] > vel[y]) {
                   int tempo = (pos[y]-pos[x]) / (vel[x]-vel[y]);
                   int position = pos[x] + vel[x] * position;
                   if (tempo < t && position < b)
                       mat[x][y] = position;
                   else
                       mat[x][y] = -1;
                }
            }
            */
        
        
        int arrived = 0;
        int swaps   = 0;
        int chick_for_swap = 0;
        for (int x=n-1;x>=0;x--) {
            double tempo = ((double)b - pos[x]) / (vel[x]);
            if (tempo <= (double)t + EPS) {
               //cout << x << " " << tempo  << " (" << (double)tempo << ")  arr: " << arrived <<  " ("  << chick_for_swap << ")" << endl;
               swaps += chick_for_swap;
               arrived ++;
               if (arrived >= k)
                  break;
            }
            else {
                 chick_for_swap++;
            }
        }
        
        if (arrived >= k)
           cout << "Case #" << l << ": " << swaps << endl;
        else
           cout << "Case #" << l << ": " << "IMPOSSIBLE" << endl;
    }
    return 0;
}
