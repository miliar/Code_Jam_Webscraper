#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
int main (){
    int T;
    ifstream fin ("A-large.in");
    ofstream fout ("A-large.out");
    fin >>T;
    for (int i=0; i<T; i++){
        int n;
        fin >>n;
        vector <string> v (n);
        for (int ia=0; ia<n; ia++){
            fin >>v[ia];
        }
        vector <int> playin(n);
        vector <double> WP(n); vector <double> OWP(n);  vector <double> OOWP(n); 
        for (int is=0; is<n; is++){
            int won=0;
            int play=0;
            for (int ij=0; ij<n; ij++){
                if (v[is][ij]!='.'){
                   play++;
                   if (v[is][ij]=='1') won++;
                }
            }
            playin[is]=play;
            WP[is]=(double)won/(double)play;
        }
        for (int is=0; is<n; is++){
            double sum=0.;
            int op=0;
            for (int ij=0; ij<n; ij++){
                if (v[is][ij]!='.'){
                   double wp=WP[ij];
                   if (v[ij][is]=='1'){
                      wp*=(double)playin[ij];
                      wp-=1;
                      wp/=(playin[ij]-1);
                   }
                   else {
                      wp*=(double)playin[ij];
                      wp/=(playin[ij]-1);
                   }
                   sum+=wp;
                   op++;
                }
            }
            OWP[is]=sum/(double)op; 
        }
        for (int is=0; is<n; is++){
            double sum=0.;
            int op=0;
            for (int ij=0; ij<n; ij++){
                if (v[is][ij]!='.'){
                   sum+=OWP[ij];
                   op++;
                }
            }
            OOWP[is]=sum/(double)op; 
        }
        fout <<"Case #"<<i+1<<":"<<endl;
        for (int is=0; is<n; is++){
            fout <<(WP[is]*0.25)+(OWP[is]*0.5)+(OOWP[is]*0.25)<<endl;
        }
    } 
   // system ("pause");
}
