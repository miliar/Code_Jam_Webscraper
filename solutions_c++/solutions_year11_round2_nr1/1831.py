#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main(int argc, char *argv[])
{

    ifstream fin;
    ofstream fout;
    fin.open("A-large.in");
    fout.open("A-large.out");
    
    int i,j,k,l,p,h,n,m,t,how;
    char c;
    int a[200][200];
    double WP[200],PP[200],OWP[200],OOWP[200],RPI[200];
    fin >> t;
    for (i=1;i<=t;i++){
        fin >> n;
        for (j=1;j<=n;j++){
        for (k=1;k<=n;k++){    
            fin >> c;
            if (c=='.'){
                a[j][k]=-1;
            }else if (c=='1'){ 
                a[j][k]=1;
            }else if (c=='0'){
                a[j][k]=0;
            }      
        }
        }
        
//        for (j=1;j<=n;j++){
 //       for (k=1;k<=n;k++){    
//            cout << a[j][k] << " ";
//        }
//            cout << endl;
 //       }
        
        for (j=1;j<=n;j++){
            WP[j]=0;
            PP[j]=0;
            for(k=1;k<=n;k++){
               if (a[j][k]>-1){
                  PP[j]++;
                  WP[j]+=a[j][k];             
               }               
            }
            WP[j]=WP[j]/PP[j];
        }
        
        for (j=1;j<=n;j++){
         OWP[j]=0;
         for (k=1;k<=n;k++){
           if (a[j][k]>-1){  
             OWP[j]+=(WP[k]*PP[k]-a[k][j])/(PP[k]-1);
           }
         }
         OWP[j]=OWP[j]/PP[j];   
        }           
        
        for (j=1;j<=n;j++){
           OOWP[j]=0;
           m=0; 
           for (k=1;k<=n;k++){
              if (a[j][k]>-1){
                 m++;
                 OOWP[j]+= OWP[k];            
              }  
           }
           OOWP[j]=OOWP[j]/m;   
        }

      fout << "Case #" << i << ":\n";
      for (j=1;j<=n;j++){
//          cout << "j=" << j << ", WP=" << WP[j] << " ,OWP=" << OWP[j] << ", OOWP=" << OOWP[j] << endl;
          fout << (0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j]) << endl;
      } 
    }
    return 0;
}
