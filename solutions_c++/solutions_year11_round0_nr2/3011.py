#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
   int T;
   cin >> T;
   for(int i = 0; i < T; i++)
   {
      vector< string > combinations;
      vector< string > cancellations;
      int C;
      cin >> C;
      for(int j = 0; j < C; j++)
      {
         string x;
         cin >> x;
         combinations.push_back(x);
      }
      int D;
      cin >> D;
      for(int j = 0; j < D; j++)
      {
         string x;
         cin >> x;
         cancellations.push_back(x);
      }
      int N;
      cin >> N;
      string x;
      cin >> x;
      string out;
      if( N == 1 )
         out = x;
      else
      {
         out = "";
         out += x[0];
         for(int j = 1; j < N; j++)
         {
            out += x[j];
            //combinations first
            bool combinationFound = false;
            for(int k = 0; k < combinations.size(); k++)
            {
               if( ((out[out.size()-1] == combinations[k][0]) && (out[out.size()-2] == combinations[k][1])) || ((out[out.size()-1] == combinations[k][1]) && (out[out.size()-2] == combinations[k][0])))
               {
                  out = out.substr(0,out.size()-2);
                  out += combinations[k][2];
                  combinationFound = true;
                  break;
               }
            }
            if(combinationFound)
               continue;
            //cancelllations
            for(int k = 0; k < cancellations.size(); k++)
            {
               if(x[j] == cancellations[k][0])
               {
                  for(int l = 0; l < out.size() - 1; l++)
                     if(out[l] == cancellations[k][1])
                     {
                        out.clear();
                        break;
                     }
                  if(out.size() == 0)
                     break;
               }
               if(x[j] == cancellations[k][1])
               {
                  for(int l = 0; l < out.size() - 1; l++)
                     if(out[l] == cancellations[k][0])
                     {
                        out.clear();
                        break;
                     }
                  if(out.size() == 0)
                     break;
               }
            }
         }
      }
      std::cout << "Case #" << i+1 << ": [";
      for(int j = 0; j < out.size(); j++)
      {
         std::cout << out[j];
         if( j != out.size()-1 )
            std::cout << ", ";
      }
      std::cout << "]" << std::endl;
   }
}