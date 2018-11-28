    #include <stdio.h>
    #include <iostream>
    #include <memory.h>
    #include <algorithm>
    #include <vector>
    #include <string>
    #include <utility>
    #include <map>
    #include <set>
    #include <deque>
    #include <math.h>
    #include <iomanip>
    
    #define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
    #define fr(a,b) fo( a, 0, ( b ) )
    #define fi(a) fr( i, ( a ) )
    #define fj(a) fr( j, ( a ) )
    #define fk(a) fr( k, ( a ) )
    #define mp make_pair
    #define pb push_back
    #define all(v) (v).begin( ), (v).end( )
    #define _(a,b) memset( a, b, sizeof( a ) )
    
    using namespace std;
    typedef long long ll;
    typedef vector<int> vi;
    typedef vector<string> vs;
    
    int pos[101][101];
    int games[101];
    int won[101];
    long double owp[101],oowp[101], res[101];
    
    int main() {
        freopen( "input", "r", stdin );
        freopen( "output", "w", stdout );
    
        int i,j,k,t,n;
        char c[101];
        scanf("%d", &t);
    
        fi(t) {
            scanf("%d", &n);
            _(pos,0);
            _(games,0);
            _(won,0);
            fj(n) {
                fk(n) {
                    cin>>c[k];
                    if (c[k] == '.')
                        pos[j][k] = -1;
                    else if (c[k] == '1') {
                        pos[j][k] = 1;
                        ++games[j];
                        ++won[j];
                    }
                    else if (c[k] == '0') {
                        pos[j][k] = 0;
                        ++games[j];
                    }
                }
            }
    
            _(owp, 0);
            _(oowp, 0);
            _(res,0);
            long double avg,avg2;
            long double temp;
            long total = 0;
    
            fj(n) {
                avg = 0;
                temp = 0;
                fk(n) {
                    if (j!=k) {
                        if (pos[j][k] != -1) {
                            temp = (pos[j][k] == 1 ? (won[k])/(double)(games[k]-1) : (won[k]-1)/(double)(games[k]-1));
                            avg += temp;
                        }
                    }
                }
                owp[j] = avg / games[j];
            }
            
            printf("Case #%d:\n", i+1);
            fj(n) {
                avg2 = 0;
                fk(n) {
                    if (j!=k) {
                    if (pos[j][k] != -1)
                        avg2 += owp[k];
                    }
                }
                res[j] = (0.25 * won[j] / games[j]) + 0.5 * owp[j] + 0.25 * avg2 / games[j];
                cout<< setprecision(10);
                cout<<res[j]<<endl;
            } 
        }
    
            return 0;
        }
    
    
    
