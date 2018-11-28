#include<iostream>
#include<vector>
#include<cmath>
#include<fstream>

using namespace std;

typedef pair<int,int> pii;

int main(){
    ofstream fout ("out2.out");
    int t;
    cin >> t;
    for (int caso = 1; caso<=t; caso++){
        int n;
        cin >> n;
        int pos1 = 1, pos2 = 1, t1 = 0, t2 = 0;
        for (int i = 0; i < n; i++){
            char x;
            cin >> x;
            int add;
            if (x == 'O') add = 1;
            else add = 2;
            int boton;
            cin >> boton;
            if (add == 1){
                int dist = abs(pos1-boton);
                t1=max(t1+dist+1,t2+1);
                pos1 = boton;
            }
            else{
                int dist = abs(pos2-boton);
                t2 = max(t2+dist+1,t1+1);
                pos2 = boton;
            }
        }
        fout << "Case #" << caso << ": " << max(t1,t2) << endl;
    }
}
