#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <list>
#include <set>
#include <iomanip>

using namespace std;

#define pb push_back
#define fori(i, n) for ( int i = 0; i < (n); i++ )
#define forr(i, a, b) for ( int i = (a); i <= (b); i++ )
#define size(a) int((a).size())
#define all(x) (x).begin(),(x).end()
#define sorting(x) sort(all(x))
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end()
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define print_m(m) for(int i = 0;i<(int) m.size();i++) print_v(m[i]); cout << endl;
#define print_v(v) { for(int j = 0;j<(int) v.size();j++) cout << v[j] << " "; cout << endl; }
#define trace(x...)
#define PRINT(x...) trace(printf(x))
#define watch(x) trace(cout << #x " = " << x << "\n")

#define GRANDE 200

const int INF = 0x3FFFFFFF;
const double EPS = 1e-10;
const double PI = 3.14159265;
const double EXP = 2.71828183;

int main()
{
    int T, N;
    cin >> T;
    
    char matches[GRANDE][GRANDE];

    
    
    fori(teste,T){
        //Declaration of Vectors,sets,hashs
        double WP[GRANDE];
        double OWP[GRANDE];
        double OOWP[GRANDE];
        double RPI[GRANDE];
        
        //Input
        cin >> N;
        fori(i,N){
            fori(j,N){
                char a;
                cin >> a;
                matches[i][j] = a;
            }
        }
        
        //Development
        fori(i,N){
            int won = 0, loss = 0;
            fori(j,N){
                if(matches[i][j] == '1')
                    won++;
                if(matches[i][j] == '0')
                    loss++;
            }
            WP[i] = 1.0*won / (won + loss);
        }
        
        //AvgWP
        fori(i,N){
            //OWP for "i"
            double tempWP[GRANDE];
            fori(j,N){
                //Calculing "WP" for everyone, but not for 'i';
                int won = 0, loss = 0;
                if(j == i) continue;
                fori(k,N){
                    if(k == i) continue;
                    if(matches[j][k] == '1')
                        won++;
                    if(matches[j][k] == '0')
                        loss++;                
                }
                tempWP[j] = 1.0*won / (won + loss);
            }
            double sum = 0.0; int count = 0;
            fori(j,N){
                if((matches[i][j] == '1') || (matches[i][j] == '0')){
                    sum += tempWP[j];
                    count++;
                }
            }
            OWP[i] = sum / count;
        }
        
        fori(i,N){
            //OOWP for "i"
            double sum = 0.0; int count = 0;
            fori(j,N){
                if((matches[i][j] == '1') || (matches[i][j] == '0')){
                    sum += OWP[j];
                    count++;
                }
            }
            OOWP[i] = sum / count;
        }
        
        fori(i,N){
            RPI[i] = (0.25 * WP[i]) +  (0.5 * OWP[i]) + (0.25 * OOWP[i]);
            PRINT("Team %d:\t %.3f %.3f %.3f\t RPI: %.3f\n", i, WP[i], OWP[i], OOWP[i], RPI[i]);
            
        }
        
        //Solution
        cout << "Case #" << teste+1 << ":" << endl;
        fori(i,N){
            //OOWP for "i"
            cout << RPI[i] << setprecision(12) << endl;
        }
    }
    
    return 0;
}