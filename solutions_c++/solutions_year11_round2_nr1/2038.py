#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>
#include <fstream>

using namespace std;

int t;
vector <double> RPI(t, 0);
vector <string> v(t);
vector <double> owp(t, 0);
vector <double> wp(t, 0);
vector <double> oowp(t, 0);

ifstream fin("A-small-in.txt");
    ofstream fout("A-small-out.txt");

bool played(char c){
     if (c!='.') return true;
     return false;
}

void WP(int i){
       double a = 0, div = 0;
       for (int j = 0; j < t; j++){
           if (v[i][j] == '1') a++;
           if (played(v[i][j])) div++;
       }
       wp[i] = a/div;
}

void OWP(int j){
       double a = 0, res = 0, div = 0, div2 = 0;
       for (int i = 0; i < t; i++){
           if (i!=j and played(v[i][j])){  // si es contrincant,
              div = 0;
              a = 0;
              for (int d = 0; d < t; d++){   //miro tots els partits que ha jugat menys el que ha jugat contra mi.
                  if (d!=j){ // sense comptar el meu
                     if (v[i][d] == '1') a++;
                     if (played(v[i][d])) div++;
                  }
              }
              if (div!=0) div2++;
              res+=(a/div);
           }
       }
       owp[j] = res/div2;
}

void OOWP(int j){
       //fout <<"OOWP: "<<j<<"; ";
       double res = 0, div = 0;
       for (int i = 0; i < t; i++){
           if (played(v[i][j])) { 
                                
              //fout <<"opponent: "<<i<<" : "<<owp[i]<<" // ";
              res+=owp[i]; 
              div++; 
           }
       }
       //fout <<" / "<<div<<endl;
       //fout <<endl;
       oowp[j] = res/div;
}

int main(){
    
    int n;
    fin >>n;
    
    for (int c = 0; c < n; c++){
        fin >>t;
        RPI = vector <double> (t, 0);
        v = vector <string> (t);
        owp = vector <double> (t, 0);
        wp = vector <double> (t, 0);
        oowp = vector <double> (t, 0);
        for (int i = 0; i < t; i++) fin >>v[i];
        fout <<"Case #"<<c+1<<":"<<endl;
        for (int i = 0; i < t; i++) WP(i); //fout <<wp[i]<<" ";}
        //fout <<endl;
        for (int i = 0; i < t; i++) OWP(i); //fout <<owp[i]<<" ";}
        //fout <<endl;
        for (int i = 0; i < t; i++) OOWP(i); //fout <<oowp[i]<<" ";}
        //fout <<endl;
        for (int i = 0; i < t; i++) RPI[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
        for (int i = 0; i < t; i++) fout <<RPI[i]<<endl;
    }

}
