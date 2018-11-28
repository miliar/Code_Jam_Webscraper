#include <iostream>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <stack>
#include <queue>
#include <cmath>
#include <cstdio>

#define MAX 101

using namespace std;


int n;
char a[MAX][MAX];
double wp[MAX];
double owp[MAX];
double oowp[MAX];
int played[MAX];

double rpi(int i){
    return 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
}

int main(){
    int T;
    cin >> T;
    for (int t=1; t<=T; t++){
        
        cin >> n;
        
        for (int i=0; i<n; i++){
            wp[i] = 0.0;
            owp[i] = 0.0;
            oowp[i] = 0.0;
        }
        
        for (int i=0; i<n; i++){
            
            played[i] = n;
            
            for (int j=0; j<n; j++){
                cin >> a[i][j];
                
                if ( a[i][j] == '.' ){
                    played[i]--;
                } else if ( a[i][j] == '1' ){
                    wp[i]++;
                }
            }
            
            
        }
        
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                if ( a[i][j] != '.' ){
                    if ( a[i][j] == '1' ){
                        owp[i] += (wp[j]) / double(played[j]-1);
                    } else {
                        owp[i] += (wp[j]-1) / double(played[j]-1);
                    }
                }
            }
            owp[i] /= played[i];
        }
        for (int i=0; i<n; i++){
            wp[i] /= double(played[i]);
        }
        
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                if ( a[i][j] != '.' ){
                    oowp[i] += owp[j];
                }
            }
            oowp[i] /= played[i];
        }
        
        cout << "Case #" << t << ":" << endl;
        for (int i=0; i<n; i++){
            //cout << wp[i] << " " << owp[i] << " " << oowp[i] << " ";
            printf("%0.12g\n", rpi(i));
        }
    }

    return 0;
}