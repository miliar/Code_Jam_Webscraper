#include <iostream>

using namespace std;

int main(){
   int n_case;
   cin >> n_case;
   for( int i = 0 ; i < n_case ; i++ ){
      int n;
      cin >> n ;
      char prevc = 'P'; 
      int result = 0;
      int Bpos = 1;
      int Opos = 1;
      int Btime = 0;
      int Otime = 0;
      for( int l = 0 ; l < n ; l++ ){
         char c;
         int bnum;
         cin >> c >> bnum;
         if( c != prevc ){
            if( c == 'O' ){
         //      cout << "case1"<<endl;
               int diff = max( abs(Opos-bnum)-Otime , 0 );
               result += diff+1;
               Opos = bnum;
               Btime += diff+1;
               Otime = 0;
            }
            else{
         //      cout << "case2"<<endl;
               int diff = max( abs(Bpos-bnum)-Btime, 0);
               result += diff+1;
               Bpos = bnum;
               Otime += diff+1;
               Btime = 0;
            }
         }
         else{
            if( c == 'O' ){
            //   cout << "case3"<<endl;
               result += abs(Opos - bnum)+1;
               Btime += abs(Opos - bnum)+1;
               Opos = bnum;
            }
            else{
            //   cout << "case4"<<endl;
               result += abs(Bpos - bnum)+1;
               Otime += abs(Bpos - bnum)+1;
               Bpos = bnum;
            }
         }
         prevc = c;
       //  cout << "Orange,pos:" << Opos <<" Time:"<<Otime<<endl;
       //  cout << "Blue,pos:" << Bpos <<" Time:"<<Btime<<endl;
       //  cout << "result:" << result <<endl<<endl;
      }

      cout << "Case #" << i+1 << ": " ;
         cout << result << endl;
   }
   return 0;
}
