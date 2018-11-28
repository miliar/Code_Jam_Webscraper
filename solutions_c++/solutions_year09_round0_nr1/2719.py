#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;



int main(int argc, char *argv[])
{
    fstream f("data.in",ios::in);
    
    int l,n,d;
    
  	string words[5001];
  	string pattern;


 
    f>>l;
    f>>d;
    f>>n;
    cout<<"\n\n"<<l<<" "<<d<<" "<<n<<"\n\n";
    
    int i,j,k1,k0,match=1,is=0,final=0;
    
    for (i=0;i<d;i++){
        f>>words[i];
    }
    
    
    fstream f2("data.out",ios::out);
    
    for (i=0;i<d;i++){
        cout<<words[i]<<"\n";
    }

    cout<<"\n\n";

    for (i=0;i<n;i++){
       f>>pattern;       
       for (j=0;j<d;j++){
           k1=0;
           k0=0;
           while (match!=0 && k0<l){ 
               
               if (pattern[k1]=='('){
                 is=0;                      
                 while (pattern[k1]!=')'){
                    k1++;    
                    if (pattern[k1]==words[j][k0])is=1;
                 }
                 if (is==0)match=0;
               }else
               if (pattern[k1]!=words[j][k0])match=0;               
               k1++;
               k0++;
           }  
           if (match==1)final++;         
           match=1;
       }    
       f2<<"Case #"<<i+1<<": "<<final<<"\n";
       final=0;
    }

    f.close();
    f2.close();

    system("PAUSE");
    return EXIT_SUCCESS;
}
