#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <list>
#include <set>
#include <cmath> 

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

#define GRANDE 6000

const int INF = 0x3FFFFFFF;
const double EPS = 1e-10;
const double PI = 3.14159265;
const double EXP = 2.71828183;

int N;
int T, C, D;
 
vector < double > P;

int check(vector <double> P_teste, double t){
    for(int i=0; i<N; i++){
        if(abs(P_teste.at(i) - P.at(i)) > t){
            return 0;
        }
    }
    return 1;
}

int tente(double t){
    vector < double > P_teste = P;
    
    P_teste.at(0) = P_teste.at(0) - t;
    for(int i=1; i<N; i++){
        double try_pos = P_teste.at(i) - t;
        PRINT("Trying pos %.3f for %.3f\n", try_pos, P.at(i));
        if(try_pos - P_teste.at(i-1) < D){
            PRINT("not ok\n");
            P_teste.at(i) = P_teste.at(i-1) + D;
        } else {
            PRINT("ok\n");
            P_teste.at(i) = try_pos;
        }
    }
    PRINT("P:\n");
    fori(i,N){
        PRINT("%.3f ",P.at(i));
    }
    PRINT("P_teste - T = %.3f - D = %d\n", t, D);
    fori(i,N){
        PRINT("%.3f ",P_teste.at(i));
    }
    PRINT("\n------------\n");
    return check(P_teste, t);
}
double bin_search(double t_min, double t_max){
    if( abs(t_min - t_max) < EPS) return (t_min + t_max) / 2;
    
    double t_mid = (t_min + t_max) / 2.0;
    
    if(tente(t_mid)){
        return bin_search(t_min, t_mid);
    } else {
        return bin_search(t_mid, t_max);
    }
}


int main()
{
    cin >> T;
    
    fori(teste,T){
        //Declaration of Vectors,sets,hashs
        P.clear();
        
        //Input
        cin >> C >> D;
        
        N = 0;
        fori(i,C){
            int p, v;
            cin >> p >> v;
            fori(j,v){
                P.push_back(p);
            }
        }
        
        N = size(P);
        sort(all(P));
        
        //Development
        double resp = bin_search(0.000, 10000.0);
        PRINT("C = %d, D =%d\n", C, D);
        
        //Solution
        cout << "Case #" << teste+1 << ": ";
        cout << setprecision(12) << resp;
        cout << endl;
    }
    
    return 0;
}