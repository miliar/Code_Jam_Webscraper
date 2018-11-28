#include <iostream>
using namespace std;
char mat[200][200];
int gando[200];
int total[200];
long double OWP[200];
int n;
void resuelve(){
    cin >> n;
    for(int i=0;i<n;i++){
        total[i] = 0;
        gando[i] = 0;
        for(int j=0;j<n;j++){
            cin >> mat[i][j];
            if( mat[i][j] != '.'){
                total[i]++;
            }
            if( mat[i][j] == '1'){
                gando[i]++;
            }
        }
    }
    int cuanto;
    for(int j=0;j<n;j++){
        OWP[j] = 0.0;
        cuanto = 0;
        for(int i=0;i<n;i++){
            if( mat[i][j] == '1')
                gando[i]--;
            if( j!=i){
                if( mat[i][j] == '1'){
                    OWP[j] += ((long double)(gando[i]))/((long double)(total[i]-1));
                    cuanto++;
                }
                if( mat[i][j] == '0'){
                    OWP[j] += ((long double)gando[i])/((long double)(total[i]-1));
                    cuanto++;
                }
            }
            if( mat[i][j] =='1')
                gando[i]++;
        }
        OWP[j] /= (long double)cuanto;
    }
    for(int i=0;i<n;i++){
        long double OOW=0.0;
        cuanto =0;
        for(int j=0;j<n;j++){
            if( mat[i][j] != '.'){
                cuanto++;
                OOW += OWP[j];
            }
        }
        cout <<(0.25*((long double)gando[i]/(long double)total[i])) + (0.5*OWP[i])+ 0.25*(OOW/(long double)cuanto)<< endl;
         
         
    }
}
int main(){
    int t;
    cin >> t;
    for(int i=1;i<=t;i++){
        cout << "Case #"<< i<< ":\n";
        resuelve();
    }
    return 0;
}
