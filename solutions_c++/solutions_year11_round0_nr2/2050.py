//magicka
#include <string>
#include <vector>
#include <iostream>

using namespace std;

#define N 26
#define NOOP '*'

typedef vector<string> StrVec;

void runmagicka(StrVec& combine, StrVec& reduce, string& invoke)
{
    char combinetable[N][N], reducetable[N][N];
    for(int i=0; i<N; ++i)
       for(int j=0; j<N; ++j)
          {
               combinetable[i][j] = NOOP;
               reducetable[i][j] = NOOP;
          }
    
    for(int i=0; i< combine.size(); ++i)
    {
        int x = combine[i][0] - 'A';
        int y = combine[i][1] - 'A';
        combinetable[x][y] = combinetable[y][x] =  combine[i][2];  
    }
    
    for(int i=0; i< reduce.size(); ++i)
    {
        int x = reduce[i][0] - 'A';
        int y = reduce[i][1] - 'A';
        reducetable[x][y] = reducetable[y][x] = 'R';  
    }
    
    string buffer;
    for(int i=0; i<invoke.size(); ++i)
    {   
       if(buffer.size()>0)
       {          
          int x = buffer[buffer.size()-1] - 'A';
          int y = invoke[i] - 'A';
          if(combinetable[x][y] == NOOP)
          {
             buffer.push_back(invoke[i]);          
              //check if buffer can be reduced
              for(int j=0; j< buffer.size()-1; ++j)
              {
                  x = buffer[j]-'A';    
                  if(reducetable[x][y] !=NOOP)
                  {
                     buffer.clear();
                     break;                  
                  }    
              }                 
          }
          else
          {
             buffer[buffer.size()-1] =  combinetable[x][y];
          }      
       }
       else
       {
           buffer.push_back(invoke[i]);    
       }     
    }
    
    invoke.swap(buffer);
}

int main()
{
    int T;
    cin >> T;
    for(int n= 0; n<T; ++n)
    {
        int  C, D, k;
        StrVec combine, eliminate;
        string invoke;    
         cin >> C;
         for(int i= 0; i<C; ++i)
         {
            string temp;
            cin >> temp;
            combine.push_back(temp);     
         }
         cin >>D;
         for(int i= 0; i<D; ++i)
         {
            string temp;
            cin >> temp;
            eliminate.push_back(temp);     
         } 
         cin >> k;
         cin >> invoke;
         runmagicka(combine, eliminate, invoke);
         //Case #1: [E, A] 
         cout << "Case #"<< n+1<<": [";
         for(int i=0; i<invoke.size(); ++i)
         {
             cout << invoke[i];
             if(i+1 != invoke.size())
             {
                   cout <<", "; 
             }    
         }
         cout <<"]\n";        
    }   
}
