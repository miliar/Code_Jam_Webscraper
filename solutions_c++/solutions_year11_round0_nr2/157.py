#include<iostream>
#include<map>
#include<cassert>
#include<set>
#include<vector>
#include<fstream>
using namespace std;

class Pair {
   public:
      char a ;
      char b ;
      Pair(char x , char y) {
         if (x < y) {
            a = x ;
            b = y ;
         } else {
            b = x ;
            a = y ;
         }
      }
      bool operator < (const Pair& p) const {
         if (this->a != p.a) return this->a < p.a ;
         return this->b < p.b ;
      }
} ;

int convert(char c) {
   switch(c) {
      case 'Q':
         return 0 ;
      case 'W':
         return 1 ;
      case 'E':
         return 2 ;
      case 'R':
         return 3 ;
      case 'A':
         return 4 ;
      case 'S':
         return 5 ;
      case 'D':
         return 6 ;
      case 'F':
         return 7 ;
      default:
         assert(0) ;
   }
}

int main(int argc , char * argv[]) {
   ifstream fi(argv[1]) ;
   ofstream fo(argv[2]) ;
   int T ;
   fi >> T ;

   for (int t = 1 ; t <= T ; ++ t) {
      int C , D , N ;
      fi >> C ;
      map<Pair , char> com ;
      set<char> opp[8] ;
      vector<char> elements ;
      for (int c = 0 ; c < C ; ++ c) {
         char b[4] ;
         fi >> b ;
         com[Pair(b[0] , b[1])] = b[2] ;
      }

      fi >> D ;
      for (int d = 0 ; d < D ; ++ d) {
         char b[3] ;
         fi >> b ;
         opp[convert(b[0])].insert(b[1]) ;
         opp[convert(b[1])].insert(b[0]) ;
      }

      fi >> N ;
      for (int n = 0 ; n < N ; ++ n) {
         char e , b ;
         fi >> e ;
         if (!elements.empty()) {
            b = elements.back() ;
            if (com.find(Pair(b , e)) != com.end()) {
               elements.pop_back() ;
               elements.push_back(com[Pair(b , e)]) ;
            } else {
               bool clear = false ;
               for (int i = 0 , sz = elements.size() ; i < sz && !clear ; ++ i) {
                  if (opp[convert(e)].find(elements[i]) != opp[convert(e)].end()) {
                     clear = true ;
                  }
               }

               if (clear) {
                  elements.clear() ;
               } else {
                  elements.push_back(e) ;
               }
            }
         } else {
            elements.push_back(e) ;
         }
      }

      fo << "Case #" << t << ": [" ;
      for (int i = 0 , sz = elements.size() ; i < sz ; ++ i) {
         if (i) fo << ", " ;
         fo << elements[i] ;
      }
      fo << "]" << endl ;
   }
   return 0;
}

