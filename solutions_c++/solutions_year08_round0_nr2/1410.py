#include <iostream>
#include <vector>

using namespace std;

const int TOTAL = 24*60;

int main(){
    int N, NA, NB, T, i, j, a, b, ca, cb;
    cin >> N;

    for( j = 1; j <= N; j++ ){
        int h, m;
        char orign;

        cin >> T;
        cin >> NA >> NB;
        
        vector<int> depA(NA, 0);
        vector<int> arrA(NA, 0);
        vector<int> depB(NB, 0);
        vector<int> arrB(NB, 0);
        vector<int> v_A;
        vector<int> v_B;

        for( i = 0; i < NA; i++ ){

            cin >> h >> orign >> m;
            depA[i] = m+60*h;
            cin >> h >> orign >> m;
            arrA[i] = m+60*h;
        }

        for( i = 0; i < NB; i++ ){
            cin >> h >> orign >> m;
            depB[i] = m+60*h;
            cin >> h >> orign >> m;
            arrB[i] = m+60*h;
        }
        a = 0;
        b = 0;
        ca = 0;
        cb = 0;
        for( int time = 0; time < TOTAL; time++ )
        {
            for( i = 0; i < static_cast<int> (v_B.size()); i++ ){
                if( v_B[i] == time ){
                    cb++;
                }
            }
            for( i = 0; i < static_cast<int> (v_A.size()); i++ ){
                if( v_A[i] == time ){
                    ca++;
                }
            }
            for( i = 0; i < NB; i++ ){
                if( depB[i] == time ){
                    if( cb <= 0 ) {
                        b++; cb++;
                    }
                    cb--;
                    v_A.push_back(arrB[i]+T);
                }
            }
            for( i = 0; i < NA; i++ ){
                if( depA[i] == time ){
                    if( ca <= 0 ){
                        a++; ca++;
                    }
                    ca--;
                    v_B.push_back(arrA[i]+T);
                }
            }
        }
        cout << "Case #" << j << ": " << a << " " << b << endl;
    }
    return 0;
}
