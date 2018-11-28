#include <fstream.h>
#include <algorithm>


int main()
{

      int T,P,Q;

      int i,j;

      int cas;

      ifstream fin("c:\\test\\C-small-attempt0.in");
      ofstream fout("c:\\test\\bribe.out");

      fin >> T;

      int *cells;

      int *released;

      int bribes;

      int min_bribe;


      for(cas = 1; cas <= T; cas++)
      {

                   fin >> P >> Q;

                   cells = new int[P];
                   released = new int[Q];

                   min_bribe = 100000; //its to say infinity




                   for(j = 0; j < Q; j++) {
                         fin >> released[j];

                   }

                     do
                     {
                             for(j = 0; j < P; j++)
                                 cells[j] = 1;



                             bribes = 0;



                             for(i = 0; i < Q; i++)
                             {

                                 cells[released[i] - 1] = -1;



                                 for(j = released[i]; j < P && cells[j] != -1; j++)
                                           bribes++;

                                 for(j = released[i] - 2; j >= 0 && cells[j] != -1; j--)
                                           bribes++;








                             }
                             if(min_bribe > bribes)
                                      min_bribe = bribes;



                              bribes = 0;


                     } while ( next_permutation (released,released+Q) );





            fout << "Case #" << cas << ": " << min_bribe << endl;

      }


      return 0;
}
