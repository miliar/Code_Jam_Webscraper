#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main()
{
  ifstream in("B-large.in");
  ofstream out("out.txt");
  int T;
  in>>T;
  for(int cas = 1; cas<=T; cas++)
  {
      int c;
      int N;
      char comb[36][4], opp[28][3], str[105];
      vector<char> elem;
      in>>c;
      for(int i =0; i<c; ++i)
      {
         in>>comb[i];
      }
      int d;
      in>>d;
      for(int i =0; i<d; ++i)
      {
         in>>opp[i];
      }
      in>>N;
      in>>str;
      for(int i=0; i<N; ++i)
      {
         char ch = str[i];
         elem.push_back(ch);
         for( int t = 0; t<c; t++)
         {
            if( comb[t][0] == elem[elem.size()-1] && comb[t][1] == elem[elem.size()-2] || comb[t][0] == elem[elem.size()-2] && comb[t][1] == elem[elem.size()-1])
            {
              elem.pop_back();
              elem.pop_back();
              elem.push_back(comb[t][2]);
              t=-1;   
            }
         }        
         for( int t=0; t<d; t++)
         {
              if(opp[t][0] == elem[elem.size()-1])
              {
                  for( int x=0; x<elem.size(); ++x)
                  {
                      if(elem[x] == opp[t][1])
                       {
                         elem.clear();
                         break;        
                       } 
                  }      
              }
              else if(opp[t][1] == elem[elem.size()-1])
              {
                  for( int x=0; x<elem.size(); ++x)
                  {
                      if(elem[x] == opp[t][0])
                       {
                         elem.clear();
                         break;        
                       } 
                  }      
              }
         }      
      }
      
      out<<"Case #"<<cas<<": [";
      if(elem.size() >0)
       out<<elem[0];
      for(int x=1; x<elem.size(); ++x)
      {
         out<<", "<<elem[x];     
      }
      out<<"]"<<endl;
      
  }
  //system("pause");
}
