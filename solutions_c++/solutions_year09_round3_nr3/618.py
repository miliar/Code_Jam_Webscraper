#include<iostream>
#include<conio.h>
#include<string>
#include<fstream>
#include<time.h>
#include<sstream>
#include<vector>
#include<set>
using namespace std;

template<class T>
string toString(const T &t) {
       stringstream ss; ss << t;
       return ss.str();
}

int release(int cells, vector<int> & p) {
    char * origc = new char[cells];
    for (int j=0; j<cells; j++) {
        origc[j] = '#';
    }
    for (int j=0; j<p.size(); j++) {
        origc[p[j]-1] = 'p';
    }
    
    int cost = 10000000;
    
    vector< vector<int> > orders;
    sort(p.begin(), p.end());
    
    do {
       vector<int> t;
       for (int i=0; i<p.size(); i++) {
           t.push_back(p[i]);
           //cout << p[i] << " ";
       }
       //cout << endl;
       orders.push_back(t);
       
    } while (next_permutation(p.begin(), p.end()));
    
    for (int i=0; i<orders.size(); i++) {    
        char * c = new char[cells];
        for (int j=0; j<cells; j++) {
            c[j] = origc[j];
        }
        int cst = 0;
        vector<int> ps = orders[i];
        /*
        for (int j=0; j<ps.size(); j++)
            cout << ps[j] << " ";
        cout << endl;
        */
        for (int j=0; j<ps.size(); j++) {
            int p_to_r = ps[j]-1;
            int curr_c = 0;
            
            //cout << "releasing " << p_to_r << endl;
            
            if (p_to_r > 0) {
               // release all left
               for (int k=p_to_r-1; k>=0; k--) {
                   if (c[k] != ' ') {
                      cst++;
                      curr_c++;
                   } else {
                     break;
                   }
               }
            }
            if (p_to_r < cells-1) {
               // release all right
               for (int k=p_to_r+1; k<cells; k++) {
                   if (c[k] != ' ') {
                      cst++;
                      curr_c++;
                   } else {
                     
                     break;
                   }
               }
            }
            //cout << "current cost: " <<  curr_c << endl;
            c[p_to_r] = ' ';
            /*
            for (int j=0; j<cells; j++) {
                cout << c[j];
            }
            cout << endl;
            getch();
            */
        }
        if (cst < cost) cost = cst;
    }
    return cost;
}

int main() {
    
    ofstream out("p3.out");
    ifstream in("C-small-attempt0.in");
    
    int cases;
    in >> cases;
    for (int i=0; i<cases; i++) {
        int c; int np; vector<int> p;
        in >> c >> np;
        for (int j=0; j<np; j++) {
            int t; in >> t; p.push_back(t);
        }
        out << "Case #" << i+1 << ": " << release(c, p) << endl;
    }
    return 0;   
}
