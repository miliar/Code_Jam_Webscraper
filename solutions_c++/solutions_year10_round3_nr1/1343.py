#include<iostream>
#include<fstream> 
using namespace std;
int main(){
    int T, N, a[1001], b[1001], c, d, e, ans;
    ifstream fin("A-large.in");
    ofstream fout("A-large.out"); 
    while(fin >> T){
       for(c = 1;c <= T;c++){
          fin >> N; 
          for(d = 1;d <= N;d++){
             fin >> a[d] >> b[d];  
          }
          fout << "Case #" << c << ": "; ans = 0; 
          for(d = 1;d <= N-1;d++){
             for(e = d+1;e <= N; e++){
                if((a[d] - a[e]) * (b[d] - b[e]) < 0) ans++; 
             } 
          } 
          fout << ans << endl; 
       }
       break; 
    }
    return 0;
    } 
