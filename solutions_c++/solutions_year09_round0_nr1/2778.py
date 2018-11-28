#include <stdio>
#include <string>
#include <stdlib>
#include <fstream.h>





int main()
{  

      int N;
      int L;
      int D;

      int i,j,k,found,count;

      string *words;
      string *token;
      char cas[5000];


     ifstream fin("A-small-attempt0.in");

	  ofstream fout("A-small-attempt0.out");



     fin >> L >> D >> N;


     words = new string[D];


     for(i = 0; i < D; i++)
     {
         fin >> words[i];
     }

     for(j = 0; j < N; j++)
     {

           count = 0;

           fin >> cas;

           token = new string[L];



           k = 0;
           for(i = 0; i < L; i++)
           {

                  if(cas[k] == '(')
                  {
                       while(cas[k + 1] != ')')
                       {

                            token[i].append(cas[k+1]);
                            k++;

                       }
                       k += 2;



                  }
                  else
                  {

                        token[i].append(cas[k]);
                        k++;

                  }    


            }

            for(i = 0; i < D; i++)
            {


                found = 0;
                for(k = 0; k < L; k++)
                {

                       if(token[k].find(words[i][k])!= -1)
                           found++;




                }

                if(found == L)
                     count++;

             }

             fout << "Case #" <<(j+1) << ": " << count << endl;
     }




     


}