#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#define fori(N) for(int i=0; i<N; i++)
#define forj(N) for(int j=0; j<N; j++)

using namespace std;

int px[40];
int py[40];
int pr[40];

int main(){
    ifstream fin("D-small-attempt0.in");
    ofstream fout("D-small.out");
    
    int n, p;
    fin >> n;
    //getline(fin, line);
    for(int Z=0; Z<n; Z++){
        fin >> p;
        fori(p) fin >> px[i] >> py[i] >> pr[i];
        double minr = 99999;
        if(p == 1) minr = pr[0];
        else if(p == 2) minr = max(pr[0], pr[1]);
        else if(p == 3){
            double t1 =(pr[1] + pr[2] + sqrt((px[1]-px[2])*(px[1]-px[2]) + (py[1] - py[2]) * (py[1] - py[2])))/2;
            double t2 = (pr[0] + pr[2] + sqrt((px[0]-px[2])*(px[0]-px[2]) + (py[0] - py[2]) * (py[0] - py[2])))/2;
            double t3 = (pr[1] + pr[0] + sqrt((px[1]-px[0])*(px[1]-px[0]) + (py[1] - py[0]) * (py[1] - py[0])))/2;
            if(t1 < minr && pr[0] <= t1) minr = t1;
            if(t2 < minr && pr[1] <= t2) minr = t2;
            if(t3 < minr && pr[2] <= t3) minr = t3;
                
        }
        
        fout << "Case #" << Z+1 <<": " << minr << endl;
    }
    //cin.get();
    return 0;   
}
