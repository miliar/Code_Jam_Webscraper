#include <cstdlib>
#include <iostream>
#include <string>
#include <set>
using namespace std;
int n,l,d;
string S[5005];
set<char> T[20];


string getLine() 
  {
  string str;
  while(!feof(stdin)) 
    {
    char c=fgetc(stdin);
    if(c == 13)continue;
    if(c == 10)return str;
    str += c;
    }
  return str;
  }

void wczytaj()
{
     int k=1;
  for(int i=1;i<=15;i++)T[i].clear();
  int byl=0;
  while(!feof(stdin))
   {
    char c = fgetc(stdin);
    if(c == '(') {byl=1; continue;}
    if(c== ')'){  byl=0;  }
    if(c == 10) break;
    if(c!=')'){T[k].insert(c);
   
   // cout<<"do "<< k << " wkladam " << c <<" "<<endl;
   }
     if(byl==0)k++;
    }
}

int sprawdz()
{
    int res=0;
    for(int i=1;i<=d;i++)
    for(int k=1;k<=l;k++)
     {
            if(T[k].find(S[i][k-1])==T[k].end())break;
            if(k==l)res++;       
     }  
    return res;
}

int main(int argc, char *argv[])
{
  
    scanf("%d%d%d", &l,&d,&n);
    for(int i=0;i<=d;i++)
        S[i]=getLine();
   // cout<<"|"<<S[1]<<"|"<<S[2];
    for(int i=1;i<=n;i++)
    {
      wczytaj();         
      printf("Case #%d: %d\n", i,sprawdz());                  
    }
 
   // system("PAUSE");
    return 0;
}
