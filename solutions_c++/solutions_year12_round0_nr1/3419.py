#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
using namespace std;

#define forn(i,n) for(int i=0; i<n; i++)
#define dbg(n) cout<<#n<<": "<<n<<endl;
#define mp make_pair

char exampleInput[][108] = 
{
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv",
    "y qee"
};
char exampleOutput[][108] =
{
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up",
    "a zoo" 
};
int exampleLength = 3;

map<char,char> convert;

int T;
int main()
{
    convert['z']='q';
    convert['q']='z';
    forn(i, exampleLength)
    {
     forn(j, 108)
     {
      if(exampleInput[i][j]==0)
      {
       break;
      }       
      convert[exampleInput[i][j]] = exampleOutput[i][j]; 
     }        
    }
    
    
    ifstream input("A.in");
    ofstream output("A.out");
    input>>T;
    char pointer[10];
    input.getline(pointer,5);
    forn(t, T)
    {
        char G[108];
        char S[108];
        input.getline(G, 108);
        forn(i, 108)
        {
         if(G[i]==0)
         {
          S[i] = 0;
          break;
         }
         S[i] = convert[G[i]]; 
        } 
        output<<"Case #"<<t+1<<": "<<S<<endl;       
    }
    
}
