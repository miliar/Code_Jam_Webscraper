#include <iostream>
#include <cstring>

using namespace std;

char diamond[51 * 2][51 * 2];

int main() {
    int T, i, j, k, n, m;
    cin >> T;
    for(i= 1; i <= T; i++) {
        bzero(diamond, sizeof(diamond));
        cin >> k;
        cin.getline(diamond[j], 52*2);
        for(j= 0; j < 2*k-1; j++)
            cin.getline(diamond[j], 51*2);

        int hth= 0;
        int vth= 0;
        int tmp= 0;
        for(j= 1; j < k; j++) {
            bool s= true;
            for(m= 0; m< j; m++) {
                for(n= k-m-1; n< m+k; n+=2) {
                    if(diamond[m][n] != diamond[2*j-m][n])
                    {
                        s= false;
                        break;
                    }
                }
                if(s== false)
                    break;
            }
            if(s)
                tmp= j;
        }
        hth= tmp;

        for(j= 2*k - 2; j >= k; j-- ) {
            bool s= true;
            for(m= 2*k-2 ; m> j; m-- ) {
                for(n= m - k + 1; n< 3*k-2-m; n+=2) {
                    if(diamond[m][n] != diamond[2*j-m][n])
                    {
                        s= false;
                        break;
                    }
                }
                if(s== false)
                    break;
            }
            if(s)
               tmp= 2*k-2 -j;
        }
        
        if(tmp > hth) hth= tmp;


        tmp= 0;
        for(j= 1; j < k; j++) {
            bool s= true;
            for(m= 0; m< j; m++) {
                for(n= k-m-1; n< m+k; n+=2) {
                    if(diamond[n][m] != diamond[n][2*j-m])
                    {
                        s= false;
                        break;
                    }
                }
                if(s== false)
                    break;
            }
            if(s)
                tmp= j;
        }
        vth= tmp;

        for(j= 2*k - 2; j >= k; j-- ) {
            bool s= true;
            for(m= 2*k-2 ; m> j; m-- ) {
                for(n= m - k + 1; n< 3*k-2-m; n+=2) {
                    if(diamond[n][m] != diamond[n][2*j-m])
                    {
                        s= false;
                        break;
                    }
                }
                if(s== false)
                    break;
            }
            if(s)
                tmp= 2*k-2-j;
        }
        
        if(tmp > vth) vth= tmp;

        
        int new_size= k + (k-1-hth + k-1-vth);

        // cout << new_size << " " << k << " " << hth << " " << vth << endl;
        cout << "Case #" << i << ": " << new_size*new_size - k*k << endl;
    }
    return 0;
}
