
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ofstream fout ("robots.out");
    ifstream fin ("robots.in");
    int cases,i,num,j,seconds,counter,pos1,pos2,Ogoal,Bgoal,temp;
    
    bool unfinished,switched;
    
    fin>>cases;
    vector<int> numbers;
    vector<char> letters;
    
    for(i=0;i<cases;i++)
    {
    fin>>num;
    numbers.resize(num);
    letters.resize(num);
    for(j=0;j<num;j++)
       {
       fin>>letters[j];
       fin>>numbers[j];                 
       }
       seconds=0;
       counter=0;
       if(num!=0)
         unfinished=true;
    if(unfinished)
      {
      for(j=0;j<num;j++)
         {
         if(letters[j]=='O')
           {
           Ogoal=numbers[j];
           break;}            
         }      
         for(j=0;j<num;j++)
         {
         if(letters[j]=='B')
           {
           Bgoal=numbers[j];
           break;}            
         }      
      }
      pos1=1;
      pos2=1;
    while(unfinished)
       {
switched=true;
       if(pos1<Bgoal)
         pos1++;
         else if(pos1>Bgoal)
                pos1--;
                else if(pos1==Bgoal&&letters[counter]=='B')
                       {
                                                            
                                                             letters[counter]='A';
                                                             switched=false;
                       counter++;
         for(j=0;j<num;j++)
         {
         if(letters[j]=='B')
           {
           Bgoal=numbers[j];
           break;}            
         }                                     
                       }
       if(pos2<Ogoal)
         pos2++;
         else if(pos2>Ogoal)
                pos2--;
                else if(pos2==Ogoal&&letters[counter]=='O'&&switched)
                       {
                                                      
                       counter++;
                       letters[counter-1]='A';
         for(j=0;j<num;j++)
         {
         if(letters[j]=='O')
           {
           Ogoal=numbers[j];
           break;}            
         }                                     
                       }       
                     seconds++;
        if(num==counter){
          unfinished=false;    
          }              
                
       }                                 
                                        
                                                                                          
                        
                        
     cout<<"Case #"<<i+1<<": "<<seconds<<endl;                    
    fout<<"Case #"<<i+1<<": "<<seconds<<endl;                    
    }
   

   
    return 0;
}
