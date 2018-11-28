#include<iostream>
#include<cstdlib>
#include<deque>
#include<fstream> 
using namespace std;
int main(){
    ifstream fin("C-small-attempt0.in");
    ofstream fout("C-small-attempt0.out"); 
    int T, R, k, N, num, w, line, now, ans, cas;     //T = 戈计 R = 笲Ω计 k = 程甧 N = 刮砰计
    while(fin >> T){
       cas = 1; 
       for(;T--;){
          fin >> R >> k >> N;
          deque<int> gr; 
          for(w = 0;w < N;w++){
             fin >> num;
             gr.push_back(num); 
          }
          ans = 0; 
          for(;R--;){
             line = N; now = 0; 
             while(line > 0){
                 now += gr[0]; gr.push_back(gr[0]); 
                 line--;
                 gr.pop_front();
                 if(now + gr[0] > k) break; 
             } 
             ans += now; 
          }
          fout << "Case #" << cas << ": " << ans << endl;
          cas++; 
       } 
       break; 
    } 
    return 0;
} 
     
