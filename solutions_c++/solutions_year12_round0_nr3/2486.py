#include <cstdlib>
#include <iostream>
#include <math.h>
#include <fstream>
#include<map>
using namespace std;

int s,test,a,b;
int power(int a,int i){
    s=1;
for(int j=1;j<=i;j++)
s*=a;    
return s;
}
int solve(int a,int b){
    int c,res=0;
    map<int , map <int,bool> > m;
  if(a/10==0)
  return 0;
  else{
    for(int i=a;i<=b;i++){
            int n=(int)log10(i);
        for(int j=1;j<=(int)log10(i);j++){
            c=(i%power(10,j))*power(10,n)+(int)(i/power(10,j));        
              if(c>i&&c<=b&&c>=a && !m[i][c])
              {res++; m[i][c]=true;}
               n--;
        }    
    } 
    return res;    
  }     
}

void input(){

     
      ifstream cin("C-large.in");
      ofstream cout("C-large.out");
      
     cin>>test;
     for(int i=1;i<=test;i++){
        cin>>a>>b;
      cout<<"Case #"<<i<<": "<<solve(a,b)<<endl;          
     }     
}

int main(int argc, char *argv[])
{
    input();
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
