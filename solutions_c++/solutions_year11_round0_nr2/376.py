#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main(){
   int n_case;
   cin >> n_case;
   bool table[30][30];
   for( int i = 0 ; i < n_case ; i++ ){
      int C;
      cin >> C;
      vector< pair<string,string> > Cvec;
      for( int k = 0 ; k < C ; k++ ){
         string tmp;
         cin >> tmp;
         Cvec.push_back(make_pair(tmp.substr(0,2),tmp.substr(2)));
      }
      int D;
      cin >> D;
      vector<string> Dvec;
      for( int x = 0 ; x < 30 ; x++ ){
         for( int y = 0 ; y < 30 ; y++ ){
            table[x][y] = false;
         }
      }
      for( int k = 0 ; k < D ; k++ ){
         string tmp;
         cin >> tmp;
         table[tmp[0]-'A'][tmp[1]-'A'] = true;
         table[tmp[1]-'A'][tmp[0]-'A'] = true;
      }
      int N;
      cin >> N;
      string instr;
      cin >> instr;
      int ind = 0;
      string ans ="";
      set<char> prohibit;

      while( ind+1 < N ){
         string sub = instr.substr(ind,2);
         char c = sub[0];
         if(prohibit.find(c)!=prohibit.end()){
            ans = "";
            prohibit.clear();
            ind++;
            continue;
         }

         string ins = "";

         for( int k = 0 ; k < Cvec.size(); k++ ){
            if( Cvec[k].first == sub || (Cvec[k].first[1]==sub[0]&&Cvec[k].first[0] == sub[1]) ){
               ins = Cvec[k].second;
               ind++;
               break;
            }
         }
         if( ins == "" ){
            ins = sub.substr(0,1);
            for( int k = 0 ; k < 30 ; k++ ){
               if( table[c-'A'][k] ){
                  prohibit.insert( (char) (k+'A'));
               }
            }
         }
         ans += ins;
         ind++;
      }
      if( ind == N-1 ){
         string ins = instr.substr(ind,1);
         char c = ins[0];
         if(prohibit.find(c)!=prohibit.end()){
            ans = "";
            ins = "";
            prohibit.clear();
         }
         ans += ins;
      }

      cout << "Case #" << i+1 << ": " ;
      cout << "[";
      for( int l = 0 ; l < ans.size(); l++ ){
         if( l != ans.size()-1 ){
            cout << ans[l] << ", ";   
         }
         else{
            cout << ans[l] ;
         }
      }
      cout << "]"<< endl;
   }
   return 0;
}
