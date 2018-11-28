#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <cmath>


using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

typedef long long LL;
const double INF = 10000000000.0;
int main() {
    int T;
    in >> T;
    for( int test=1; test<=T; test++ ) {
        cout << "T:" << test << endl;
        int L, N, C;
        double t;
        in >> L >> t >> N >> C;
        vector<LL> foo, dist;
        for( int i=0; i<C; i++ ) {
            LL temp;
            in >> temp;
            foo.push_back(temp);
        }
        //dist.push_back(0);
        for( int i=0; i<N; i++ ) {
            dist.push_back( foo[i%C] );
            //cout << dist.back() << endl;
        }
        double best = INF;
        for( int f = 0; f<N; f++ ) {
            for( int s = f+1; s <= N; s++ ) {
                //build SB at f and s to be ready at t hours
                double total=0.0;
                for( int i=0; i<N; i++ ) { //moving from pos i
                    if( L>0 && ( (L==1&&f==i) || (L==2 && (f==i || s == i) ) ) ) {
                        if( total >= t ) { //already complete
                            total += dist[i];
                        }
                        //complete half way
                        else if( dist[i]*2+total > t ) {
                            //total += ((double)dist[i]-(double)(t-total)/2.0)+(double)(t-total);
                            total += ((double)dist[i]+(double)(t-total)/2.0);
                        //not complete
                        }
                        else {
                            total += dist[i]*2.0;
                        }
                    }
                    else { //normal speed
                        total += dist[i]*2.0;
                    }
                    //cout << total << endl;
                }
                //cout << total << endl;
                if( best > total ) best = total;
                //if( total > INF ) cout << "Problem: " << total << " Case:" << test << endl;
            }
        }
        out << "Case #" << test << ": " << (LL)round(best) << endl;

    }

    return 0;
}



