#include <iostream>

using namespace std;

int main(){
    int T;
    int N;
    cin >> T;
    char Match[100][100];
    double WP[100];
    double OWP[100];
    double OOWP[100];
    int count[100];
    

    for( int i = 0; i < T; i++ ){


        cin >> N;
        for( int j = 0; j < N; j++ )
            for( int k = 0; k < N; k++ ){
                cin >> Match[j][k];
            }
        for( int j = 0; j < N; j++ ){
            count[j] = 0;
        }

        
        double sum = 0.0;
        for( int j = 0; j < N; j++){
            sum = 0;
            for( int k = 0; k < N; k++){
                if( Match[j][k] != '.' ){
                    sum += Match[j][k] - '0';
                    count[j]++;
                }

            }
            WP[j] = sum/count[j];
        }

        
        
        for( int j = 0; j < N; j++){
            sum = 0;
            for( int k = 0; k < N; k++ ){
                if( Match[j][k] != '.' ){
                    sum += (WP[k] * count[k] - (Match[k][j]-'0')) / (count[k] - 1);
                }
            }
            OWP[j] = sum / count[j];
        }

        
        for( int j = 0; j < N; j++){
            sum = 0;
            for( int k = 0; k < N; k++){
                if( Match[j][k] != '.' ){
                    sum += OWP[k];
                }
            }
            OOWP[j] = sum/count[j];
        }

        cout << "Case #" << i+1 << ":" << endl;
        for( int j = 0; j < N; j++){
            double ans = 0.25 * WP[j] + 0.5 * OWP[j] + 0.25 * OOWP[j];
            cout << ans << endl;
        }

    }
}
