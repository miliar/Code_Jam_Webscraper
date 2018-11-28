#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

class Dnode {
   private:
      Dnode * p ;
      int r ;
   public:
      int sz ;
      Dnode() : r(0) , sz(1) {
         p = this ;
      }

      void merge(Dnode& x) {
         Dnode * a = x.find() ;
         Dnode * b = this->find() ;

         if (a == b) return ;
         if (a->r < b->r) {
            b->p = a ;
            a->sz += b->sz ;
         } else if (a->r > b->r) {
            a->p = b ;
            b->sz += a->sz ;
         } else {
            b->p = a ;
            a->r ++ ;
            a->sz += b->sz ;
         }
      }

      Dnode * find() {
         if (this == p) return this ;
         return (p = p->find()) ;
      }
} ;

double cost(int sz) {
   if (sz == 1) return 0 ;
   return sz ;
}

int main(int argc , char * argv[]) {
   ifstream fi(argv[1]) ;
   ofstream fo(argv[2]) ;
   int T ;
   fi >> T ;
   for (int t = 1 ; t <= T ; ++ t) {
      int N ;
      Dnode * arr ;
      fi >> N ;
      arr = new Dnode[N] ;

      for (int n = 0 ; n < N ; ++ n) {
         int num ;
         fi >> num ;
         -- num ;
         arr[num].merge(arr[n]) ;
      }

      double sum = 0 ;
      for (int i = 0 ; i < N ; ++ i) {
         if (&arr[i] == arr[i].find()) {
            sum += cost(arr[i].sz) ;
         }
      }

      fo << "Case #" << t << ": " << fixed << setprecision(6) << sum << endl ;
   }
   return 0;
}

