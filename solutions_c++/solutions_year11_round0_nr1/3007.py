#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main()
{
  ifstream in("A-large.in");
  ofstream out("out.txt");
  int T;
  in>>T;
  for(int c = 1; c<=T; c++)
  {
      vector<int> bots;
      vector<int> buttons;
      int N;
      in>>N;
      for(int i =0; i<N; ++i)
      {
         char r;
         int p;
         in>>r>>p;
         bots.push_back(r);
         buttons.push_back(p);    
      }
      
      int o=1, b=1, i=0, sec =0;
      while(i< buttons.size())
      {
         switch( bots[i] )
         {
               case 'B':
                    {
                     if(buttons[i] < b)
                       --b;
                     else if(buttons[i] >b)
                       ++b;
                     else
                      ++i;
                     
                     int targetIndex = i, target;
                     while(bots[targetIndex] != 'O' && targetIndex < bots.size())
                       targetIndex++;
                     
                     if(buttons[targetIndex] < o)
                      --o;
                     else if(buttons[targetIndex] > o)
                      ++o;
                      
                     break;   
                    }
              case 'O':
                    {
                     if(buttons[i] < o)
                       --o;
                     else if(buttons[i] >o)
                       ++o;
                     else
                      ++i;
                     
                     int targetIndex = i, target;
                     while(bots[targetIndex] != 'B' && targetIndex < bots.size())
                       targetIndex++;
                     
                     if(buttons[targetIndex] < b)
                      --b;
                     else if(buttons[targetIndex] > b)
                      ++b;
                      
                     break;   
                    }  
         }
         ++sec;
      }
      out<<"Case #"<<c<<": "<<sec<<endl;
  }
  //system("pause");
}
