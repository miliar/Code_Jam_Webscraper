#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;
int main (){
    ifstream fin ("A-large.in");
    ofstream fout ("A-large.out");
    int T;
    fin >>T;
    for (int i=1; i<=T; i++){
        int n;
        fin >>n;
      //  cout <<n<<endl;
        vector <int> v (n);
        string s;
        for (int k=0; k<n; k++){
            char a; int b;
            fin >>a>>b;
           // cout <<a<<" "<<b<<endl;
            s+=a; v[k]=b;
        }
        int mov=0;
        int posb=1; int posa=1;
        int dif=0;
        char moving=s[0];
        for (int k=0; k<n; k++){
            if (s[k]!=moving){
               moving=s[k];
               int dist;
               if (moving=='O') dist=abs(posa-v[k]);
               else dist=abs(posb-v[k]);
               int espera=dist-dif;
               mov+=(max(0,espera)+1);
               dif=max(1,espera+1);
               if (moving=='O') posa=v[k];
               else posb=v[k];
            }
            else {
               int dist;
               if (moving=='O') dist=abs(posa-v[k]);
               else dist=abs(posb-v[k]);
               mov+=(dist+1);
               dif+=(dist+1);
               if (moving=='O') posa=v[k];
               else posb=v[k];
            }
         //   cout <<mov<<" "<<dif<<endl;
        }
      //  cout <<"-----"<<endl;
        fout <<"Case #"<<i<<": "<<mov<<endl;
    //system ("pause");
    }
}
