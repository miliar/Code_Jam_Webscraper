#include <iostream>
#include <fstream>

#include <algorithm>

using namespace std;

int main () {

  fstream infile("A-small-attempt0.in", ios::in);
  fstream outfile("A-small-attempt0.out", ios::out);

  int cases;
  int PD,PG,N;



  infile >> cases;

  for (int case_count = 1;case_count<=cases;case_count++)
  {
      infile >> N >> PD >> PG;

      if ( ( (PD == 100) && (PG==100) ) || ( (PD==0) && (PG==0) )  )
        outfile << "Case #" << case_count << ": Possible" << endl;
      else if ( ( (PD != 100) && (PG==100) ) || ( (PD!=0) && (PG==0) )  )
        outfile << "Case #" << case_count << ": Broken" << endl;
      else
      {
         for (int D=1;D<=min(100,N);D++)
         {
             if( ((D*PD)%100) == 0 )
             {
                 outfile << "Case #" << case_count << ": Possible" << endl;
                 break;
             }
             if( D==min(100,N) )
                 outfile << "Case #" << case_count << ": Broken" << endl;

         }



      }


  }

  infile.close();
  outfile.close();

  return 0;
}
