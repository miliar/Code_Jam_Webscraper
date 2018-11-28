#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream in("in.txt");
    ofstream out("results.txt");
    int t,y;
    int L,D,N;
    string tmp;
int q;
int z;
int res;
    vector<string> existing_words;
    vector<string> letter;
    
    
    in>>L;in>>D;in>>N;

    for(t=0;t<D;t++)
    {
                tmp="";
                in>>tmp;
                existing_words.push_back(tmp);
    }

   int e;
   
for(e=0;e<N;e++)    
{    
tmp="";
  in>>tmp;
  string le="";
  y=0;  
  letter.erase(letter.begin(),letter.end());
  for(t=0;t<tmp.length();t++)
  {
               if(tmp[t]=='(') {y=1;continue;}
               if(tmp[t]==')') {letter.push_back(le);le="";y=0;continue;}
                           if(y==1) le+=tmp[t];
                           else {le+=tmp[t];letter.push_back(le);le="";continue;}
  }

res=0;

for(t=0;t<existing_words.size();t++)
{
                                    q=1;
     for(y=0;y<existing_words[t].length();y++)
     {
         if(q==0) {break;}
         q=0;    
              
         for(z=0;z<letter[y].length();z++)
         {
                                         
             if(existing_words[t][y]==letter[y][z]) q=1;
         }
     }
     if(q==1) res++;                                    
}

cout<<res<<endl;
out<<"Case #"<<e+1<<": "<<res<<endl;
}
      
   // system("PAUSE");
    return EXIT_SUCCESS;
}
