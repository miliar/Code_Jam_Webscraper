#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

std::vector <char>seq;


void addChar(char c,char combine[26][26],char oppose[26][26], char* occur)
{
     if (seq.size()==0)
     {
        seq.push_back(c);
           occur[c-'A'] = 1;
           return;
           }
     else
       {
            char temp = combine[c-'A'][seq.back()-'A'];
            if(temp != 0)
            { 
                    occur[seq.back()-'A'] = occur[seq.back()-'A'] -1;
                      seq.pop_back(); 
                      addChar(temp,combine,oppose,occur);
                      return;
            }
            else
            {
                int i;
                for (i=0; i<26; i++)
                {
                    if(occur[i] > 0)
                    {
                        if(oppose[c-'A'][i] == 1) 
                        {
                            memset(occur,0,26);
                            seq.clear();
                            return;
                        }
                    }
                }
                seq.push_back(c);
               occur[c-'A'] = occur[c-'A'] + 1;
               return;
            }
       }
 }
 
int main()
{
     ifstream ifile; ifile.open("B-large.in", ios::in);
     ofstream ofile; ofile.open("output.txt",ios::out);
     char occur[26];
     char combine[26][26];
     char oppose[26][26];
     memset(occur,0,26);
     memset(oppose,0,26*26);
     memset(combine,0,26*26);
     
     
     int cases; ifile>> cases;
     int r,num;
     for(r=1; r<=cases; r++)
     {
         ifile>> num;
         string str;
         int i;
         for (i=0; i<num; i++)
         {
         ifile>> str;
         
         combine[str[0]-'A'][str[1]-'A'] = str[2];
         combine[str[1]-'A'][str[0]-'A'] = str[2];
         }
     
          ifile>> num;

         for (i=0; i<num; i++)
         {
             ifile>> str;
             oppose[str[0]-'A'][str[1]-'A'] = 1;
             oppose[str[1]-'A'][str[0]-'A'] = 1;
         }
     
          ifile>> num;
          char c;
          for(i=0; i<num; i++)
          {
                   ifile>>c;
                   addChar(c,combine,oppose, occur);
                   
          }
          
          ofile<<"Case #"<<r<<": [";
        
         for(i=0; i<seq.size();i++)
         {
                  ofile<<seq[i];
                  if((i<seq.size()-1) && (seq.size()>1))
                  ofile<<", ";
         }
         ofile<<"]"<<endl;
         
         seq.clear();    
         memset(occur,0,26);
         memset(oppose,0,26*26);
         memset(combine,0,26*26);  
     }  
     
    return 0;
}
