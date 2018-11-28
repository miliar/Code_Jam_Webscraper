#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime>
#include <climits>  
#include <fstream>  

using namespace std;
typedef unsigned long long ull;

int arr[2000001];

int valid(int a, int &lima, int &limb)
{
    int mul =1;
    int cont=1;
    int in= a;
    int lim = int(log10(a));
    if(!arr[a]){
       for (int i=0 ; i<lim; i++)
          mul *= 10;
           
       for (int j=0 ; j<lim ; j++){
          a = a/10 + a % 10 *mul;
          
          
           if(a>=lima && a<=limb && !arr[a])
              if(int(log10(a))==lim && a!=in){
              arr[a]++;
              cont++;
           }
       }
        
       arr[in]++;
    }
    
    return  cont*(cont-1)/2;
    
}


    
int main()
{
    ifstream in("entrada.txt", ios::in);
    ofstream out("salidas.out", ios::out);
    int cases =0;
    int cas;
    int a,b;
    in>>cas;
    ull res =0;
   
    while(cas--)
    {
       in>>a>>b;
       res=0;
       memset(arr,0,sizeof(arr));
       for(int i=a; i<=b; i++)
          res+=valid(i,a,b);
      
       out<<"Case #"<<++cases<<": "<<res<<endl;
       
    }
   
}
