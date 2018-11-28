#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio> 
#include <cmath>
#include <cstdlib>
#include <fstream>

using namespace std;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}


typedef struct {
        int dh,dm;
        int ah,am;
} trip;

int diff(trip a, trip b) {
    return (b.dh - a.ah) * 60 + b.dm - a.am;
}

int main() {
    
    //ifstream in("B-small.in");
    ifstream in("B-large.in");
    
    //ofstream out("B-small.out");
    ofstream out("B-large.out");
    
    int N;
    
    in >> N;
    
    for (int i = 0; i < N; i++) {
        int T;
        
        in >> T;
        
        int NA,NB;
        
        in >> NA >> NB;
        
        vector<trip> A_trips, B_trips;
        
        for (int j = 0; j < NA; j++) {
            string d, a;
            in >> d >> a;
            
            trip tmp;
            
            sscanf(d.c_str(), "%d:%d", &tmp.dh, &tmp.dm);
            sscanf(a.c_str(), "%d:%d", &tmp.ah, &tmp.am);
            
            A_trips.push_back(tmp);
        }
        
        for (int j = 0; j < NB; j++) {
            string d,a; in >> d >> a;
            trip tmp;
            sscanf(d.c_str(), "%d:%d", &tmp.dh, &tmp.dm);
            sscanf(a.c_str(), "%d:%d", &tmp.ah, &tmp.am);
            
            B_trips.push_back(tmp);
        }
        
        bool A_res[NA]; bool B_res[NB];
        memset(A_res, 1, NA); memset(B_res, 1, NB);
        
        for (int j = 0; j < NA; j++) {
            int min_m = 24 * 60;
            int min_pos = -1;
            
            for (int k = 0; k < NB; k++) {
                int diff_AB = diff(A_trips[j], B_trips[k]);
                if (diff_AB < min_m && diff_AB >= T && B_res[k] == 1) {
                    min_pos = k;
                    min_m = diff_AB;
                }
            }
            
            if (min_pos != -1) B_res[min_pos] = 0;
        }
        
        for (int j = 0; j < NB; j++) {
            int min_m = 24 * 60;
            int min_pos = -1;
            
            for (int k = 0; k < NA; k++) {
                int diff_BA = diff(B_trips[j], A_trips[k]);
                if (diff_BA < min_m && diff_BA >= T && A_res[k] == 1) {
                    min_pos = k;
                    min_m = diff_BA;
                }
            }
            
            if (min_pos != -1) A_res[min_pos] = 0;
        }
        
        int na = 0, nb = 0;
        
        for (int j = 0; j < NA; j++) na += A_res[j];
        
        for (int j = 0; j < NB; j++) nb += B_res[j];
        
        out << "Case #" << i + 1 << ": " << na << " " << nb << endl;
    }
    
    return 0;
}
