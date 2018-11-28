#include <iostream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; i++)

#define FORI(i,b,a) for(int i = b - 1 ; i >= a ; i--)

#define LL long long
#define ULL unsigned long long
#define UI unsigned int

#define VI vector<int>
#define VS vector<string>

#define pb push_back

int main() {
    int tc,T;
    int arr[101][101];
    cin>>tc;
    FOR(T,1,tc+1) {
        memset(arr,101*101*sizeof(int),0);
        int n;
        cin>>n;
        vector <double> win(n,0),owp(n,0),oowp(n,0);
        VI num(n,0);
        char ch;
        FOR(i,0,n) {
            int c = 0;
            int winCount = 0;
            FOR(j,0,n) {
                cin>>ch;
                if(ch == '.') {
                    arr[i][j] = -1;
                }
                else if(ch == '1') {
                     arr[i][j] = 1;
                     winCount++;
                     c++;
                }
                else if(ch == '0') {
                     arr[i][j] = 0;
                     c++;
                }
            }
            num[i] = c;
            win[i] = (double)winCount / c;
        }
        
        FOR(i,0,n) {
            double d = 0;
            FOR(j,0,n) {
                if(arr[i][j] != -1) {
                    int c = 0;
                    int winCount = 0;
                    FOR(k,0,n) {
                        if(i != k) {
                             if(arr[j][k] == 1) winCount++;
                             else if(arr[j][k] == 0) c++;
                        }
                    }
                    d = d + (double)winCount / (winCount + c);
                }
            }
            owp[i] = d/num[i];
        }
        
        FOR(i,0,n) {
            double d = 0;
            FOR(j,0,n) {
                if(arr[i][j] != -1) {
                    d = d + owp[j];
                }
            }
            oowp[i] = d/num[i];
        }
        
        printf("Case #%d:\n",T);
        
        FOR(i,0,n) {
            printf("%lf\n", 0.25 * win[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
        }
    }
    return (0);
}
