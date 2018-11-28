#include<fstream.h>
#include<stdlib.h>

#define ARRAYSIZE 10

int main()

{
    
      long long T;
      int N;
      int K; 
      
      long long i;
      int j,c;
      char *output;
      
      bool snapper[ARRAYSIZE];
      bool power[ARRAYSIZE];
      

      ifstream fin("A-small-attempt9.in");

      ofstream fout("A-small-attempt9.out");
      
      if(!fin)
         exit(0);
      
      fin >> T;     
      
      
      for(i = 1; i <= T; i++)
      {
            /*crucial*/
            memset(snapper,false,ARRAYSIZE);
            memset(power,false,ARRAYSIZE);            
        
            power[0] = true;           
            
            fin >> N >> K;       
          
         
            for(j = 1; j <= K; j++)
            {                    
                                                    
                  for(c = 0; c < N; c++)
                  {
                     if(power[c] == true)
                        snapper[c] = !snapper[c];
                                   
                  }
                  for(c = 0; c < N - 1; c++)
                  {                        
                                      
                     if(power[c] == true && snapper[c] == true)
                     {
                          power[c + 1] = true;       
                     }
                     else if(snapper[c] == false)
                     {                                               
                          power[c + 1] = false; 
                              
                      }                     
                        
                  }                     
                 
            }          
            
            if(snapper[N - 1] == true && power[N - 1] == true)
               output = "ON";
            else
               output = "OFF";
              
            fout <<"Case #" <<(i) << ": " << output <<"\n";                
            
      }
      
    return 0;
    
}
