#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <list>
#include <set>
#include <math.h>

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

bool compare(pair <double,double> a, pair <double,double> b){
    return (a.first < b.first);
}

int main()
{
    int T, N;
    cin >> T;
    
    double X, W, R, tempo;
    fori(teste,T){
        //Declaration of Vectors,sets,hashs
        vector < pair <double,double> > walk; //Speed, length
        
        //Input
        cin >> X >> W >> R >> tempo >> N;
        R -= W;
        
        double walkT = 0.0;
        fori(i,N){
            int a, b, c;
            cin >> a >> b >> c;
            
            pair <double,double> wt = make_pair( c+W , b-a );
            walkT += (b-a);
            walk.push_back(wt);
        }
        
        double walkOnly = (walkT < X)?X-walkT:0.0;
        walk.push_back( make_pair( W , walkOnly ) );
        
        sort(all(walk),compare);
        //Development
        
        //computing tempo
        PRINT("X %.3f W %.3f R %.3f - tempo %.3f\n",X, W, R, tempo);
        double spent_time = 0.0;
        fori(i,N+1){
            double w, d;
            w = walk.at(i).first;
            d = walk.at(i).second;
            PRINT("Walkway: %.3f %.3f\t",w,d);
            
            double run_dist = tempo * (w+R);
            if(run_dist > d){
                //Posso correr tudo
                double run_time = d/(w+R);
                run_dist = d;
                spent_time += run_time;
                PRINT("CORRO TUDO: DIST %.3f TIME %.3f", run_dist, run_time);
                tempo       -= run_time;
                
            } else {
                //Nao posso correr tudo
                spent_time += tempo;
                //Agora vou andando
                
                double walk_distance;
                if(fabs(tempo) < EPS){
                    walk_distance = d;
                } else {
                    walk_distance = (d - run_dist);
                }
                double walk_time = walk_distance/w;
                
                spent_time += walk_time;
                PRINT("CORRO DIST %.3f TIME %.3f, ANDO DIST %.3f TIME %.3f", run_dist, time, (d-run_dist), walk_time);
                tempo = 0.0;
                
            }

            PRINT("\t NOW %.3f\n",spent_time);
        }
        
        //Solution
        cout << "Case #" << teste+1 << ": ";
        cout << setprecision(16) << spent_time;
        cout << endl;
    }
    
    return 0;
}