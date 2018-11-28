#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

int n,d,res;
int T[22][505];
string S;
string getLine() {
  string s;
  while(!feof(stdin)) {
    char c = fgetc(stdin);
    if(c == 13) continue;
    if(c == 10) return s;
    s += c;
    }
  return s;
  }

void clear()
{
for(int i=0;i<=20;i++)
for(int k=0;k<=500;k++)
T[i][k]=0;     
res=0;     
}

int main(int argc, char *argv[])
{
    string W=" welcome to code jam";
    scanf("%d",&n);
    S=getLine();
    for(int test=1;test<=n;test++)
    {
    clear();        
    S=getLine(); 
   // cout<<S; 
    d=S.length();
    for(int i=0;i<d;i++)
    if(S[i]==W[1])T[1][i]=1;
    
   
    for(int j=2;j<=19;j++)
    {
          int sumka=0; 
            for(int i=0;i<d;i++)
            {
            if(S[i]==W[j])T[j][i]=sumka;
            sumka+=T[j-1][i];
            sumka%=10000;
            }
    }
     for(int i=0;i<d;i++)
     {
     res+=T[19][i]; 
     res%=10000;  
     }  
            
     /*  for(int i=1;i<=20;i++){
       for(int k=1;k<=50;k++)
       cout<<T[i][k];
       cout<<endl;    
       } */
            
    printf("Case #%d: %04d\n", test, res);        
            
    }
    
    
    //system("PAUSE");
    return 0;
}
