
#include <iostream>
#include <string.h>
using namespace std;

/* We start counting groups until the first in a run is repeated
 * In that case we have the whole sequence recognised and everything
 * that was done before that repetition.
 *  We then have a modular arithmetics problem in our hands. As we 
 *  only have to check how many times the whole sequence of runs is 
 *  ran through, and then just add the remainder.
 *  We end this process earlier if we got R runs in our way.
 * */

unsigned int grps[1000], runs[1000];
int first[1000];
unsigned int T, k, R, N, l;


int main(int argc, char *argv[])
{
   cin >> T;
   for(unsigned int i = 0; i<T; i++)
   {
      unsigned int l=0, sum = 0, r, headsz, tailsz, tailsum, headsum, *tail;
 
      cin >> R;
      cin >> k;
      cin >> N;
      
      for(unsigned int j = 0; j<N; j++)
         cin >> grps[j];

      for(r=0;r<R;r++)
      {
         unsigned int s = 0;
         for(int j=0; j<N && s+grps[l]<=k; j++, l=(l+1)%N)
            s+=grps[l];
         sum+=s;
      }

      cout << "Case #" << i+1 << ": "<< sum << endl;
   }

   return 0;
}
  

