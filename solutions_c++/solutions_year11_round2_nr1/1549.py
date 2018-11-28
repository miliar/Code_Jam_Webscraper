#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <fstream>

using namespace std;



int main(){
    
    ifstream inf;
    inf.open("input1.txt");
    
    ofstream outf;
    outf.open("output1.txt");
    
    int nt;
    inf>>nt;
    
    for (int it = 0; it<nt; it++){
        int n;
        inf>>n;
        
        int ** s = new int *[n];
        
        for (int i = 0; i < n; i++){
            s[i] = new int[n];
        }
        
        char c;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                inf>>c;
                //cout<<c;
                if (c == '0') s[i][j] = 0;
                else if (c == '1') s[i][j] = 1;
                else s[i][j] = -1;
            }    
        }    
        
        long double *w = new long double[n];
        long double *t = new long double[n];
        long double *wp = new long double[n];
        
        
        for (int i = 0; i< n; i++){
            t[i] = 0;
            w[i] = 0;
            for (int j = 0; j < n; j++){
                if (s[i][j] != -1) t[i] = t[i]+1;
                if (s[i][j] == 1) w[i] = w[i]+1;
            }
            wp[i] = w[i]/t[i];
        }
        
        long double *owp = new long double[n];
        
        for (int i = 0; i < n; i++){
            owp[i] = 0;
            for (int j = 0; j < n; j++){
                if (s[i][j] == 0){
                   owp[i] = owp[i] + (w[j] - 1)/(t[j]-1);
                }
                else if (s[i][j] == 1){
                     owp[i] = owp[i] + w[j]/(t[j] - 1);
                }
            }
            owp[i] = owp[i]/t[i];   
        }
        
        long double *oowp = new long double[n];
        
        for (int i = 0; i < n; i++){
                oowp[i] = 0;
                for (int j = 0; j < n; j++){
                    if (s[i][j] != -1) oowp[i] = oowp[i] + owp[j];    
                }
                oowp[i] = oowp[i]/t[i];
        }
        
        long double *rpi = new long double[n];
        
        outf<<"Case #"<<it+1<<":\n";
        for (int i = 0; i < n; i++){
            rpi[i] = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
            //outf<<w[i]<<" "<<t[i]<<" "<<wp[i]<<" "<<owp[i]<<" "<<oowp[i]<<" "<<rpi[i]<<endl;
            outf<<rpi[i]<<endl;
            }
        
    }
    //cin>>nt;
    return 0;
    
}
