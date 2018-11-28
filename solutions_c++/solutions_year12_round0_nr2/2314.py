#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

int best;

void find(int i, int n, int s, int p, int num, int total[]){
    if (i == n){
       best = max(best, num);
    }
    if (n-i <= best - num) return;
     
    int current = total[i];
    if (current/3 >= p) find(i+1, n, s, p, num+1, total);
    
    if (current%3 == 0) {
       if (s>0 && current/3+1==p && current/3>0) 
            find(i+1, n, s-1, p, num+1, total);
       else
            find(i+1, n, s, p, num, total);
    }
    if (current%3 == 1) {
       if (current/3+1 == p)
            find(i+1, n, s, p, num+1, total);
       else 
            find(i+1, n, s, p, num, total);
    }
    if (current%3 == 2) {
       if (current/3+1 == p)
          find(i+1, n, s, p, num+1, total);
       else if (s>0 && current/3+2 == p)
          find(i+1, n, s-1, p, num+1, total);
       else find(i+1, n, s, p, num, total);
    }
}

int main(){
    int t;
    cin >> t;
    ofstream fout;
    fout.open("output.txt");
    for (int i=0; i<t; i++) {
        int n, s, p, total[101];
        best = 0;
        cin >> n >> s >> p;
        for (int j=0; j<n; j++)
            cin >> total[j];
        find(0, n, s, p, 0, total);
        fout << "Case #" << i+1 << ": " << best << endl;
    }
    fout.close();
    return 0;
}
    
