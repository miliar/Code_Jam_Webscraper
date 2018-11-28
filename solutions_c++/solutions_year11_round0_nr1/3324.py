#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream cin("Test.txt");
    ofstream cout("Output.txt");
    long long Count, L;
    char prev , current;
    int LO, LB, temp, d;
    int NumOrder;
    
    
    int TestNum;
    cin >> TestNum;
    
    for(int j = 0; j < TestNum; j++)
    {
            LO = 1;
            LB = 1;
            Count = 0;
            prev = 'a';
            
    cin >> NumOrder;
    
    for(int i=0; i < NumOrder; i++)
    {
            cin >> current;
            if(prev == 'a')
                    {
                           if(current == 'O')
                                  {
                                      cin >> LO;
                                      Count += LO;
                                      L = Count;
                                   }
                           else
                                   {
                                       cin >> LB;
                                       Count += LB;
                                       L = Count;
                                   }
                           prev = current;   
                           continue;
                    }
            if(current == prev)
              {
                       if(current == 'O')
                                  {
                                         cin >> temp;
                                         d = temp - LO;
                                         if(temp < LO)
                                                 d = -1*d;
                                         LO = temp;
                                         Count += d+1;
                                         L += d+1;
                                  }
                       if(current == 'B')
                                  {
                                         cin >> temp;
                                         d = temp - LB;
                                         if(temp < LB)
                                                 d = -1*d;
                                         LB = temp;
                                         Count += d+1;
                                         L += d+1;
                                  }                               
              }
              else
              {
                  if(current == 'O')
                                  {
                                         cin >> temp;
                                         d = temp - LO;
                                         if(temp < LO)
                                                 d = -1*d;
                                         LO = temp;
                                         if((d+1) <= L)
                                         {
                                                  Count++;
                                                  L = 1;
                                         }
                                         else
                                         {
                                             Count += d+1 - L;
                                             L = d+1 - L;
                                         }
                                         prev = 'O';
                                  }
                  if(current == 'B')
                                  {
                                         cin >> temp;
                                         d = temp - LB;
                                         if(temp < LB)
                                                 d = -1*d;
                                         LB = temp;
                                         if((d+1) <= L)
                                         {
                                                  Count++;
                                                  L = 1;
                                         }
                                         else
                                         {
                                             Count += d+1 - L;
                                             L = d+1 - L;
                                         }
                                         prev = 'B';
                                  } 
                                  
              }      
    }
    cout << "Case #" << j+1 << ": "<< Count << endl;
    
   }
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
