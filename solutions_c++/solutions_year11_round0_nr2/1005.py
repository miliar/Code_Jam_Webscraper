#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main()
{
  ifstream in("B-large.in");
  ofstream out("answer.txt");
  int T, d, c, N;

  in>>T;
  for(int Test = 1; Test<=T; Test++)
  {
      char Combine[36][4], Oppose[28][3], final[105];
      vector<char> Anwer;
      in>>c;
      for(int i =0; i<c; ++i)
      {
         in>>Combine[i];
      }

      in>>d;
      for(int i =0; i<d; ++i)
      {
         in>>Oppose[i];
      }
      in>>N;
      in>>final;
      for(int i=0; i<N; ++i)
      {
         char ch = final[i];
         Anwer.push_back(ch);
         for( int t = 0; t<c; t++)
         {
            if( Combine[t][0] == Anwer[Anwer.size()-1] && Combine[t][1] == Anwer[Anwer.size()-2] || Combine[t][0] == Anwer[Anwer.size()-2] && Combine[t][1] == Anwer[Anwer.size()-1])
            {
              Anwer.pop_back();
              Anwer.pop_back();
              Anwer.push_back(Combine[t][2]);
              t=-1;   
            }
         }        
         for( int t=0; t<d; t++)
         {
              if(Oppose[t][0] == Anwer[Anwer.size()-1])
              {
                  for( int x=0; x<Anwer.size(); ++x)
                  {
                      if(Anwer[x] == Oppose[t][1])
                       {
                         Anwer.clear();
                         break;        
                       } 
                  }      
              }
              else if(Oppose[t][1] == Anwer[Anwer.size()-1])
              {
                  for( int x=0; x<Anwer.size(); ++x)
                  {
                      if(Anwer[x] == Oppose[t][0])
                       {
                         Anwer.clear();
                         break;        
                       } 
                  }      
              }
         }      
      }
      
      out<<"Case #"<<Test<<": [";
      if(Anwer.size() >0)
       out<<Anwer[0];
      for(int x=1; x<Anwer.size(); ++x)
      {
         out<<", "<<Anwer[x];     
      }
      out<<"]"<<endl;
      
  }
  system("pause");
  return 0;
}
