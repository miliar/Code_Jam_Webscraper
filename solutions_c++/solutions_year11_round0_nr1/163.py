#include<iostream>
#include<fstream>
using namespace std;

class Job {
   public :
      char P ;
      bool done ;
      Job * dep ;
} ;

int main(int argc , char * argv[]) {
   ifstream fi(argv[1]) ;
   ofstream fo(argv[2]) ;
   int T ;
   fi >> T ;
   for (int t = 1 ; t <= T ; ++ t) {
      int N ;
      fi >> N ;
      Job O[100] , B[100] , Dummy ;
      int OL = 0 , BL = 0 ;

      Job * prev = &Dummy ;
      Dummy.done = true ;
      for (int n = 0 ; n < N ; ++ n) {
         char R ; int P ;
         fi >> R >> P ;
         // cout << "'" << R << "'" << P << endl ;
         switch (R) {
            case 'B':
               B[BL].P = P - 1 ;
               B[BL].done = false ;
               B[BL].dep = prev ;
               prev = B + BL ;
               BL ++ ;
               break ;
            case 'O':
               O[OL].P = P - 1 ;
               O[OL].done = false ;
               O[OL].dep = prev ;
               prev = O + OL ;
               OL ++ ;
               break ;
         }
      }

      int posB = 0 , posO = 0 ;
      int jobB = 0 , jobO = 0 ;
      int Time = 0 ;
      while (jobB != BL || jobO != OL) {
         bool doneB = false , doneO = false ;
         Time ++ ;
         if (jobB < BL) {
            if (B[jobB].dep->done && B[jobB].P == posB) {
               doneB = true ;
            } else if (B[jobB].P < posB) {
               posB -- ;
            } else if (B[jobB].P > posB) {
               posB ++ ;
            }
         }
         if (jobO < OL) {
            if (O[jobO].dep->done && O[jobO].P == posO) {
               doneO = true ;
            } else if (O[jobO].P < posO) {
               posO -- ;
            } else if (O[jobO].P > posO) {
               posO ++ ;
            }
         }

         if (doneB) {
            B[jobB].done = true ;
            ++ jobB ;
         }
         if (doneO) {
            O[jobO].done = true ;
            ++ jobO ;
         }
      }

      fo << "Case #" << t << ": " << Time << endl ;
   }
   return 0;
}

