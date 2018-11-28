//welcome to code jam
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    int currentcase, cases = 0;
    cin >> cases;
    cin.ignore();
    for(currentcase = 1; currentcase <= cases; currentcase++)
             {
              string input = "";
              int count, answer;
              count = 0;
              getline(cin,input);
              cout << "Case #" << currentcase << ": ";
              
              int charindex [18];
              for (int i = 0; i <=18; i++)
                  {
                       charindex[i] = 0;
                  }
              
              // Find w
              while (charindex[0] <= input.length())
                  {
                   if (input.substr(charindex[0],1) == "w")
                      {
                       // Find e
                       charindex[1] = charindex[0] + 1;
                       while (charindex[1] <= input.length())
                             {
                              if (input.substr(charindex[1],1) == "e")
                                 {
                                  // Find l
                                  charindex[2] = charindex[1] + 1;
                                  while (charindex[2] <= input.length())
                                        {
                                         if (input.substr(charindex[2],1) == "l")
                                         {
                                          // Find c
                                          charindex[3] = charindex[2] + 1;
                                          while (charindex[3] <= input.length())
                                                {
                                                 if (input.substr(charindex[3],1) == "c")
                                                    {
                                                     // Find o
                                                     charindex[4] = charindex[3] + 1;
                                                     while (charindex[4] <= input.length())
                                                           {
                                                            if (input.substr(charindex[4],1) == "o")
                                                               {
                                                                //Find m
                                                                charindex[5] = charindex[4] + 1;
                                                                while (charindex[5] <= input.length())
                                                                      {
                                                                       if (input.substr(charindex[5],1) == "m")
                                                                          {
                                                                           //Find e
                                                                           charindex[6] = charindex[5] + 1;
                                                                           while (charindex[6] <= input.length())
                                                                                 {
                                                                                  if (input.substr(charindex[6],1) == "e")
                                                                                     {       
                                                                                      //Find space
                                                                                      charindex[7] = charindex[6] + 1;
                                                                                      while (charindex[7] <= input.length())
                                                                                            {
                                                                                             if (input.substr(charindex[7],1) == " ")
                                                                                                {
                                                                                                 //Find t
                                                                                                 charindex[8] = charindex[7] + 1;
                                                                                                 while (charindex[8] <= input.length())
                                                                                                       {
                                                                                                        if (input.substr(charindex[8],1) == "t")
                                                                                                           {
                                                                                                            //Find o
                                                                                                            charindex[9] = charindex[8] + 1;
                                                                                                            while (charindex[9] <= input.length())
                                                                                                                  {
                                                                                                                   if (input.substr(charindex[9],1) == "o")
                                                                                                                      {
                                                                                                                       //Find space
                                                                                                                       charindex[10] = charindex[9] + 1;
                                                                                                                       while (charindex[10] <= input.length())
                                                                                                                             {
                                                                                                                              if (input.substr(charindex[10],1) == " ")
                                                                                                                                 {
                                                                                                                                  //Find c
                                                                                                                                  charindex[11] = charindex[10] + 1;
                                                                                                                                  while (charindex[11] <= input.length())
                                                                                                                                        {
                                                                                                                                         if (input.substr(charindex[11],1) == "c")
                                                                                                                                            {
                                                                                                                                             //Find o
                                                                                                                                             charindex[12] = charindex[11] + 1;
                                                                                                                                             while (charindex[12] <= input.length())
                                                                                                                                                   {
                                                                                                                                                    if (input.substr(charindex[12],1) == "o")
                                                                                                                                                       {
                                                                                                                                                        //Find d
                                                                                                                                                        charindex[13] = charindex[12] + 1;
                                                                                                                                                        while (charindex[13] <= input.length())
                                                                                                                                                              {
                                                                                                                                                               if (input.substr(charindex[13],1) == "d")
                                                                                                                                                                  {
                                                                                                                                                                   //Find e
                                                                                                                                                                   charindex[14] = charindex[13] + 1;
                                                                                                                                                                   while (charindex[14] <= input.length())
                                                                                                                                                                         {
                                                                                                                                                                          if (input.substr(charindex[14],1) == "e")
                                                                                                                                                                             {
                                                                                                                                                                              //Find space
                                                                                                                                                                              charindex[15] = charindex[14] + 1;
                                                                                                                                                                              while (charindex[15] <= input.length())
                                                                                                                                                                                    {
                                                                                                                                                                                     if (input.substr(charindex[15],1) == " ")
                                                                                                                                                                                        {
                                                                                                                                                                                         //Find j
                                                                                                                                                                                         charindex[16] = charindex[15] + 1;
                                                                                                                                                                                         while (charindex[16] <= input.length())
                                                                                                                                                                                               {
                                                                                                                                                                                                if (input.substr(charindex[16],1) == "j")
                                                                                                                                                                                                   {
                                                                                                                                                                                                    //Find a
                                                                                                                                                                                                    charindex[17] = charindex[16] + 1;
                                                                                                                                                                                                    while (charindex[17] <= input.length())
                                                                                                                                                                                                          {
                                                                                                                                                                                                           if (input.substr(charindex[17],1) == "a")
                                                                                                                                                                                                              {
                                                                                                                                                                                                               //Find m
                                                                                                                                                                                                               charindex[18] = charindex[17] + 1;
                                                                                                                                                                                                               while (charindex[18] <= input.length())
                                                                                                                                                                                                                     {
                                                                                                                                                                                                                      if (input.substr(charindex[18],1) == "m")
                                                                                                                                                                                                                         {
                                                                                                                                                                                                                          count++;                                                                          
                                                                                                                                                                                                                         }
                                                                                                                                                                                                                      charindex[18]++;
                                                                                                                                                                                                                     }                                                                                                        
                                                                                                                                                                                                              }
                                                                                                                                                                                                           charindex[17]++;
                                                                                                                                                                                                          }                                       
                                                                                                                                                                                                   }
                                                                                                                                                                                                charindex[16]++;
                                                                                                                                                                                               }                                                                          
                                                                                                                                                                                        }
                                                                                                                                                                                     charindex[15]++;
                                                                                                                                                                                    }                                      
                                                                                                                                                                             }
                                                                                                                                                                          charindex[14]++;
                                                                                                                                                                         }                                                                          
                                                                                                                                                                  }
                                                                                                                                                               charindex[13]++;
                                                                                                                                                              }                                                                          
                                                                                                                                                       }
                                                                                                                                                    charindex[12]++;
                                                                                                                                                   }                                                                          
                                                                                                                                            }
                                                                                                                                         charindex[11]++;
                                                                                                                                        }                                                                                   
                                                                                                                                 }
                                                                                                                              charindex[10]++;
                                                                                                                             }                                                                   
                                                                                                                       }
                                                                                                                   charindex[9]++;
                                                                                                                  }                                                                   
                                                                                                           }
                                                                                                        charindex[8]++;
                                                                                                       }                                                                         
                                                                                                }
                                                                                             charindex[7]++;
                                                                                            }                                                                   
                                                                                     }
                                                                                  charindex[6]++;
                                                                                 }                                                                          
                                                                          }
                                                                       charindex[5]++;
                                                                      }
                                                               }
                                                            charindex[4]++;
                                                           }
                                                    }
                                                 charindex[3]++;
                                                }
                                         }
                                         charindex[2]++;
                                        }
                                 }
                              charindex[1]++;
                             }
                       
                      }
                   charindex[0]++;
                  }
             answer = int((double(count / 10000.0) - int(count / 10000)) * 10000);
             printf("%04d\n", answer);
             }
    return EXIT_SUCCESS;
}
