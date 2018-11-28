#include <string>
#include <iostream>
#include <sstream>

using namespace std;

int main()
{
    int cases;
    string caseline;
    
    getline(cin, caseline);
    
    istringstream casestrm(caseline);
    
    casestrm >> cases;
    
    
    
    for (int i=0; i<cases;i++)
    {
    
    long long int count = 0;
    
    string tomatch;
    
    getline(cin, tomatch);
    
    size_t indexes[25] = {0};
    
    indexes[0] = tomatch.find("w", 0);
    while (indexes[0] != string::npos)
    {
      indexes[1] = tomatch.find("e", indexes[0]+1);
      while (indexes[1] != string::npos)
      {


        indexes[2] = tomatch.find("l", indexes[1]+1);
        while (indexes[2] != string::npos)
        {


          indexes[3] = tomatch.find("c", indexes[2]+1);
          while (indexes[3] != string::npos)
          {



            indexes[4] = tomatch.find("o", indexes[3]+1);
            while (indexes[4] != string::npos)
            {



              indexes[5] = tomatch.find("m", indexes[4]+1);
              while (indexes[5] != string::npos)
              {



                indexes[6] = tomatch.find("e", indexes[5]+1);
                while (indexes[6] != string::npos)
                {


                  indexes[7] = tomatch.find(" ", indexes[6]+1);
                  while (indexes[7] != string::npos)
                  {



                    indexes[8] = tomatch.find("t", indexes[7]+1);
                    while (indexes[8] != string::npos)
                    {



                      indexes[9] = tomatch.find("o", indexes[8]+1);
                      while (indexes[9] != string::npos)
                      {


                        indexes[10] = tomatch.find(" ", indexes[9]+1);
                        while (indexes[10] != string::npos)
                        {


                          indexes[11] = tomatch.find("c", indexes[10]+1);
                          while (indexes[11] != string::npos)
                          {



                            indexes[12] = tomatch.find("o", indexes[11]+1);
                            while (indexes[12] != string::npos)
                            {


                              indexes[13] = tomatch.find("d", indexes[12]+1);
                              while (indexes[13] != string::npos)
                              {


                                indexes[14] = tomatch.find("e", indexes[13]+1);
                                while (indexes[14] != string::npos)
                                {


                                  indexes[15] = tomatch.find(" ", indexes[14]+1);
                                  while (indexes[15] != string::npos)
                                  {


                                    indexes[16] = tomatch.find("j", indexes[15]+1);
                                    while (indexes[16] != string::npos)
                                    {


                                      indexes[17] = tomatch.find("a", indexes[16]+1);
                                      while (indexes[17] != string::npos)
                                      {


                                        indexes[18] = tomatch.find("m", indexes[17]+1);
                                        while (indexes[18] != string::npos)
                                        {
                                          count++;
                                          if (count == 10000) { count = 0; }
                                          indexes[18] = tomatch.find("m", indexes[18]+1);
                                        }
                                        
                                        indexes[17] = tomatch.find("a", indexes[17]+1);
                                      }
                                      
                                      indexes[16] = tomatch.find("j", indexes[16]+1);
                                    }
                                    

                                    indexes[15] = tomatch.find(" ", indexes[15]+1);
                                  }
                                  
                                  indexes[14] = tomatch.find("e", indexes[14]+1);
                                }
                                
                                indexes[13] = tomatch.find("d", indexes[13]+1);
                              }
                              
                              indexes[12] = tomatch.find("o", indexes[12]+1);
                            }
                            
                            indexes[11] = tomatch.find("c", indexes[11]+1);
                          }
                          
                          indexes[10] = tomatch.find(" ", indexes[10]+1);
                        }
                        
                        indexes[9] = tomatch.find("o", indexes[9]+1);
                      }
                        
                      indexes[8] = tomatch.find("t", indexes[8]+1);
                    }
                    
                    indexes[7] = tomatch.find(" ", indexes[7]+1);
                  }
                  
                  indexes[6] = tomatch.find("e", indexes[6]+1);
                }
                
                indexes[5] = tomatch.find("m", indexes[5]+1);
              }
              
              indexes[4] = tomatch.find("o", indexes[4]+1);
            }
            
            indexes[3] = tomatch.find("c", indexes[3]+1);
          }
          
          indexes[2] = tomatch.find("l", indexes[2]+1);
        }
        
        indexes[1] = tomatch.find("e", indexes[1]+1);
      }
      
      indexes[0] = tomatch.find("w", indexes[0]+1);
    }

    printf("Case #%d: %04d\n", i+1, count);
    }
}
