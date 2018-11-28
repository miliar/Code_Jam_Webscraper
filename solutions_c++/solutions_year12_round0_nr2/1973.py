#include <fstream>
#include <iostream>

using namespace std;

ifstream f("b.in");
ofstream g("b.out");

int n, s, p, t;

int modul(int x){

    if (x < 0) return x*-1;
    return x;

}

int main(){

    f >> t;
    for(int j=1; j<=t; j++){
         f >> n >> s >> p;
         int rez = 0;
         for(int i=1; i<=n; i++){
            int x;
            f >> x;
            int ok = 0;
            for(int a=0; a<=10; a++){
                for(int b=max(0,a-1); b<=min(10,a+1); ++b){
                    int c = x-(a+b);
                    if (c < 0 || c > 10) continue;
                    if (modul(a-b)>1 || modul(a-c) > 1 || modul(b-c) > 1) continue;
                    if (max(a,max(b,c)) >= p){
                        ++rez;
                        ok = 1;
                        break;
                    }
                }
                if (ok==1) break;
            }
            if (s == 0 || ok == 1) continue;
            for(int a=0; a<=10; a++){
                for(int b=max(0,a-2); b<=min(10,a+2); b++){
                    int c = x-(a+b);
                    if (c < 0 || c > 10) continue;
                    if (modul(a-b) > 2 || modul(a-c) > 2 || modul(b-c) > 2) continue;
                    if (max(a,max(b,c)) >= p){
                        ++rez;
                        --s;
                        ok = 1;
                        break;
                    }
                }
                if (ok==1) break;
            }
        }
        g <<"Case #"<<j<<": "<< rez << "\n";
        //g << rez << " ";
    }

}
