#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <sstream>

using namespace std;

int ustawTurbo(int* dist, int n, int i, int t){
                int lsum = 0; int tempsum = 0;
                for(int l = 0; l < i; l++){
                    lsum += dist[l];
                    tempsum += dist[l] *2;
                }
                int lsumr = lsum + dist[i];
                //printf("lsum = %d, lsumr = %d\n", lsum, lsumr);
                if(t <= 2*lsum){
                    tempsum +=dist[i];
                } else if((t > 2*lsum) && (t <= 2*lsumr)){
                    int built = t - 2*lsum;
                    tempsum += dist[i] + built/2;
                } else tempsum += dist[i] *2;
                for(int j = i + 1; j < n; j++){
                    tempsum += 2*dist[j];
                }
            return tempsum;
}

int main()
{
    int tests;
    cin >> tests;
    for(int k = 1; k <= tests; k++){
        int l,n,c;
        long long int t;
        cin >> l;
        cin >> t;
        cin >> n;
        cin >> c;
        int *dist = new int[n];
        int *okr = new int[c];
        for(int i = 0; i < c; i++){
            cin >> okr[i];
        }
        for(int i = 0 ; i < n; i++){
            dist[i] = okr[i % c];
        }
        int sum = 0;
        int all = 0;
        for(int x = 0; x < n; x++){
            all += dist[x] *2;
        }
        if( l == 0){
            for(int i = 0; i < n; i++){
                sum += dist[i] * 2;
            }
        }else if(l == 1){
            int mini = 999999999;
            for(int i = 0; i < n; i++){
                mini = min(mini, ustawTurbo(dist, n, i, t));
            }
            sum = mini;
        }else{
            int mini = 999999999;
            for(int i = 0; i < n; i++){
                for(int j = i + 1; j < n; j++){
                    int a = ustawTurbo(dist, n, i, t);
                    int b = ustawTurbo(dist, n, j, t);
                    mini = min(mini, a + b - all);
                }
            }
            sum = mini;
        }
        cout << "Case #" <<k <<": " <<sum<<endl;
        delete[] okr;
        delete[] dist;
    }
    return 0;
}

/*                int lsum = 0;
                for(int l = 0; l < i; l++){
                    lsum += dist[l];
                    tempsum += dist[l] *2;
                }
                int lsumr = lsum + dist[i];
                //printf("lsum = %d, lsumr = %d\n", lsum, lsumr);
                if(t <= 2*lsum){
                    tempsum +=dist[i];
                } else if((t > 2*lsum) && (t <= 2*lsumr)){
                    int built = t - 2*lsum;
                    tempsum += dist[i] + built/2;
                } else tempsum += dist[i] *2;
                for(int j = i + 1; j < n; j++){
                    tempsum += 2*dist[j];
                }
                mini = min(mini, tempsum);
            }
            sum = mini;
*/
