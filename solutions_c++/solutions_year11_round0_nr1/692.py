/*
ID: dhxav
PROG: bot_trust
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    ofstream fout ("A-large.out");
    ifstream fin ("A-large.in");
    
    int T, N;
    char colour[100];
    int number[100];
    int timer;
    int next, distance, nextdist;
    int positionB, positionO;
    
    fin >> T;

    for (int i=0; i<T; i++)
    {
        fin >> N;
        
        for (int j=0; j<N; j++)
        {
            fin >> colour[j] >> number[j];
        }
        
        timer = 0;
        positionB = 1;
        positionO = 1;
        
        for (int j=0; j<N; j++)
        {
            if (colour[j]=='B')
            {
               for (int k=j+1; k<N; k++)
               {
                   if (colour[k]=='O')
                   {
                      next = k;
                      break;
                   }
               }
                   
               if (positionB>number[j])
                  distance = positionB - number[j];
               else
                   distance = number[j] - positionB;
                   
               timer += distance+1;
               positionB = number[j];
                   
               if (positionO>number[next])
               {
                  nextdist = positionO - number[next];
                  if (distance+1<nextdist)
                     positionO -= (distance+1);
                  else
                      positionO = number[next];
               }
               else
               {
                   nextdist = number[next] - positionO;
                   if (distance+1<nextdist)
                      positionO += (distance+1);
                   else
                       positionO = number[next];
               }
            }
               
            if (colour[j]=='O')
            {
               for (int k=j+1; k<N; k++)
               {
                   if (colour[k]=='B')
                   {
                      next = k;
                      break;
                   }
               }
                   
               if (positionO>number[j])
                  distance = positionO - number[j];
               else
                   distance = number[j] - positionO;
                   
               timer += distance+1;
               positionO = number[j];
                   
               if (positionB>number[next])
               {
                  nextdist = positionB - number[next];
                  if (distance+1<nextdist)
                     positionB -= (distance+1);
                  else
                      positionB = number[next];
               }
               else
               {
                   nextdist = number[next] - positionB;
                   if (distance+1<nextdist)
                      positionB += (distance+1);
                   else
                       positionB = number[next];
               }
            }
        }
               
        fout << "Case #" << i+1 << ": " << timer << endl;
    }
    
    return 0;
}
