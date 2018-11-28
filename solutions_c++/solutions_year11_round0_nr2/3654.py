
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ofstream fout ("magick.out");
    ifstream fin ("magick.in");
   int cases,i,combo,oppose,j,characters,k,m,l;
   bool repeat,cleared;
   string master,combo1,combo2;
   char first,second;
   vector<string> combos;
   vector<string> opposes;
   vector<char> elements;
   fin>>cases;
   for(i=0;i<cases;i++)
      {
      fin>>combo;
      combos.resize(combo);
      for(j=0;j<combo;j++)
         {
         fin>>combos[j];         
         }
      fin>>oppose;   
      opposes.resize(oppose);
    
      for(j=0;j<oppose;j++)
         {
         fin>>opposes[j];
          }     
       fin>>characters;   
       fin>>master;
       elements.resize(0);
       for(j=0;j<characters;j++)
          {
                    //for(l=0;l<elements.size();l++)
             //cout<<elements[l]<<",";
             //cout<<endl;
          elements.push_back (master[j]);
          do{
                             repeat=false;
          if(elements.size()>1) 
            {
            first=elements[elements.size()-1];
            second=elements[elements.size()-2];
            combo1="";
            combo2="";
                combo1+=first;
                combo1+=second;
                combo2+=second;
                combo2+=first; 
           for(k=0;k<combos.size();k++)
              {
              if(combo1==combos[k].substr(0,2)||combo2==combos[k].substr(0,2))
                {
                elements.pop_back();
                elements[elements.size()-1]=combos[k][2];     
                repeat=true;                                                          
                }                         
              }                                       
            }
            }while(repeat);                      
          for(k=0;k<elements.size();k++)
             for(m=k+1;m<elements.size();m++)
                {
                first=elements[k];
                second=elements[m];
                combo1="";
                combo2="";
                combo1+=first;
                combo1+=second;
                combo2+=second;
                combo2+=first;
                cleared=false;
                for(l=0;l<opposes.size();l++)
                   {
                   if(combo1==opposes[l]||combo2==opposes[l])
                     {
                     elements.resize(0);
                                                  cleared=true;
                                                  break;           
                                                             }   
                                                             if(cleared)
                                                             break;                       
                                             
                   }
                                             
                
                
                
                }
                      
                                
          }
          fout<<"Case #"<<i+1<<": [";
          cout<<"Case #"<<i+1<<endl;
          for(j=0;j<elements.size();j++)
             {
             fout<<elements[j];
             if(j<elements.size()-1)
             fout<<", ";
             }
             fout<<"]"<<endl;
                       
                       
                       
                       
      }

   
    return 0;
}
